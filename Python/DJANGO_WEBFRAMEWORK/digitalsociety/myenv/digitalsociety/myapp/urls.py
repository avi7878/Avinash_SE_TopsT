"""
URL configuration for digitalsociety project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('change-password/',views.change_password,name='change-password'),
    path('update-chairman-profile/',views.update_chairman_profile,name='update-chairman-profile'),
    path('add-notice/',views.add_notice,name='add-notice'),
    path('view-notice/',views.view_notice,name='view-notice'),
    path('edit-notice/<int:pk>/',views.edit_notice,name="edit-notice"),
    path('delete-notice/<int:pk>',views.delete_notice,name="delete-notice"),
    path('forgot-password/',views.forgot_password,name='forgot-password'),
    path('change-password-value/',views.change_password_value,name='change-password-value'),
    path('register/',views.register,name='register'),
    path('add-member/',views.add_member,name='add-member'),
    path('all-member/',views.all_member,name='all-member'),
    path('societyspecification-profile/<int:pk>',views.societyspecification_profile,name="societyspecification-profile"),
    path('member-profile/',views.member_profile,name='member-profile'),
    path('update-member-profile/',views.update_member_profile,name='update-member-profile'),
    path('add-event/',views.add_event,name='add-event'),
    path('view-event/',views.view_event,name='view-event'),
    path('add-complaints/',views.add_complaints,name='add-complaints'),
    path('view-complaints/',views.view_complaints,name='view-complaints'),
    path('add-maintainance/',views.add_maintainance,name='add-maintainance'),
    path('all-maintainance/',views.all_maintainance,name='all-maintainance'),
]
