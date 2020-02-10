from rest_framework import serializers
from . models import DogCatModel

class dogcatSerializers(serializers.ModelSerializer):
	class Meta:
		model=DogCatModel
		fields='__all__'