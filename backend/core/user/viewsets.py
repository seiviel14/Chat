from .serializers import UserSerializer
from .models import User

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters

class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.OrderingFilter)
    ordering_fields = ['updated']
    ordering = ['-updated']

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()

    def get_object(self):
        lookup_field_value = self.kwargs[self.lookup_field]
        object = User.objects.get(lookup_field_value)
        self.check_object_permissions(self.request, object)

        return object