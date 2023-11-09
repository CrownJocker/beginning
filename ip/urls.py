from django.urls import path
from ip.views import views

app_name = 'ip'
urlpatterns = [

    # IPAddress
    path("catalog-ip/", views.IPCatalogs.as_view(), name='catalog-ip'),
    path("create-ip/", views.CreateIPAddressView.as_view(), name='create-ip'),
    path("update-ip/<int:pk>", views.IPAddressUpdateView.as_view(), name='update-ip'),
    path("delete-ip/<int:pk>", views.IPAddressDeleteView.as_view(), name='delete-ip'),
    path("view-ip/<int:pk>", views.IPAddressDetailView.as_view(), name='detail-ip'),

    # LLIH9Ga
    path("add-ip/", views.FilterIPAddressesView.as_view(), name='filter1'),
    path("filter_res/", views.FilterIPAddressesView.as_view(), name='filter_results'),

]
