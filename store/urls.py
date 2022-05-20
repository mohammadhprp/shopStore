from django.urls import path
from django.urls.conf import include
from rest_framework_nested import routers
from .views import *

router = routers.DefaultRouter()
router.register('products', ProductViewSet, basename='products')
router.register('collections', CollectionViewSet)
router.register('carts', CartViewSet)
router.register('customers', CustomerViewSet)
router.register('orders', OrderViewSet, basename='orders')

products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('reviews', ReviewViewSet, basename='product-reviews')

carts_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
carts_router.register('items', CartItemViewSet, basename='cart-items')

# URLConf
urlpatterns = router.urls + products_router.urls + carts_router.urls

# urlpatterns += [
#     path('urls/', schema_view)
# ]  # If you Have specific patterns use this.


# d645bf8a-8910-45a3-ab86-7a952d91161f
