from django.urls import path
from .views import SignUpView, LoginView, TaskCreateView, TaskListView, TaskTrashView, TrashedListView, DeleteTaskPermanentlyView, RestoreTaskView, CompletedTaskView, CompletedTaskListView, ImportantTaskView, ImportantTaskListView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    path('home/', TaskListView.as_view(), name='home'),
    path('add-task/', TaskCreateView.as_view(), name='add-task'),
    path('trash-task/<int:pk>/', TaskTrashView.as_view(), name='trash-task'),
    path('trashed-task-list/', TrashedListView.as_view(), name='trashed-task-list'),
    path('delete-task/<int:pk>/', DeleteTaskPermanentlyView.as_view(), name='delete-task'),
    path('restore-task/<int:pk>/', RestoreTaskView.as_view(), name='restore-task'),
    path('complete-task/<int:pk>/', CompletedTaskView.as_view(), name='complete-task'),
    path('completed-task-list/', CompletedTaskListView.as_view(), name='completed-task-list'),
    path('important-task/<int:pk>/', ImportantTaskView.as_view(), name='important-task'),
    path('important-task-list/', ImportantTaskListView.as_view(), name='important-task-list'),
]
