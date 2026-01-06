from fastapi import BackgroundTasks
import time

# Background task example
def send_email_background(email: str, message: str):
    # Simulate sending email (in real app, use actual email service)
    time.sleep(2)  # Simulate delay
    print(f"Email sent to {email}: {message}")

# Another background task for logging
def log_user_action(user_id: str, action: str):
    print(f"User {user_id} performed action: {action}")