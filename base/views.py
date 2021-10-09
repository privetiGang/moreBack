from django.db.models import Avg, Max, Min, Sum
from rest_framework import generics
from base.models import Dict, MetaFields, Mts, Magazine, Adidas
from base.serializers import DictSerializer, MetaFieldsSerializer, MtsSerializer, MagazineSerializer, AdidasSerializer
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


class MetaFieldListView(generics.ListAPIView):
    serializer_class = MetaFieldsSerializer
    queryset = MetaFields.objects.all()


class MtsListView(generics.ListAPIView):
    serializer_class = MtsSerializer
    queryset = Mts.objects.all()


class MagazineListView(generics.ListAPIView):
    serializer_class = MagazineSerializer
    queryset = Magazine.objects.all()


class AdidasListView(generics.ListAPIView):
    serializer_class = AdidasSerializer
    queryset = Adidas.objects.all()


class MtstAtributeAggregateView(generics.ListAPIView):
    serializer_class = MtsSerializer

    def get_queryset(self):
        attributes = self.request.GET.get("attributes")
        return Mts.objects.all().aggregate(Avg(attributes))


class MtsAttributeMaxView(generics.ListAPIView):
    serializer_class = MtsSerializer

    def get_queryset(self):
        attributes = self.request.GET.get("attributes")
        return Mts.objects.all().aggregate(Max("sum"))


class MtsAttributeMinView(generics.ListAPIView):
    serializer_class = MtsSerializer

    def get_queryset(self):
        attributes = self.request.GET.get("attributes")
        return Mts.objects.all().aggregate(Min(attributes))


class MtsAttributeSumView(generics.ListAPIView):
    serializer_class = MtsSerializer

    def get_queryset(self):
        attributes = self.request.GET.get("attributes")
        return Mts.objects.all().aggregate(Sum(attributes))


class MagazineAttributeSortView(generics.ListAPIView):
    serializer_class = MagazineSerializer

    def get_queryset(self):
        attributes = self.request.GET.get("attributes")
        attributes = '-' + attributes
        return Magazine.objects.order_by(attributes)
