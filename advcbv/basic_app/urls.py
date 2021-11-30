from django.urls import path
from basic_app import views


app_name = 'basic_app'

urlpatterns = [

    path('',views.SchoolListView.as_view(),name='list'),
    path('students/',views.StudentListView.as_view(),name='slist'),
    path('<int:pk>/',views.SchoolDetailView.as_view(),name='detail'),
    path('students/<int:pk>/',views.StudentDetailView.as_view(),name='sdetail'),
    path('create/', views.SchoolCreateView.as_view(),name='create'),
    path('screate/', views.StudentCreateView.as_view(),name='screate'),
    path('update/<int:pk>/', views.SchoolUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.SchoolDeleteView.as_view(), name='delete'),
    path('students/update/<int:pk>/', views.StudentUpdateView.as_view(), name='supdate'),
    path('students/delete/<int:pk>/', views.StudentDeleteView.as_view(), name='sdelete'),

]
