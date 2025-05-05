
from django.contrib import admin
from django.urls import include, path
from gui import views as gui_views
# urls
urlpatterns = [
    path('api/v1/departments/', include('departments.urls')),
    path('api/v1/auth/', include('authentication.urls')),
    path('admin/', admin.site.urls),

    path('register/', gui_views.register_view, name='register'),
    path('login/', gui_views.login_view, name='login'),
    path('logout/', gui_views.logout_view, name='logout'),

    path('', gui_views.department_list, name='department_list'),
    path('create/', gui_views.department_create, name='department_create'),
    path('update/<int:pk>/', gui_views.department_update, name='department_update'),
    path('delete/<int:pk>/', gui_views.department_delete, name='department_delete'),
]