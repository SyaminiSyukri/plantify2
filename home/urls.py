from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('', views.index, name='index'),
    path('<id>/<str:slug>/', views.detail_view, name='details'),
    path('search/', views.search, name='search'),

    path('notes/', views.notesPage, name='notes'),


    path("plant/<int:image_id>/edit/", views.edit_plant, name="edit_plant"),
    


    path('users/', views.user_list, name='user_list'),  # List all users
    path('users/<int:user_id>/edit/', views.edit_user, name='edit_user'),  # Edit user
    path('users/<int:user_id>/delete/', views.delete_user, name='delete_user'),  #deleting user

    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.profile_update, name='profile_update'),





]