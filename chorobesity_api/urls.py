from django.urls import include, path
from rest_framework import routers
from chorobesity import views

router = routers.DefaultRouter()
router.register(r'', views.CountyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
