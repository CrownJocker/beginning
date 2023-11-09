from django.urls import path
from .views import views

app_name = 'organisation'
urlpatterns = [
    # Filial
    path('filial/', views.Filials.as_view(), name='filials'),
    path("filial-update-sdv/<int:pk>", views.FilialUpdateView.as_view(), name='filial-update-sdv'),
    path("filial-delete-sdv/<int:pk>", views.FilialDeleteView.as_view(), name='filial-delete-sdv'),
    path("filial-view-sdv/<int:pk>", views.FilialDetailView.as_view(), name='filial-view-sdv'),
    path("fil-add-sdv/", views.FilialCreateView.as_view(), name='fil-add-sdv'),

    # Department
    path('department/', views.Departments.as_view(), name='departments'),
    path("dept-update-sdv/<int:pk>", views.DeptUpdateView.as_view(), name='dept-update-sdv'),
    path("dept-add-sdv/", views.DeptCreateView.as_view(), name='dept-add-sdv'),
    path("dept-delete-sdv/<int:pk>", views.DeptDeleteView.as_view(), name='dept-delete-sdv'),
    path("dept-view-sdv/<int:pk>", views.DeptDetailView.as_view(), name='dept-view-sdv'),

    # SubDepartment
    path('subDepartment/', views.SubDepartments.as_view(), name='subDepartments'),
    path("subDept-update-sdv/<int:pk>", views.SubDeptUpdateView.as_view(), name='subDept-update-sdv'),
    path("subDept-add-sdv/", views.SubDeptCreateView.as_view(), name='subDept-add-sdv'),
    path("subDept-delete-sdv/<int:pk>", views.SubDeptDeleteView.as_view(), name='subDept-delete-sdv'),
    path("subDept-view-sdv/<int:pk>", views.SubDeptDetailView.as_view(), name='subDept-view-sdv'),

]