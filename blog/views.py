from django.shortcuts import render

from blog.serializers import BlogSerializer
from .models import Blog
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import Http404
# Create your views here.

class BlogView(APIView):

    permission_classes = [IsAuthenticated]



    def get(self, request, format=None):
        snippets = Blog.objects.all()
        serializer = BlogSerializer(snippets, many=True)
        return Response(serializer.data)
       

    def post(self,request, *args, **kwargs):
    

        serializer =  BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
      
            return Response({
                
                "message": "Post successfully Created.",
            })
        return Response(serializer.errors)

class BlogDetailsView(APIView):

    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Blog.objects.get(id=pk)
        except Blog.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(id=pk)
        serializer =  BlogSerializer(snippet)
        return Response(serializer.data)
      
class BlogSearchview(APIView):


    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Blog.objects.get(text__icontains=pk)
        except Blog.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer =  BlogSerializer(snippet)
        return Response(serializer.data)
