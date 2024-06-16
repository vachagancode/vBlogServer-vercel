from rest_framework.response import Response
from rest_framework.decorators import api_view 

from .serializers import ContactDataSerializer
from .models import ContactFormData

# bot
from .bot import send_data
import asyncio

loop = asyncio.get_event_loop()

@api_view(['POST'])
def addFormData(request):
	serializer = ContactDataSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		name = str(serializer.data["name"])
		email = str(serializer.data["email"])
		message = str(serializer.data["message"])
		formatted_data = f"Name: {name}\nEmail: {email}\nMessage: {message}"
		print(formatted_data)
		loop.run_until_complete(send_data(formatted_data))
	return Response(serializer.data)

@api_view(['GET'])
def getFormData(request):
	form_model_data = ContactFormData.objects.all()
	serializer = ContactDataSerializer(data=form_model_data, many=True)
	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)