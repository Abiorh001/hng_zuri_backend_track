from django.urls import path
from .views import RetrieveApiEndpoint


urlpatterns = [
    path("", RetrieveApiEndpoint.as_view(), name="zuri-endpoint")
]