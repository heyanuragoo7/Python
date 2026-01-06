# from django.shortcuts import render
from django.http import HttpResponse
# from rest_framework.views import APIView

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password, check_password
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Users, Cart, CartItem
from .serializers import UserSerializer, CartSerializer, CartItemSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .permissions import IsAdminRole

# Create your views here.
def home(request):
    return HttpResponse("Home")

class Signup(APIView):
    def post(self, request):
        name = request.data.get('name')
        email = request.data.get('email')
        password = request.data.get('password')
        age = request.data.get('age')

        if not all([name, email, password, age]):
            return Response(
                {"error": "All fields are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if Users.objects.filter(email=email).exists():
            return Response(
                {"error": "Email already exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = Users.objects.create(
            name=name,
            email=email,
            password=make_password(password),  # bcrypt hash
            age=age
        )

        serializer = UserSerializer(user)
        return Response(
            {"message": "User registered successfully", "user": serializer.data},
            status=status.HTTP_201_CREATED
        )

class Login(APIView):
    
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user = Users.objects.get(email=email)
        except Users.DoesNotExist:
            return Response(
                {"error": "Invalid credentials"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        if not check_password(password, user.password):
            return Response(
                {"error": "Invalid credentials"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        refresh = RefreshToken.for_user(user)
        refresh["role"] = user.role

        return Response({
            "message": "Login successful",
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "user": {
                "id": user.id,
                "name": user.name,
                "email": user.email
            }
        })

class CartView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminRole]

    def get(self, request):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        serializer = CartSerializer(cart) 
        return Response(serializer.data)

    # def post(self, request):
    #     cart, created = Cart.objects.get_or_create(user=request.user)
    #     serializer = CartSerializer(cart)
    #     return Response(
    #         {"message": "Cart created", "cart": serializer.data},
    #         status=status.HTTP_201_CREATED
    #     )

class AddToCart(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        cart, _ = Cart.objects.get_or_create(user=request.user)

        product_name = request.data.get("product_name")
        price = request.data.get("price")
        quantity = request.data.get("quantity", 1)

        if not product_name or not price:
            return Response(
                {"error": "Product name and price are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        item = CartItem.objects.create(
            cart=cart,
            product_name=product_name,
            price=price,
            quantity=quantity
        )

        serializer = CartItemSerializer(item)
        return Response(
            {"message": "Item added to cart", "item": serializer.data},
            status=status.HTTP_201_CREATED
        )


class UpdateCartItem(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, item_id):
        try:
            item = CartItem.objects.get(
                id=item_id,
                cart__user=request.user
            )
        except CartItem.DoesNotExist:
            return Response(
                {"error": "Item not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        item.quantity = request.data.get("quantity", item.quantity)
        item.price = request.data.get("price", item.price)
        item.save()

        serializer = CartItemSerializer(item)
        return Response(
            {"message": "Cart item updated", "item": serializer.data}
        )

class DeleteCartItem(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, item_id):
        try:
            item = CartItem.objects.get(
                id=item_id,
                cart__user=request.user
            )
        except CartItem.DoesNotExist:
            return Response(
                {"error": "Item not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        item.delete()
        return Response(
            {"message": "Item removed from cart"},
            status=status.HTTP_204_NO_CONTENT
        )
