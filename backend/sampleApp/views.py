from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class Test(APIView):
    """Test  View"""
    permission_classes = (AllowAny,)

    def get(self, request):
        content = "hello"

        return Response(content)
