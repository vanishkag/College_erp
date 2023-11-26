from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),

    path('fac_login', views.fac_login, name="fac_login"),
    path('fac_forpass', views.fac_forpass, name="fac_forpass"),

    path('slogin', views.slogin, name="slogin"),
    path('stu_forpass', views.stu_forpass, name="stu_forpass"),

    path('admin_login', views.admin_login, name="admin_login"),
    path('admin_forpass', views.admin_forpass, name="admin_forpass"),

    path('welcome', views.welcome, name="welcome"),

    path('error', views.error, name="error"),

    path('stu_sis', views.stu_sis, name="stu_sis"),

    path('fac_sis', views.fac_sis, name="fac_sis"),

    path('admin_sis', views.admin_sis, name="admin_sis"),

    path('timetable/add', views.timetable_add, name='timetable_add'),
    path('timetable/update/', views.timetable_update, name='timetable_update'),
    path('timetable/delete/', views.timetable_delete, name='timetable_delete'),
    path('timetable/search/', views.timetable_search, name='timetable_search'),

    path('attendance/add', views.attendance_add, name='attendance_add'),
    path('attendance/update/', views.attendance_update, name='attendance_update'),
    path('attendance/delete/', views.attendance_delete, name='attendance_delete'),
    path('attendance/search/', views.attendance_search, name='attendance_search'),

    path('achievement/add', views.achievement_add, name='achievement_add'),
    path('achievement/update/', views.achievement_update, name='achievement_update'),
    path('achievement/delete/', views.achievement_delete, name='achievement_delete'),
    path('achievement/search/', views.achievement_search, name='achievement_search'),

    path('sis/add', views.sis_add, name='sis_add'),
    path('sis/update/', views.sis_update, name='sis_update'),
    path('sis/delete/', views.sis_delete, name='sis_delete'),
    path('sis/search/', views.sis_search, name='sis_search'),

    path('attendance', views.attendance, name='attendance'),
]