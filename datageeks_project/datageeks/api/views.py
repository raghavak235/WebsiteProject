from rest_framework import viewsets
from datageeks.api.serializers import PostSerializer
from datageeks.models import Post
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, \
    ListCreateAPIView, RetrieveUpdateAPIView


#  API VIEW SET CODE
class PostListAPIView(APIView):
    def get(self, request, format=None):
        qs = Post.objects.all()
        serializer = PostSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request):
        #pass
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            Title = serializer.data.get('title')
            print('Title :', Title)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer, status=status.HTTP_400_BAD_REQUEST)
        # Return this if request method is not POST
        # return Response({'key': 'value'}, status=status.HTTP_200_OK)

    def put(self, request, pk=None):
        #pass
        data = request.data
        serializer = Post.objects.get(id=data.get('id'))
        serializer.title = data.get('title')
        serializer.content = data.get('content')
        if serializer is not None:
            serializer.save()
            return Response(serializer, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#
# class PostListAPIView(ListAPIView):
#     serializer_class = PostSerializer
#
#     def get_queryset(self):
#         qs = Post.objects.all()
#         qtitle = self.request.GET.get('title')
#         if qtitle is not None:
#             qs = qs.filter(title__icontains=qtitle)
#         return qs


class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostRetrieveAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'


class PostUpdateAPIView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostListCreateAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


#  View Set Code
class PostCRUD(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    # authentication_classes = [JSONWebTokenAuthentication, ]
    # permission_classes = [IsAuthenticated, ]
