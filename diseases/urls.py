from django.urls import path 
from . import views

urlpatterns = [
	path('disease/', views.DiseaseListView.as_view()),
	path("disease/<slug:slug>/", views.DiseaseDetailView.as_view()),
	path("pill/", views.PillListView.as_view()),
	path("pill/<slug:slug>/", views.PillDetailView.as_view())
]