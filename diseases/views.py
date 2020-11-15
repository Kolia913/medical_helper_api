from django.shortcuts import render
from rest_framework.views import APIView 
from .models import Disease, Pill
from .serializers import DiseaseListSerializer, DiseaseDetailSerializer, PillListSerializer, PillDetailSerializer
from rest_framework.response import Response


# Create your views here.
class DiseaseListView(APIView):
	"""Вывод списка заболеваний"""
	def get(self, request):
		diseases = Disease.objects.all()
		serializer = DiseaseListSerializer(diseases, many=True)
		return Response(serializer.data)


class DiseaseDetailView(APIView):
	"""Вывод информации о заболевании"""
	def get(self, request, slug):
		disease = Disease.objects.get(slug=slug)
		serializer = DiseaseDetailSerializer(disease)
		return Response(serializer.data)


class PillListView(APIView):
	"""Вывод списка препаратов"""
	def get(self, request):
		pills = Pill.objects.all()
		serializer = PillListSerializer(pills, many=True)
		return Response(serializer.data)


class PillDetailView(APIView):
	"""Вывод информации о препарате"""
	def get(self, request, slug):
		pill = Pill.objects.get(slug=slug)
		serializer = PillDetailSerializer(pill)
		return Response(serializer.data)