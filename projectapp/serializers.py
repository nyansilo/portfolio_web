from rest_framework import serializers
from . models import Project


"""
class approvalsSerializers(serializers.ModelSerializer):
	class Meta:
		model=Approvals
		fields='__all__'
"""

class ProjectListlSerializer(serializers.ModelSerializer):
	class Meta:
		model=Project
		fields='__all__'


