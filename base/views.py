from rest_framework import generics
from base.models import Dict
from base.serializers import DictSerializer
from mozilla_django_oidc.views import OIDCLogoutView
from django.conf import settings


class DictListView(generics.ListAPIView):
    serializer_class = DictSerializer

    def get_queryset(self):
        id = self.request.GET.get("id")
        return Dict.objects.filter(id=id)


class DictCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Dict.objects.all()
    serializer_class = DictSerializer


class DictDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Dict.objects.all()
    serializer_class = DictSerializer


def keycloak_logout(request):
    """ Ths method is used to retrieve logout endpoint to also end the keycloak session as well as the Django session.
    """
    logout_endpoint = settings.OIDC_OP_LOGOUT_ENDPOINT
    return logout_endpoint + "?redirect_uri=" + request.build_absolute_uri(settings.LOGOUT_REDIRECT_URL)


class LogoutView(OIDCLogoutView):
    """ Extend standard logout view to include get method (called from URL)
    """

    def get(self, request):
        return self.post(request)
