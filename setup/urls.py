from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet, GroupViewSet, userLogadoViewset
from rest_framework.authtoken import views
from product.views import productViewSet, messageViewSet, bagViewSet, sacoleiraProducts, commentViewset, productDetail
from account.views import profileViewset, sacoleirasViewset, profileDetail
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'messages', messageViewSet)
router.register(r'userLogado', userLogadoViewset, basename='userlogado')
router.register(r'bag', bagViewSet, basename='bag')
router.register(r'comments', commentViewset)
router.register(r'products', productViewSet)
router.register(r'profile', profileViewset, basename='profile')
router.register(r'sacoleiras', sacoleirasViewset, basename='sacoleiras')


urlpatterns = [
    path('', include(router.urls)),
    path('sacoleiras/<int:id>/products/', sacoleiraProducts.as_view()),
    path('sacoleiras/<int:id>/products/<int:pk>', productDetail.as_view()),
    path('profileDetail/<int:pk>/', profileDetail.as_view()),
    path('api-token-auth/', views.obtain_auth_token, name='api-tokn-auth'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
