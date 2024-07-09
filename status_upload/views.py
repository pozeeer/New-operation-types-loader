from datetime import date, datetime, timedelta
from typing import List, Dict, Set
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from dotenv import load_dotenv

import requests
import os

from .models import OperationTypeModel

load_dotenv()


class NewTypeOperation(APIView):
    def post(self, request) -> Response:
        date_to: date = datetime.now().date()
        date_from: date = self._get_date_from(date_to)
        data: List[Dict] = self._get_wb_data(date_from, date_to)
        new_types: Set[str] = self._process_new_types(data)
        return self._create_response(new_types)

    @staticmethod
    def _get_date_from(date_to) -> date:
        return date_to - timedelta(days=7)

    @staticmethod
    def _get_wb_data(date_from: date, date_to: date) -> List[dict]:
        params = {'dateFrom': date_from.strftime('%Y-%m-%d'), 'dateTo': date_to.strftime('%Y-%m-%d')}
        response = requests.get(
            'https://statistics-api.wildberries.ru/api/v5/supplier/reportDetailByPeriod',
            headers={'Authorization': os.getenv('WB_API_TOKEN')},
            params=params
        )
        return response.json()

    @staticmethod
    def _process_new_types(data: List[Dict]) -> Set[str]:
        old_data: Set[str] = OperationTypeModel.objects.values_list('name_of_type', flat=True).distinct()
        new_types: Set[str] = set()
        for item in data:
            supplier_oper_name = item['supplier_oper_name']
            if supplier_oper_name not in old_data:
                OperationTypeModel.objects.create(name_of_type=supplier_oper_name)
                new_types.add(supplier_oper_name)
        return new_types

    @staticmethod
    def _create_response(new_types: Set[str]) -> Response:
        if not new_types:
            return Response({'new_operation_type': 'новых типов операций не обнаружено'})
        else:
            return Response({'new_operation_type': list(new_types)})


class AllTypeOperation(APIView):
    def get(self, request) -> Response:
        all_types_operation: List[str] = OperationTypeModel.objects.values_list('name_of_type', flat=True).distinct()
        return Response({'all_operation_types': all_types_operation})
