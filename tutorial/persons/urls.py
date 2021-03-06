from django.urls import path
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from persons import views

urlpatterns = format_suffix_patterns([
    path('persons/', views.PersonList.as_view()),
    path('persons/<int:pk>/', views.PersonDetail.as_view()),
])

