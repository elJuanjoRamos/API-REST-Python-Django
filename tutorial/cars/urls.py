from django.urls import path
from cars import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path('cars/', views.CarList.as_view()),
    path('cars/<int:pk>/', views.CarDetail.as_view()),
])


