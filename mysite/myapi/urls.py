from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.plan_list, name='plan_list'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('add', views.ADD, name='add'),
    path('edit', views.EDIT, name='edit'),
    path('update/<str:id>', views.UPDATE, name='update'),
    path('delete/<str:id>', views.DELETE, name='delete'),
    # Add more URLs as needed
]