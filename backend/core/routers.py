from rest_framework.routers import SimpleRouter
from core.user.viewsets import UserViewSet
from core.auth.viewsets import LoginViewSet, RegistrationViewSet, RefreshViewSet

routes = SimpleRouter()

routes.register('auth/login', LoginViewSet, basename='login')
routes.register('auth/register', RegistrationViewSet, basename='register')
routes.register('auth/refresh', RefreshViewSet, basename='refresh')
routes.register('user', UserViewSet, basename='user')

urlpatterns = [
    *routes.urls
]