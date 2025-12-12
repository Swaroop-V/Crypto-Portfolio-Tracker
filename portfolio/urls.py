from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AssetViewSet, dashboard

router = DefaultRouter()
router.register(r'assets', AssetViewSet)

urlpatterns = [
    path('api/', include(router.urls)), # API Endpoints
    path('', dashboard, name='dashboard'), # Visualization
]