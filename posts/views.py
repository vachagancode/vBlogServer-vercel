from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import PostSerializer
from .models import Post

@api_view(['GET'])
def getPosts(request):
	PostData = Post.objects.all()
	serializer = PostSerializer(data=PostData, many=True)
	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['GET'])
def getSpecialPost(request, pk):
	PostData = Post.objects.get(id=pk)
	serializer = PostSerializer(PostData)
	return Response(serializer.data)

@api_view(['POST'])
def addPosts(request):
	serializer = PostSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['PUT'])
def editSpecificPost(request, pk):
	PostData = Post.objects.get(id=pk)
	serializer = PostSerializer(PostData, data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['DELETE'])
def deletePost(reqeust, pk):
	try:
		post = Post.objects.get(id=pk)
	except:
		return Response("The Post Does Not Exist !")

	post.delete()
	return Response("Deleted Successfully")