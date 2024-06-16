from django.urls import path, include
from . import views

app_name = "contact_app"

urlpatterns = [
	path("contact_api/add/", views.addFormData),
	path("contact_api/get/", views.getFormData)
]