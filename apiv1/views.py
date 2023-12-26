from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions,status
from . import serializers

class UserRegistView(APIView):
    serializer_class = serializers.UserRegistSerializer
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data)
        
        

class TweetListView(APIView):
    def get(self,request):
        return Response('GET')