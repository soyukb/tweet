from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions,status
from django.contrib.auth import login
from . import serializers
from tweet_api_project.models import Tweet

class UserRegistView(APIView):
    serializer_class = serializers.UserRegistSerializer
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data)
        
class UserLoginView(APIView):
    serializer_class = serializers.UserLoginSerializer
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data,context={'request':request})
        if serializer.is_valid():  
            user = serializer.validated_data['user']    
            login(request,user)
            return Response('ログインしました',status=status.HTTP_202_ACCEPTED) 
        return Response('リクエストが誤っています', status=status.HTTP_400_BAD_REQUEST)
             

class TweetListView(APIView):
    serializer_class = serializers.TweetSerializer
   
    def get(self,request):
        tweets = Tweet.objects.all().order_by('-created_at')
        serializers = self.serializer_class(tweets, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={
            'user': request.user,
        })
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response("リクエストの内容に誤りがあります", status=status.HTTP_400_BAD_REQUEST)
