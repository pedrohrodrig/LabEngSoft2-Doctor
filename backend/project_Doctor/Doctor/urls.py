from django.urls import path

from .views import DoctorView

urlpatterns = [
    path("Doctor/", DoctorView.as_view(actions={"post": "create", "get": "list_all"})),
    path("Doctor/<int:pk>/", DoctorView.as_view(actions={"get": "retrieve"})),
]