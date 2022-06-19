from django.shortcuts import render
from display.models import Metric
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.gererics import ListAPIView, CreateAPIView
from rest_framework.authentication import SessionAuthentication

from display.serializers import MetricSerializer


def index(request):
    allvariables = Metric.objects.order_by('-id')[:10]
    return render(request, "display/out.html", {"all": allvariables})


def index2(request):
    allvariables = Metric.objects.order_by('-id')[:10]
    return render(request, "display/outtable.html", {"all": allvariables})


# class DataView(APIView):
#     def get(self, request):
#         articles = Data.objects.all()
#         serializer = DataSerializer(articles, many=True)
#         return Response({"datas": serializer.data})
#
#     def post(self, request):
#         data = request.data.get('data')
#         serializer = DataSerializer(data=data)
#         if serializer.is_valid(raise_exception=True):
#             data_saved = serializer.save()
#         return Response({"success": "Article '{}' created successfully".format(data_saved.dateandtime)})


class MetricListAPI(ListAPIView):
    serializer_class = MetricSerializer
    authentication_classes = [SessionAuthentication]

    def get_queryset(self):
        return Metric.objects.all()


class MetricCreateAPI(CreateAPIView):
    serializer_class = MetricSerializer
    authentication_classes = [SessionAuthentication]

    def get_queryset(self):
        return Metric.objects.all()