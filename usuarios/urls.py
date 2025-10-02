from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.home_view, name="home"),   # 👈 Aquí agregamos el home
    path("registro/", views.registro_view, name="registro"),
    path("login/", views.login_view, name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("perfil/", views.perfil_view, name="perfil"),

    path('revision/', views.revision_view, name='revision'),
    path('planificacion/', views.planificacion_view, name='planificacion'),
    path('desarrollo/', views.desarrollo_view, name='desarrollo'),
    path('enviar/', views.enviar_view, name='enviar'),
    path('reunion/', views.reunion_view, name='reunion'),
]