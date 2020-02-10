from rest_framework import serializers
from projectapp.models import Project
from cassavaapp.models import CassavaModel
from loanapp.models import Approvals
from dogcatapp.models import DogCatModel


""" PROJECT LIST SERIALIZER """
class ProjectListlSerializer(serializers.ModelSerializer):
	class Meta:
		model=Project
		fields='__all__'

""" PROJECT LIST SERIALIZER """
class CassavaSerializer(serializers.ModelSerializer):
	class Meta:
		model= CassavaModel
		fields='__all__'


""" APPROVALS SERIALIZER """
class ApprovalSerializer(serializers.ModelSerializer):
	class Meta:
		model=Approvals
		fields='__all__'


""" DOGCAT SERIALIZER """
class DogCatSerializer(serializers.ModelSerializer):
	class Meta:
		model=DogCatModel
		fields='__all__'
