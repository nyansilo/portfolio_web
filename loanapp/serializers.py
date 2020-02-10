from rest_framework import serializers
from . models import Approvals


"""
class approvalsSerializers(serializers.ModelSerializer):
	class Meta:
		model=Approvals
		fields='__all__'
"""

class ApprovalSerializer(serializers.ModelSerializer):
	class Meta:
		model=Approvals
		fields='__all__'

class HelloSerializer(serializers.Serializer):
	"""docstring for HelloSerializer"""
	firstname = serializers.CharField(max_length=10)
	lastname = serializers.CharField(max_length=10)
		
