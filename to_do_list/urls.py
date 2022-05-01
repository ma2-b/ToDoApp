from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView


app_name = 'to_do_list'


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='to_do_list:login'), name='logout'),
    path('register/', RegisterPage.as_view(),name='register'),
    
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('create-task/', TaskCreate.as_view(), name='task-create'),
    path('task-updata/<int:pk>/', TaskUpdate.as_view(), name='task-updata'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),

]