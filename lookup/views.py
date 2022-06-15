from django.http import HttpRequest, JsonResponse
from django.shortcuts import render

# Create your views here.

def print_all(request: HttpRequest):
    ret = {
        "method": request.method,
        "params": str(request),
        "body": str(request.body)
    }
    return JsonResponse(
        ret
    )