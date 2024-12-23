from django.urls import path

from task_manager.views import TaskListView, TaskCreateView, logout_user, RegisterView, TaskUpdateView, LoginUserView, \
    TaskDeleteView

urlpatterns = [
    path('', TaskListView.as_view(), name='index'),
    path('create-task/', TaskCreateView.as_view(), name='create-task'),
    path('update-task/<int:pk>/', TaskUpdateView.as_view(), name='update-task'),
    path('delete-task/<int:pk>/', TaskDeleteView.as_view(), name='delete-task'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]
