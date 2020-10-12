from django.urls import path

from .views import checkout, HomeView, ItemDetailView, add_to_cart

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name="item-list"),
    path('checkout/', checkout, name="checkout"),
    path('product/<slug>', ItemDetailView.as_view(), name="product"),
    path('add-to-cart/<slug>/', add_to_cart, name="add-to-cart")
]
