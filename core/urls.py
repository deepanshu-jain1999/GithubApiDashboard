from django.urls import path
from . import views

urlpatterns = [
    path('search-user/', views.SearchUser.as_view()),
]

