from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.conf import settings
from django.conf.urls.static import static
from home import views as home_views
from rest_framework import routers

from testUser.apis import *
from organisation.views.api import *
from ip.views.api import *

schema_view = get_schema_view(
    openapi.Info(
        title='API-шники',
        default_version='v1',
        description='Описание API',
    ),
    public=True,
)

router = routers.DefaultRouter()

urlpatterns = [
    # Documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),

    # Apps
    path('admin/', admin.site.urls),
    path('testUser/', include('testUser.urls', namespace='testUser')),
    path('staff/', include('staff.urls', namespace='staff')),
    path('users/', include('users.urls', namespace='users')),
    path('organisation/', include('organisation.urls', namespace='organisation')),
    path('ip/', include('ip.urls', namespace='ip')),
    path('', home_views.HomePage.as_view(), name="home-page"),

    #
    path('', include(router.urls)),


    # Users
    path('api/usersDetail/', UserDetail.as_view()),
    path('api/users-list-view/', UserListView.as_view()),

    # Positions
    path('api/positions-detail/<int:pk>', PositionsUpdateViewApi.as_view()),
    path('api/positions-list-view/', PositionsListApi.as_view()),

    # TypeSubject
    path('api/TypeSubject-view/<int:pk>', TypeSubjectViewApi.as_view()),
    path('api/TypeSubject-list', TypeSubjectListApi.as_view()),

    # IPAddress
    path('api/update-ip-address/<int:pk>', IPAddressUpdateView.as_view()),
    path('api/create-ip-address', IPAddressListCreateView.as_view()),

    # Filial
    path('api/list-filial/', FilialListCreateView.as_view()),
    path('api/update-filial/<int:pk>', FilialUpdateView.as_view()),

    # Department
    path('api/list-department/', DepartmentListCreateView.as_view()),
    path('api/update-department/<int:pk>', DepartmentUpdateView.as_view()),

    # SubDepartment
    path('api/list-subDept/', SubDepartmentListCreateView.as_view()),
    path('api/update-subDept/<int:pk>', SubDepartmentUpdateView.as_view()),

    # Group
    path('api/list-group/', GroupListCreateView.as_view()),
    path('api/update-group/<int:pk>', GroupUpdateView.as_view()),

    # Instruction
    path('api/list-instruction/', InstructionsListApi.as_view()),
    path('api/update-instruction/<int:pk>', InstructionsUpdateViewApi.as_view()),

    # Steps
    path('api/list-steps/', StepsListApi.as_view()),
    path('api/update-steps/<int:pk>', StepsUpdateViewApi.as_view()),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

