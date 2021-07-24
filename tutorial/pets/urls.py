from django.urls import path
from pets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path('pets/', views.pets_list),
    path('pets/<int:pk>/', views.pets_detail),
])

