from .views import project_detail_view, project_list_view
from django.urls import path

urlpatterns = [
    path('', project_list_view, name='project_list'),
    path('<int:pk>', project_detail_view, name='project_detail')
]
