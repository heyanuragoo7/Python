from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password, check_password

from .serializers import UserSerializer, BlogSerializer
from .models import User, Blog

# Create your views here.

class DefaultView(APIView):
    # permission_classes = [permissions.AllowAny]

    def get(self, request):
        return Response(
            {
                "message": "API is Working"
            },
            status = status.HTTP_200_OK
        )

class SignupView(APIView):

    def post(self, request):
        name = request.data.get("name")
        email = request.data.get("email")
        password = request.data.get("password")
        age = request.data.get("age")

        if not all([name, email, password, age]):
            return Response(
                {"error": "All fields Required!"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if User.objects.filter(email=email).exists():
            return Response(
                {"error": "Email Exists, Provide Another Email"}
            )
        
        user = User.objects.create(
            name = name,
            email = email,
            password = make_password(password),
            age = age
        )

        serialize_data = UserSerializer(user)

        return Response(
            {
                "message": "User Created",
                "data": serialize_data.data
            },
            status = status.HTTP_201_CREATED,
        )
    
class LoginView(APIView):

    def post(self, request):

        try:
            email = request.data.get("email")
            password = request.data.get("password")

            if not all([email, password]):
                return Response(
                    {
                        "error": "All fields Required"
                    }
                )
            
            if not User.objects.filter(email=email).exists():
                return Response(
                    {
                        "error": "Not Exists Email"
                    }
                )
            
            user = User.objects.get(email=email)
            
            if not check_password(password, user.password):
                return Response(
                    {
                        "error": "Correct Password Required"
                    }
                )
            
            refresh = RefreshToken.for_user(user)
            refresh['role'] = user.role

            return Response(
                {
                    "message": "User LoggedIn",
                    "token": str(refresh.access_token), # str(refresh.access_token),
                    "user": {
                        "name": user.name,
                        "email": user.email
                    }
                },
                status = status.HTTP_200_OK
            )
        
        except Exception as e:
            return Response(
                {
                    "message": "INTERNAL_SERVER_ERROR",
                },
                status = status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class BlogView(APIView):

    def get(self, request):

        blogs = Blog.objects.all()

        serialized_data = BlogSerializer(blogs, many=True)

        return Response(
            {
                "message": "Blogs Fetched",
                "data": serialized_data.data
            },
            status = status.HTTP_200_OK
        )

    def post(self, request):

        id = request.data.get("owner")
        name = request.data.get("name")
        content = request.data.get("content")

        if not all([name, content]):
            return Response(
                {
                    "data": "All fields Required!"
                }
            )
        
        user = User.objects.get(id=id)
        print(user.id)
        print("HI USER,",user)
        
        blog = Blog.objects.create(
            owner = user.id,
            name = name,
            content = content
        )

        serialized_data = BlogSerializer(blog)

        return Response(
            {
                "message": "Blog Data Fetched Successfully",
                "data": serialized_data.data
            },
            status = status.HTTP_201_CREATED
        )
    
