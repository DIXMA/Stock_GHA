from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from app.class_views.auth_control_views import LoginView, LoginAction, \
    HomeView, LogoutAction
from app.class_views.roles_views import RolesView, RoleCreateView

urlpatterns = [
    url(r'^$', LoginView.as_view(), name="login"),
    url(r'^login_action/$', LoginAction.as_view(), name="login_action"),
    url(r'^logout_action/$', LogoutAction.as_view(), name="logout_action"),
    url(r'^home/$', login_required(HomeView.as_view()), name="home"),
    url(r'^roles/$', login_required(RolesView.as_view()), name="roles"),
    url(r'^roles/create$', login_required(RoleCreateView.as_view()),
        name="roles_create"),
    url(r'^quotations/$', login_required(RolesView.as_view()), name="quotations"),
]
