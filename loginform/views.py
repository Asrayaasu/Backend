from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import CustomUser
# Create your views here.
@api_view(['POST'])
def register_user(request):
    email = request.data.get('email')
    password = request.data.get('password')
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    if not (email and password and first_name and last_name):
        return Response({"error": "All fields are required"}, status=400)
    if CustomUser.objects.filter(email=email).exists():
        return Response({"error": "User already exists"}, status=400)
    user = CustomUser.objects.create_user(
    email=email, password=password, first_name=first_name,
    last_name=last_name
    )
    return Response({"message": "User created successfully"}, status=201)
@api_view(['POST'])
def login_user(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(request, email=email, password=password)
    if user is not None:
        refresh = RefreshToken.for_user(user)
        return Response({
        "refresh": str(refresh),
        "access": str(refresh.access_token),
        })
    return Response({"error": "Invalid credentials"}, status=401)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response({"message": f"Hello {request.user.email}, this is a protected view!"}, status=200)