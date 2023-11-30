from django.urls import include, path
from rest_framework import routers
from chorobesity import views
from django.views.generic.base import RedirectView

router = routers.DefaultRouter()
router.register(r'states', views.StateListViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', RedirectView.as_view(url='/api/states', permanent=False), name='index')
]
