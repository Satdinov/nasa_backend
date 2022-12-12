import json
import requests

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import views
from rest_framework.response import Response

from nasa.apps.serializers import GetInfoSerializer
from nasa.apps.services import save_info_to_db, get_info_from_api

filter_query_params = [
    openapi.Parameter('name', openapi.IN_QUERY, type=openapi.TYPE_STRING,
                      description='Название спутника (FALCONSAT / AISSAT / PROXIMA)'),
]

class GetInfoView(views.APIView):
    authentication_classes = []
    permission_classes = []

    @swagger_auto_schema(
        operation_description="Эндпоинт для получения информации по спутнику.",
        manual_parameters = filter_query_params,
    )
    def post(self, *args, **kwargs):
        name = self.request.query_params.get('name')
        d = get_info_from_api(name)
        return Response(d)

class SaveToDBView(views.APIView):
    authentication_classes = []
    permission_classes = []

    @swagger_auto_schema(
        operation_description="Эндпоинт для получения информации в БД.",
        manual_parameters=filter_query_params,
    )
    def post(self, *args, **kwargs):
        name = self.request.query_params.get('name')
        info = get_info_from_api(name)
        save_info_to_db(info)
        return Response(info)