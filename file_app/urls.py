from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
     path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('', views.index, name='index'),

    path('department-list', views.department_list, name='department_list'),
    path('department/<int:id>/update', views.update_department, name='update_department'),
    path('department/<int:id>/delete', views.delete_department, name='delete_department'),

    path('faculty-list', views.faculty_list, name='faculty_list'),
    path('faculty/<int:id>/update', views.update_faculty, name='update_faculty'),
    path('faculty/<int:id>/delete', views.delete_faculty, name='delete_faculty'),

    path('staff-list', views.staff_list, name='staff_list'),
    path('staff/<int:id>/update', views.update_staff, name='update_staff'),
    path('staff/<int:id>/delete', views.delete_staff, name='delete_staff'),

    path('faculty/archives-list', views.faculty_archives_list, name='faculty_archives_list'),
    path('staff/archives-list', views.staff_archives_list, name='staff_archives_list'),

    path('add/staff-documents', views.add_staff_document, name='add_staff_documents'),
    path('add/faculty-documents', views.add_faculty_document, name='add_faculty_documents'),


]
