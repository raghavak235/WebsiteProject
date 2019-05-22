from django.conf.urls import url, include

from rest_framework import routers

from datageeks.api.views import PostCRUD


from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

router = routers.DefaultRouter()

router.register('postinfo', PostCRUD)

urlpatterns = [
    url(r'', include(router.urls)),
    url(r'^auth-token/', obtain_jwt_token),
    url(r'^auth-token-refresh/', refresh_jwt_token),
    url(r'^auth-token-verify/', verify_jwt_token),

]