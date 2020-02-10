from rest_framework import serializers
from . models import CassavaModel

class cassavaSerializers(serializers.ModelSerializer):
	class Meta:
		model= CassavaModel
		fields='__all__'