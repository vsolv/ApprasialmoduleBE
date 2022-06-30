import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated

from employeeservice.data.request.appraisaldetailrequest import AppraisalDetailRequest
from employeeservice.data.request.appraisalqueuerequest import AppraisalQueueRequest
from employeeservice.data.request.appraisalrequest import AppraisalRequest
from employeeservice.models import Employee, Appraisal
from employeeservice.service.appraisaldetailservice import AppraisalDetailService
from employeeservice.service.appraisalqueueservice import AppraisalQueueService
from employeeservice.service.appraisalservice import AppraisalService
from employeeservice.service.employeeservice import EmployeeService
from employeeservice.util.emputil import appraisal_type_composite
from emputilityservice.service.authentication import EmployeeAuthentication
from emputilityservice.service.permission import EmployeePermission
from utilityservice.data.response.emppage import WisefinPage
from utilityservice.data.response.empmessage import WisefinMsg, SuccessMessage, ErrorMessage, Success, SuccessStatus, Error, ErrorDescription


@csrf_exempt
@api_view(['POST', 'GET'])
@authentication_classes([EmployeeAuthentication])
@permission_classes([IsAuthenticated, EmployeePermission])
def appraisal_create(request):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        request_fn = AppraisalRequest(data_json)
        user_id = request.user.id
        print(user_id)
        appraisal_details = AppraisalDetailService()
        appraisal_id = AppraisalService().appraisal_create(request_fn)
        #appraisal_details
        details = data_json.get('details')
        print('details_id', details)
        try:
            for x in details:
                details_obj = AppraisalDetailRequest(x)
                if appraisal_id!=None:
                    details_resp = appraisal_details.appraisal_detail_create(details_obj, appraisal_id)

            resp = WisefinMsg()
            resp.set_message(SuccessMessage.CREATE_MESSAGE)
            response = HttpResponse(resp.get(), content_type='application/json')
            return response
        except:
            resp = WisefinMsg()
            resp.set_message(ErrorMessage.INVALID_DATA)
            response = HttpResponse(resp.get(), content_type='application/json')
            return response


    elif request.method == 'GET':
        page = request.GET.get('page', 1)
        page = int(page)
        vys_page = WisefinPage(page, 10)
        req_obj = AppraisalService().fetch_appraisal(vys_page, request)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response


@csrf_exempt
@api_view(['GET', 'DELETE'])
@authentication_classes([EmployeeAuthentication])
@permission_classes([IsAuthenticated, EmployeePermission])
def get_appraisal(request, id):
    if request.method == 'GET':
        req_obj = AppraisalService().get_appraisal(id)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response

    elif request.method == 'DELETE':
        req_obj = AppraisalService().del_appraisal(id)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response


#APPRAISAL_DROP_DOWN
@csrf_exempt
@api_view(['GET'])
@authentication_classes([EmployeeAuthentication])
@permission_classes([IsAuthenticated, EmployeePermission])
def appraisal_drop_down(request):
    if request.method == 'GET':
        val = appraisal_type_composite()
        response = HttpResponse(val.get(), content_type='application/json')
        return response


#APPRAISAL_DETAIL_CREATE
@csrf_exempt
@api_view(['POST', 'GET'])
@authentication_classes([EmployeeAuthentication])
@permission_classes([IsAuthenticated, EmployeePermission])
def appraisal_detail_create(request):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        request_fn = AppraisalDetailRequest(data_json)
        req_obj = AppraisalDetailService().appraisal_detail_create(request_fn)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response

    elif request.method == 'GET':
        page = request.GET.get('page', 1)
        page = int(page)
        vys_page = WisefinPage(page, 10)
        req_obj = AppraisalDetailService().fetch_appraisal_detail(vys_page)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response

@csrf_exempt
@api_view(['GET', 'DELETE'])
@authentication_classes([EmployeeAuthentication])
@permission_classes([IsAuthenticated, EmployeePermission])
def get_appraisal_details(request, id):
    if request.method == 'GET':
        req_obj = AppraisalDetailService().get_appraisal_detail(id)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response

    elif request.method == 'DELETE':
        req_obj = AppraisalDetailService().del_appraisal_detail(id)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response


#APPRAISAL_QUEUE
@csrf_exempt
@api_view(['POST', 'GET'])
@authentication_classes([EmployeeAuthentication])
@permission_classes([IsAuthenticated, EmployeePermission])
def appraisal_queue_create(request):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        request_fn = AppraisalQueueRequest(data_json)
        req_obj = AppraisalQueueService().appraisal_queue_create(request_fn)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response

    elif request.method == 'GET':
        page = request.GET.get('page', 1)
        page = int(page)
        vys_page = WisefinPage(page, 10)
        req_obj = AppraisalQueueService().fetch_appraisal_queue(vys_page)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response


@csrf_exempt
@api_view(['GET'])
@authentication_classes([EmployeeAuthentication])
@permission_classes([IsAuthenticated, EmployeePermission])
def appraisal_get(request, appraisal_id):
    if request.method == 'GET':
        appr_serv = AppraisalService()
        appr_detail_serv = AppraisalDetailService()
        appraisal_list = Appraisal.objects.filter(id=appraisal_id)

        if len(appraisal_list) > 0:
            appraisal = appr_serv.get_appraisal(appraisal_list[0].id)
            appraisal_detail = appr_detail_serv.get_appraisal_details(appraisal_id)
            appraisal.details = appraisal_detail
            response = HttpResponse(appraisal.get(), content_type='application/json')
            return response

        else:
            resp = Error()
            resp.set_description(ErrorMessage.INVALID_DATA)
            resp.set_code('400')
            response = HttpResponse(resp.get(), content_type='application/json')
            return response


#EMPLOYEE_DROP_DOWN
@csrf_exempt
@api_view(['GET'])
@authentication_classes([EmployeeAuthentication])
@permission_classes([IsAuthenticated, EmployeePermission])
def employee_drop_down(request):
    if request.method == 'GET':
        page = request.GET.get('page', 1)
        page = int(page)
        vys_page = WisefinPage(page, 10)
        emp_serv = EmployeeService()
        req_obj = emp_serv.employee_drop_down(vys_page,request)
        response = HttpResponse(req_obj.get(), content_type='application/json')
        return response


