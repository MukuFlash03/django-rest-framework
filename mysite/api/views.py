from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import BlogPost
from .serializers import BlogPostSerializer

# Create your views here.

class BlogPostListCreate(generics.ListCreateAPIView):
	queryset = BlogPost.objects.all()
	serializer_class = BlogPostSerializer

	def get(self, request, *args, **kwargs):
		print("GET request received - getting all blog posts")
		queryset = BlogPost.objects.all()
		serializer = BlogPostSerializer(queryset, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def delete(self, request, *args, **kwargs):
		print("DELETE request received - deleting all blog posts")
		BlogPost.objects.all().delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	queryset = BlogPost.objects.all()
	serializer_class = BlogPostSerializer
	lookup_field = "pk"

class BlogPostList(APIView):
	def get(self, request, format=None):
		title = request.query_params.get("title", "")

		if title:
			blog_posts = BlogPost.objects.filter(title__icontains=title)
		else:
			blog_posts = BlogPost.objects.all()
		
		serializer = BlogPostSerializer(blog_posts, many=True)

		return Response(serializer.data, status=status.HTTP_200_OK)
