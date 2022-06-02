from employeeservice.data.response.employeeaddressresponse import EmployeeAddressResponse
from employeeservice.models.employeemodels import EmployeeAddress
from django.db.models import Q
from utilityservice.data.response.empmessage import WisefinMsg, SuccessMessage, ErrorMessage, Success, SuccessStatus, Error, ErrorDescription
from utilityservice.data.response.emplist import WisefinList
from employeeservice.util.emputil import ActiveStatus
from utilityservice.data.response.emppaginator import WisefinPaginator


class EmployeeAddressService:
    def create_emp_address(self, data_obj, emp_add_id):
        resp = WisefinMsg()
        create_arr = data_obj['create_arr']
        update_arr = data_obj['update_arr']
        if len(update_arr)> 0:
            for val in update_arr:
        # if emp_add_id is not None:
                EmployeeAddress.objects.filter(id=val['id']).update(**val)
                obj = EmployeeAddress.objects.get(id=emp_add_id)

        else:
            if len(create_arr)> 0:
                elist = [EmployeeAddress(**val) for val in create_arr]
                obj = EmployeeAddress.objects.bulk_create(elist)
            resp.set_message(SuccessMessage.CREATE_MESSAGE)

        return resp

    def fetch_employee_addr(self, employee_id):
        emp_obj = EmployeeAddress.objects.filter(status=ActiveStatus.Active, employee_id=employee_id)
        list_data = WisefinList()
        for obj in emp_obj:
            data_resp = EmployeeAddressResponse()
            data_resp.set_line1(obj.line1)
            data_resp.set_line2(obj.line2)
            data_resp.set_line3(obj.line3)
            data_resp.set_pincode_id(obj.pincode_id)
            data_resp.set_city_id(obj.city_id)
            data_resp.set_district_id(obj.district_id)
            data_resp.set_state_id(obj.state_id)
            data_resp.set_type(obj.type)
            list_data.append(data_resp)
        # vpage = WisefinPaginator(emp_obj, vys_page.get_index(), 10)
        # list_data.set_pagination(vpage)
        return list_data

    def get_employee_addr(self, id):
        obj = EmployeeAddress.objects.get(id=id)
        data_resp = EmployeeAddressResponse()
        data_resp.set_id(obj.id)
        data_resp.set_line1(obj.line1)
        data_resp.set_line2(obj.line2)
        data_resp.set_line3(obj.line3)
        data_resp.set_pincode_id(obj.pincode_id)
        data_resp.set_state_id(obj.state_id)
        data_resp.set_city_id(obj.city_id)
        data_resp.set_district_id(obj.district_id)
        data_resp.set_type(obj.type)

        return data_resp

    def del_employee_addr(self, id):
        EmployeeAddress.objects.filter(id=id).update(status=ActiveStatus.Delete)
        success_obj = Success()
        success_obj.set_status(SuccessStatus.SUCCESS)
        success_obj.set_message(SuccessMessage.DELETE_MESSAGE)
        return success_obj

##FOR OVERALL GET
    def fetch_employee_addres(self, employee_id):
        emp_obj = EmployeeAddress.objects.filter(status=ActiveStatus.Active, employee_id=employee_id)
        list_data = []
        for obj in emp_obj:
            data_resp = EmployeeAddressResponse()
            data_resp.set_line1(obj.line1)
            data_resp.set_line2(obj.line2)
            data_resp.set_line3(obj.line3)
            data_resp.set_pincode_id(obj.pincode_id)
            data_resp.set_city_id(obj.city_id)
            data_resp.set_district_id(obj.district_id)
            data_resp.set_state_id(obj.state_id)
            data_resp.set_type(obj.type)
            list_data.append(data_resp)
        # vpage = WisefinPaginator(emp_obj, vys_page.get_index(), 10)
        # list_data.set_pagination(vpage)
        return list_data



