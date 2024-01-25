
from django.contrib import admin
from django.urls import path,include
from todoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.RegistrationView.as_view(),name="register"),
    path("login/",views.LoginView.as_view(),name="signin"),
    path("index/",views.IndexView.as_view(),name="index"),
    path("todos/<int:pk>/change",views.TodoUpdateView.as_view(),name="todo-change"),
    path("todos/<int:pk>/remove",views.TodoDeleteView.as_view(),name="todo-delete"),
    path("logout/",views.SignOutView.as_view(),name="signout"),
    path("api/",include("api.urls")),
]
