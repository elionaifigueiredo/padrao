from django.urls import path
from .import views

urlpatterns = [
    path('logar', views.logar_user, name="logar_user"),
    path('logout_view', views.logout_view, name="logout_view")
]