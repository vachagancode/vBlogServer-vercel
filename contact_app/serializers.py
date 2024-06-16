from rest_framework.serializers import ModelSerializer
from .models import ContactFormData

class ContactDataSerializer(ModelSerializer):
	class Meta:
		model = ContactFormData
		fields = "__all__"