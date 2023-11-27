from django.urls import path
from .views import views

app_name = 'checkDate'
urlpatterns = [
    # MedicalExamination
    path('medical-examination/', views.MedicalExaminations.as_view(), name='me-ex'),
    path("me-create", views.CreateMedicalExaminationView.as_view(), name='me-create'),
    path("me-delete/<int:pk>", views.MedicalExaminationDeleteView.as_view(), name='me-delete'),
    path("me-view/<int:pk>", views.MedicalExaminationDetailView.as_view(), name='me-view'),
    path("me-update/<int:pk>", views.MedicalExaminationUpdateView.as_view(), name='me-update'),

]