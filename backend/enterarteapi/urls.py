from .views import responseViewSet

path.data('api/response', responseViewSet)

from django.urls import path, include
# from rest_framework import routers
from .views import responseViewSet

router = path.DefaultRouter()
router.register('response', responseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from django.urls import path
from .views import responseList, responseDetail

urlpatterns = [
    path('response/', responseList.as_view()),
    path('response/<int:pk>/', responseDetail.as_view())
]
