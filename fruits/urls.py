from fruits.apps import FruitsConfig
from django.urls import path
from . import views

app_name = FruitsConfig.name

urlpatterns = [
    # Add your URL patterns here
    path('', views.FruitsListAPIView.as_view()),
    path('create/', views.FruitsCreateAPIView.as_view(), name="fruits-create"),
    path('<int:pk>/', views.FruitsUpdateAPIView.as_view(), name="fruits-update"),
]