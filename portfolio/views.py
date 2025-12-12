from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Asset
from .serializers import AssetSerializer
from .utils import get_live_price
import json

# API View for CRUD operations
class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

# Dashboard View for Visualization
def dashboard(request):
    assets = Asset.objects.all()
    labels = []
    data = []

    for asset in assets:
        live_price = get_live_price(asset.symbol.lower())
        total_value = live_price * asset.quantity
        
        labels.append(asset.symbol.upper())
        data.append(total_value)

    context = {
        'labels': json.dumps(labels),
        'data': json.dumps(data),
    }
    return render(request, 'dashboard.html', context)