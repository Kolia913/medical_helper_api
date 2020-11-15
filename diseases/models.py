from django.db import models

class Type(models.Model):
	"""Типы заболеваний"""
	name = models.CharField("Тип", max_length=255)
	desc = models.TextField("Описание", max_length=2000)

	def __str__(self):
		return self.name

		
	class Meta:
		verbose_name = "Тип"
		verbose_name_plural = "Типы"


class Conflict(models.Model):
	"""Противопоказания"""
	name = models.CharField("Название", max_length=150)
	image_url = models.ImageField("Изображение", upload_to="conflicts/")
	desc = models.TextField("Описание")

	def __str__(self):
		return self.name


	class Meta:
		verbose_name="Противопоказание"
		verbose_name_plural="Противопоказания"


class Pill(models.Model):
	"""Лекарства"""
	name = models.CharField("Название", max_length=200)
	image = models.ImageField("Изображение", upload_to="pills/")
	conflicts = models.ManyToManyField(Conflict, verbose_name="Противопоказания", related_name="pill_conflict", null=True)
	desc = models.TextField("Описание")
	slug = models.SlugField(max_length=255, unique=True)

	def __str__(self):
		return self.name

	
	class Meta:
		verbose_name = "Лекарство"
		verbose_name_plural = "Лекарства"


class Disease(models.Model):
	"""Заболевания"""
	name = models.CharField("Название", max_length=255)
	image = models.ImageField("Изображение", upload_to="diseases/")
	symptoms = models.TextField("Симптомы", max_length=3000)
	desc = models.TextField("Описание")
	types = models.ManyToManyField(Type, verbose_name="Тип", related_name="disease_type")
	slug = models.SlugField(max_length=255, unique=True)

	def __str__(self):
		return self.name

	
	class Meta:
		verbose_name="Заболевание"
		verbose_name_plural="Заболевания"


class Effect(models.Model):
	"""Эффективность"""
	pill = models.ForeignKey(Pill, verbose_name="Лекарство", on_delete=models.CASCADE)
	disease = models.ForeignKey(Disease, verbose_name="Заболевание", on_delete=models.CASCADE)
	effectivity = models.FloatField("Еффективность", default=0, help_text="0-100, указывать в процентах(%)")

	def __str__(self):
		return "Ефективность"

	
	class Meta:
		verbose_name="Эффективность"
		verbose_name_plural="Эффективность"