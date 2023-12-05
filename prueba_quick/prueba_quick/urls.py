from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from crud.views import ClientViewSet, BillViewSet, ProductViewSet, BillProductViewSet
from usuarios.views import registro_usuario, login_usuario

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'bills', BillViewSet)
router.register(r'products', ProductViewSet)
router.register(r'billproducts', BillProductViewSet)

urlpatterns = [
    path('registro/', registro_usuario, name='registro_usuario'),
    path('login/', login_usuario, name='login_usuario'),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
