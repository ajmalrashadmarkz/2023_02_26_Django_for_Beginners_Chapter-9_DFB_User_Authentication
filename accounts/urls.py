from django.urls import path
from . import views
urlpatterns = [
    path("test/",views.test,name="test"),
    path("signup/",views.SignUpView.as_view(),name = "signup"),
]