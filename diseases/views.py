from django.shortcuts import render
from rest_framework.views import APIView 
from .models import Disease, Pill, Effect, Conflict
from .serializers import DiseaseListSerializer, DiseaseDetailSerializer, PillListSerializer, PillDetailSerializer, EffectListSerializer, ConflictDetailSerializer
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


class EffectListView(APIView):
	"""Вывод препаратов и их еффективности"""
	def get(self, request, pk):
		effects = Effect.objects.filter(disease_id=pk)
		serializer = EffectListSerializer(effects, many=True)
		return Response(serializer.data)


class ConflicDetailView(APIView):
	"""Вывод противопоказаний препарата"""
	def get(self, request, pk):
		conflict = Conflict.objects.get(id=pk)
		serializer = ConflictDetailSerializer(conflict)
		return Response(serializer.data)
