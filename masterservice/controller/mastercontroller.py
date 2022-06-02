import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from masterservice.data.request.departementrequest import DepartmentRequest
from masterservice.service.departementservice import DepartmentService
from utilityservice.data.response.emppage import WisefinPage


@csrf_exempt
@api_view(['POST', 'GET'])
def create_department(request):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        request_fn = DepartmentRequest()
        dep_id = request_fn.fetch_id(data_json)
        req_dict = request_fn.fetch_request(data_json)
        req_obj = DepartmentService().create_department(req_dict, dep_id)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response

    elif request.method == 'GET':
        page = request.GET.get('page', 1)
        page = int(page)
        vys_page = WisefinPage(page, 10)
        req_obj = DepartmentService().fetch_department(vys_page)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response

@csrf_exempt
@api_view(['GET','DELETE'])
def get_department(request, id):
    if request.method == 'GET':
        req_obj = DepartmentService().get_department(id)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response

    elif request.method == 'DELETE':
        req_obj = DepartmentService().del_department(id)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response


