from rest_framework import viewsets
from datageeks.api.serializers import PostSerializer
from datageeks.models import Post
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated


class PostCRUD(viewsets.ModelViewSet):

    serializer_class = PostSerializer
    queryset = Post.objects.all()
    authentication_classes = [JSONWebTokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]
