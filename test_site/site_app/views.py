from django.shortcuts import render
from django.http import HttpResponse
import os

# HOST = '0.0.0.0'
# PORT = 5000
SERVICE_NAME = os.environ.get('SERVICE_NAME', 'application')

def home_page(request):
    # return make_response(
    #     jsonify(
    #         {'message': f'Hello from {SERVICE_NAME}!'}
    #     ))
    return HttpResponse("wow you achieve this!")