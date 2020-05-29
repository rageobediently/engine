from django.shortcuts import render
from display.models import Data
from rest_framework.response import Response
from rest_framework.views import APIView

from display.serializers import DataSerializer


def index(request):
    allvariables = Data.objects.order_by('-id')[0:10]
    return render(request, "display/out.html",{"all":allvariables})
def index2(request):
    allvariables = Data.objects.order_by('-id')[0:10]
    return render(request, "display/outtable.html",{"all":allvariables})

class DataView(APIView):
    def get(self, request):
        articles = Data.objects.all()
        serializer = DataSerializer(articles, many=True)
        return Response({"datas": serializer.data})
    def post(self, request):
        data = request.data.get('data')
        # Create an article from the above data
        serializer = DataSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            data_saved = serializer.save()
        return Response({"success": "Article '{}' created successfully".format(data_saved.dateandtime)})