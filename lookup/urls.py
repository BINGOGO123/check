from django.urls import path
from .views import print_all

app_name="backend"

urlpatterns = [
    path("print_all/", print_all, name="print_all")
]