from django.http import response
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import serializers,status
from .models import CategoryModel,ProductModel
from .serializers import CategoryModelSerializer,ProductModelSerializer
# Create your views here.

@api_view(['GET','POST'])
def post_list(request):
    if request.method == 'GET':#Get means  to read the data
        posts = ProductModel.objects.all()
        serializer = ProductModelSerializer(posts,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':#Post means to create/insert the data
        # data = JSONParser.parse(re  quest)
        serializer = ProductModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def post_detail(request,pk):
    try:
        post = ProductModel.objects.get(pk=pk)
    except ProductModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProductModelSerializer(post)
        return Response(serializer.data)
    elif request.method == 'PUT':
        # data = JSONParser().parse(request)
        serializer = ProductModelSerializer(post,data=request.data)
        if serializer.is_valid():
            print('put data')
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        post.delete()
        print('data deleted at the specific id')
        return Response(status=status.HTTP_204_NO_CONTENT)
