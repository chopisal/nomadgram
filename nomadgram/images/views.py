from rest_framework.views import APIView
from rest_framework.response import Response


class ListAllImages(APIView):

    def get(self, request, format=None):
