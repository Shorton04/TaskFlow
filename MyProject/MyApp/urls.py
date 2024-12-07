from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("dashboard/", views.dashboard_view, name="dashboard"),  # Corrected reference
    path("logout/", views.logout_view, name="logout"),
    path('dashboard/profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile_view, name='profile_edit'),  # Add this URL pattern for editing profile
    path('profile/change-password/', views.change_password_view, name='change_password'),
    path('profile/delete-account/', views.delete_account_view, name='delete_account'),
    path('project/<int:project_id>/members/', views.project_members, name='project_members'),
    path('project/<int:project_id>/members/<int:member_id>/update-role/', views.update_member_role, name='update_member_role'),
    path('project/<int:project_id>/members/<int:member_id>/remove/', views.remove_member, name='remove_member'),
    path('dashboard/project/', views.project_list, name='project_list'),
    path('create/', views.project_create, name='project_create'),
    path('<int:pk>/update/', views.project_update, name='project_update'),
    path('<int:pk>/delete/', views.project_delete, name='project_delete'),
    path('dashboard/tasks/', views.task_list, name='task_list'),
    path('tasks/create/', views.task_create, name='task_create'),
    path('tasks/<int:pk>/update/', views.task_update, name='task_update'),
    path('tasks/<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('dashboard/leader-reports/', views.leader_reports, name='leader-reports'),
    path('dashboard/member-reports/', views.member_reports, name='member-reports'),
    path('member-reports/generate-summary-report/<int:project_id>/', views.generate_project_summary_report, name='generate_project_summary_report'),
    path('generate-csv-report/', views.generate_csv_report, name='generate_csv_report'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)