from rest_framework import generics, viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from base.models import Dict, MetaFields, Mts, Magazine, Adidas, FavouriteDatasets
from base.serializers import DictSerializer, MetaFieldsSerializer, MtsSerializer, MagazineSerializer, AdidasSerializer, \
    MetaFieldsSerializerFilter, FavouriteDatasetsSerializer
from mozilla_django_oidc.views import OIDCLogoutView
from django.conf import settings
from django_filters.rest_framework import DjangoFilterBackend


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


class MagazineAttributeSortView(generics.ListAPIView):
    serializer_class = MagazineSerializer

    def get_queryset(self):
        attributes = self.request.GET.get("attributes")
        attributes = '-' + attributes
        return Magazine.objects.order_by(attributes)


class FilterListViewSet(generics.ListAPIView):
    serializer_class = MetaFieldsSerializer
    queryset = MetaFields.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'quality', 'type']
    ordering_fields = ['date_start', 'date_finish']


@api_view(['GET'])
def buy_datasets(request):
    id = request.GET.get("id")
    model = MetaFields.objects.get(id=id)
    model.payable = 0
    model.save()
    return Response({'status': 'Успешно'}, status=status.HTTP_200_OK)


@api_view(['GET'])
def favourite_datasets(request):
    id = request.GET.get("id")
    favourite = FavouriteDatasets.objects.create(metafields_id=id)
    return Response({'status': 'Успешно'}, status=status.HTTP_200_OK)


class FavouriteDatasetsView(generics.ListAPIView):
    serializer_class = FavouriteDatasetsSerializer
    queryset = FavouriteDatasets.objects.all()
