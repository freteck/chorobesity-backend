from django.urls import include, path
from rest_framework import routers
from chorobesity import views

router = routers.DefaultRouter()
router.register(r'states', views.StateListViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
