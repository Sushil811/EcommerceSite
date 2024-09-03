from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home ),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('category/<slug:val>/', views.CategoryView.as_view(), name='category' ),
    path('category-title/<val>/', views.CategoryTitle.as_view(), name='category-title' ),
    path('product-details/<int:pk>/', views.ProductDetails.as_view(), name='product-details' ),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)