from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('leave/', views.leave, name='leave'),
    path('update/', views.update, name='update'),
    path('change_password/', views.change_password, name='change_password'),

    path("users/", views.users, name="users"),
    path("profile/<str:username>/", views.profile, name="profile"),
    path("<int:user_id>/follow/", views.follow, name="follow"),
]
