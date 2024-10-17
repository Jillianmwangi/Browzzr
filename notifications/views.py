from django.shortcuts import render

# Create your views here.
# notifications/views.py
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Notification

class NotificationListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notifications = Notification.objects.filter(recipient=request.user, read=False)
        data = [{'actor': str(notification.actor), 'verb': notification.verb, 'target': str(notification.target), 'timestamp': notification.timestamp} for notification in notifications]
        return Response(data)

class MarkNotificationsReadView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        notifications = Notification.objects.filter(recipient=request.user, read=False)
        notifications.update(read=True)
        return Response({'message': 'Notifications marked as read'})
