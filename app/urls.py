from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from app.class_views.auth_control_views import LoginView, LoginAction, \
    HomeView, LogoutAction
from app.class_views.roles_views import RolesView, RoleCreateView, \
    RolDeactivateView
from app.class_views.quotation_views import QuotationsView, \
    QuotationsCreateView, QuotationStateView
from app.class_views.users_views import UsersListView, UsersCreateView
from app.class_views.stock import StockView, StockCreateView, RawMaterial, \
    RawMaterialCreateView, StockOperatorView, StrockOperatorUdateView, \
    ProjectsView, ProjectCreateView, ProjectDetailsView, ProjectPersonalCreate

urlpatterns = [
    url(r'^$', LoginView.as_view(), name="login"),
    url(r'^login_action/$', LoginAction.as_view(), name="login_action"),
    url(r'^logout_action/$', LogoutAction.as_view(), name="logout_action"),
    url(r'^home/$', login_required(HomeView.as_view()), name="home"),

    # Users
    url(r'^employees/$', login_required(UsersListView.as_view()), name="users"),
    url(r'^employees/create_form$', login_required(UsersCreateView.as_view()),
        name="create_form$"),
    url(r'^employees/create_action', login_required(UsersCreateView.as_view()),
        name="users_create_action"),
    url(r'^employees/delete_action', login_required(UsersListView.as_view()),
        name="users_delete_action"),

    # Roles
    url(r'^roles/$', login_required(RolesView.as_view()), name="roles"),
    url(r'^roles/create$', login_required(RoleCreateView.as_view()),
        name="roles_create"),
    url(r'^roles/delete', login_required(RolDeactivateView.as_view()),
        name="roles_delete"),

    # Projects
    url(r'^projects/$', login_required(ProjectsView.as_view()),
        name="projects"),
    url(r'^projects/create_form/$', login_required(ProjectCreateView.as_view()),
        name="projects_create_form"),
    url(r'^projects/create_action/$',
        login_required(ProjectCreateView.as_view()),
        name="projects_create_action"),
    url(r'^projects/details/(?P<pr_pk>[0-9]+)/$',
        login_required(ProjectDetailsView.as_view()),
        name="projects_details"),
    # Projects -> Quotations
    url(r'^projects/quotation/$', login_required(QuotationsView.as_view()),
        name="quotations"),
    url(r'^projects/quotation_create/(?P<pr_pk>[0-9]+)/$',
        login_required(QuotationsCreateView.as_view()),
        name="projects_quotation_create"),
    url(r'^quotations/create_action/$',
        login_required(QuotationsCreateView.as_view()),
        name="projects_quotations_create_action"),
    url(r'^quotations/change_state/$',
        login_required(QuotationStateView.as_view()),
        name="quotations_change_state"),
    # Projects -> Personal
    url(r'^projects/personal/(?P<pr_pk>[0-9]+)/$',
        login_required(ProjectPersonalCreate.as_view()), name="project_personal"),
    url(r'^projects/personal_action/$',
        login_required(ProjectPersonalCreate.as_view()),
        name="project_personal_action"),

    # Stock
    url(r'^raw_material/$', login_required(RawMaterial.as_view()),
        name="raw_material"),
    url(r'^raw_material/create_form/$', login_required(
        RawMaterialCreateView.as_view()), name="raw_material_create_form"),
    url(r'^raw_material/create_action/$', login_required(
        RawMaterialCreateView.as_view()), name="raw_material_create_action"),
    url(r'^stock/operator/$', login_required(StockOperatorView.as_view()),
        name="stock_operator"),
    url(r'^stock/operator_stock_update_form/$',
        login_required(StrockOperatorUdateView.as_view()),
        name="stock_operator_update_form"),
    url(r'^stock/operator_stock_update_action/$',
        login_required(StrockOperatorUdateView.as_view()),
        name="operator_stock_update_action"),
    url(r'^stock/$', login_required(StockView.as_view()),
        name="stock"),
    url(r'^stock/create_form/$', login_required(StockCreateView.as_view()),
        name="stock_create_form"),
    url(r'^stock/create_action/$', login_required(StockCreateView.as_view()),
        name="stock_create_action"),
]
