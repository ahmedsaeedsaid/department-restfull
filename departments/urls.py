from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListCreateDepartmentAPIView.as_view(), name='get_post_departments'),
    path('<int:pk>/', views.RetrieveUpdateDestroyDepartmentAPIView.as_view(), name='get_delete_update_department'),
]