from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_view),
    path('products/', views.product_view),
    path('new/', views.new)
]