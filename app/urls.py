from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from app.class_views.auth_control_views import LoginView, LoginAction, \
    HomeView, LogoutAction
from app.class_views.roles_views import RolesView, RoleCreateView, RolDeactivateView
from app.class_views.quotation_views import QuotationsView, QuotationsCreateView, QuotationStateView
from app.class_views.users_views import UsersListView, UsersCreateView
from app.class_views.stock import StockView, StockCreateView

urlpatterns = [
    url(r'^$', LoginView.as_view(), name="login"),
    url(r'^login_action/$', LoginAction.as_view(), name="login_action"),
    url(r'^logout_action/$', LogoutAction.as_view(), name="logout_action"),
    url(r'^home/$', login_required(HomeView.as_view()), name="home"),

    # Users
    url(r'^employees/$', login_required(UsersListView.as_view()), name="users"),
    url(r'^employees/create_form$', login_required(UsersCreateView.as_view()), name="create_form$"),
    url(r'^employees/create_action', login_required(UsersCreateView.as_view()), name="users_create_action"),
    url(r'^employees/delete_action', login_required(UsersListView.as_view()), name="users_delete_action"),

    # Roles
    url(r'^roles/$', login_required(RolesView.as_view()), name="roles"),
    url(r'^roles/create$', login_required(RoleCreateView.as_view()),
        name="roles_create"),
    url(r'^roles/delete', login_required(RolDeactivateView.as_view()),
        name="roles_delete"),

    # Quotations
    url(r'^quotations/$', login_required(QuotationsView.as_view()),
        name="quotations"),
    url(r'^quotations/create/$', login_required(QuotationsCreateView.as_view()),
        name="quotations_create"),
    url(r'^quotations/create_action/$', login_required(QuotationsCreateView.as_view()),
        name="quotations_create_action"),
    url(r'^quotations/change_state/$', login_required(QuotationStateView.as_view()),
        name="quotations_change_state"),

    # Stock
    url(r'^stock/$', login_required(StockView.as_view()),
        name="stock"),
    url(r'^stock/create_form/$', login_required(StockCreateView.as_view()),
        name="stock_create_form"),
    url(r'^stock/create_action/$', login_required(StockCreateView.as_view()),
        name="stock_create_action"),
]
