"""datasets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import mozilla_django_oidc
import mozilla_django_oidc.views
from django.contrib import admin
from django.urls import path, include

import base
from base.views import DictCreateView, DictDeleteView, DictListView, MetaFieldListView, MtsListView, MagazineListView, \
    MagazineAttributeSortView, AdidasListView, MtsAttributeMaxView, MtsAttributeMinView, MtsAttributeSumView, \
    MtstAtributeAggregateView, TypeDataSetView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/create', DictCreateView.as_view()),
    path('api/delete/<int:pk>', DictDeleteView.as_view()),
    path('api/get/', DictListView.as_view()),
    path('oidc/', include('mozilla_django_oidc.urls')),
    path("accounts/login/", mozilla_django_oidc.views.OIDCAuthenticationRequestView.as_view(), name="keylcoak_login"),
    path("accounts/logout/", base.views.LogoutView.as_view(), name="keycloak_logout"),
    path("oidc/callback/", mozilla_django_oidc.views.OIDCAuthenticationCallbackView.as_view(),
         name="keycloak_callback"),
    path('metafields/', MetaFieldListView.as_view()),
    path('mts/', MtsListView.as_view()),
    path('adidas/', AdidasListView.as_view()),
    path('type-dataset/', TypeDataSetView.as_view()),
    path('magazine/', MagazineListView.as_view()),
    path('magazine-dataset/sort/', MagazineAttributeSortView.as_view()),
    path('mts-dataset/max/', MtsAttributeMaxView.as_view()),
    path('mts-dataset/min/', MtsAttributeMinView.as_view()),
    path('mts-dataset/sum/', MtsAttributeSumView.as_view()),
    path('mts-dataset/avg/', MtstAtributeAggregateView.as_view()),

]
