from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@api_view(['GET', 'POST'])
def hello(request):
  if request.method == 'GET':
    return Response('Hello')
  elif request.method == 'POST':
    return Response({'data': 'Hello'})