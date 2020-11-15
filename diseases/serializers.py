from rest_framework import serializers

from .models import Disease, Pill


class DiseaseListSerializer(serializers.ModelSerializer):
	"""Список заболеваний"""
	class Meta:
		model = Disease
		fields = ("name", "image", "types")


class DiseaseDetailSerializer(serializers.ModelSerializer):
	"""Информация о заболевании"""
	types = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)

	class Meta:
		model = Disease
		fields = '__all__'


class PillListSerializer(serializers.ModelSerializer):
	"""Список препаратов"""
	class Meta:
		model = Pill
		fields =  ("name", "image", "desc")


class PillDetailSerializer(serializers.ModelSerializer):
	"""Информация о препарате"""
	# conflicts = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)

	class Meta:
		model = Pill
		fields = "__all__"