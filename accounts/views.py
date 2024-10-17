from django.contrib.auth import authenticate, login
from pyexpat.errors import messages
from urllib import request
from django.forms import PasswordInput
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import CustomUser
from .serializers import UserSerializer

class FollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        user_to_follow = self.get_object()
        if request.user != user_to_follow:
            request.user.following.add(user_to_follow)
            return Response({'status': 'now following'}, status=status.HTTP_200_OK)
        return Response({'error': 'You cannot follow yourself'}, status=status.HTTP_400_BAD_REQUEST)

class UnfollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        user_to_unfollow = self.get_object()
        request.user.following.remove(user_to_unfollow)
        return Response({'status': 'unfollowed'}, status=status.HTTP_200_OK)
    



class RegisterView(View):
    def get(self, request):
        # Handle GET request
        return render(request, 'register.html')

    def post(self, request):
        # Handle POST request
        return HttpResponse("User registered!")
    
class LoginView(View):
    def post(self, request):
        # Get the username and password from the form submission
        username = request.POST.get('Ozzy18')  
        password = request.POST.get('987654321')  # Replace 'password' with the form field name for password
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Login the user if authentication is successful
            login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('home')  # Redirect to home or another page
        
        else:
            # Authentication failed, return to login page with error message
            messages.error(request, 'Invalid username or password.')
            return render(request, 'login.html')