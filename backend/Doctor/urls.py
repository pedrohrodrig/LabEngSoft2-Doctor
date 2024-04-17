from django.urls import path

from .views import DoctorView, EvaluationView

urlpatterns = [
    # path doctor
    path("Doctor/", DoctorView.as_view(actions={"post": "create", "get": "list_all"})),
    path("Doctor/<int:pk>/", DoctorView.as_view(actions={"get": "retrieve"})),
    path("Doctor_from_id/<int:id_user>/", 
        DoctorView.as_view(actions={"get": "list_from_professional_id"}),
    ),
    path("evaluation/list/", EvaluationView.as_view(actions={"get": "list_all"})),
    path("evaluation/create/", EvaluationView.as_view(actions={"post": "create"})),
    path("evaluation/<int:pk>/", EvaluationView.as_view(actions={"get": "retrieve", "delete": "delete"})),
    path("evaluation_from_patient/<int:pk>/", EvaluationView.as_view(actions={"get": "retrieve_by_patient"})),
]