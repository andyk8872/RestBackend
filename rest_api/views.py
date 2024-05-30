from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer


# Create your views here.

# Class based Views

class PostsAPIView(APIView):
    """
    List all posts, or create a new post.
    """
    def get(self, request):
        """1"""
        posts = Post.objects.all() #queryset
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        """2"""
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class postDetailsAPIView(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        """3"""
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#Function Views

@api_view(['GET', 'POST'])
def PostView(request):
    """
    List all code posts, or create a new post.
    """
    if request.method == 'GET':
        posts = Post.objects.all() #queryset
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def posts_detail(request, pk):
    """1"""
    try:
        post = Post.objects.get(pk=pk) #instance
    except Post.DoesNotExist:
        return Response(status=404 )

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        post.delete()
        return Response(status=204)
    