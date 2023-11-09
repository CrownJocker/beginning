from django.urls import path
from . import views

app_name = 'testUser'
urlpatterns = [

    path("instr_filter_res/", views.FilterInstructionsView.as_view(), name='instruction_filter_results'),
    path("catalogs", views.Catalogs.as_view(), name='catalogs'),
    path("sidebar/", views.sdbar),
    # path('users/', views.CustomUserView.as_view(), name='users'),

    path("qube", views.QubeView.as_view(), name='qubick'),

    # Instructions
    path("instructions-view/", views.Instructions.as_view(), name='instructions'),
    path("instruction-update-sdv/<int:pk>", views.InstructionUpdateView.as_view(), name='instruction-update'),
    path("instruction-delete-sdv/<int:pk>", views.InstructionDeleteView.as_view(), name='instruction-delete'),
    path("instruction-detail-view-sdv/<int:pk>", views.InstructionDetailView.as_view(), name='instruction-view'),
    path("instruction-add-sdv/", views.InstructionCreateView.as_view(), name='instruction-add'),

]
