from django.conf.urls import url, include

from rest_framework import routers

from datageeks.api.views import PostCRUD, PostListAPIView, PostCreateAPIView, PostRetrieveAPIView, PostUpdateAPIView, PostDeleteAPIView


from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

router = routers.DefaultRouter()

router.register('postinfo', PostCRUD)

urlpatterns = [
    url(r'', include(router.urls)),
    url(r'^auth-token/', obtain_jwt_token),
    url(r'^auth-token-refresh/', refresh_jwt_token),
    url(r'^auth-token-verify/', verify_jwt_token),
    url(r'^post-list/', PostListAPIView.as_view()),
    url(r'^post-create/', PostCreateAPIView.as_view()),
    url(r'^post-retrieve/(?P<id>\d+)/$', PostRetrieveAPIView.as_view()),
    url(r'^post-update/(?P<pk>\d+)/$', PostUpdateAPIView.as_view()),
    url(r'^post-delete/(?P<pk>\d+)/$', PostDeleteAPIView.as_view()),
]