from employeeservice.data.response.employeeeducationresponse import EmployeeEducationResponse
from employeeservice.util.emputil import ActiveStatus
from utilityservice.data.response.emplist import WisefinList
from utilityservice.data.response.empmessage import WisefinMsg, SuccessMessage, Success, SuccessStatus
from employeeservice.models.employeemodels import Employee_educationDetails
from utilityservice.data.response.emppaginator import WisefinPaginator


class EmployeeEducationService:
    def create_emp_edu(self, data_obj, emp_edu_id):
        resp = WisefinMsg()
        create_arr = data_obj['create_arr']
        update_arr = data_obj['update_arr']
        if len(update_arr) > 0:
            for val in update_arr:
                Employee_educationDetails.objects.filter(id=val['id']).update(**val)

        else:
            if len(create_arr) > 0:
                edulist = [Employee_educationDetails(**vals) for vals in create_arr]
                Employee_educationDetails.objects.bulk_create(edulist)
            resp.set_message(SuccessMessage.CREATE_MESSAGE)

        return resp

    def fetch_emp_edu(self, employee_id):
        empedu_obj = Employee_educationDetails.objects.filter(status=ActiveStatus.Active, employee_id=employee_id)
        list_data = WisefinList()
        for obj in empedu_obj:
            data_resp = EmployeeEducationResponse()
            data_resp.set_id(obj.id)
            data_resp.set_inst_name(obj.inst_name)
            data_resp.set_passing_year(obj.passing_year)
            data_resp.set_title(obj.title)
            data_resp.set_percentage(obj.percentage)
            data_resp.set_qualification(obj.qualification)
            list_data.append(data_resp)
        # vpage = WisefinPaginator(empedu_obj, vys_page.get_index(), 10)
        # list_data.set_pagination(vpage)
        return list_data

    def get_employee_edu(self, id):
        obj = Employee_educationDetails.objects.get(id=id)
        data_resp = EmployeeEducationResponse()
        data_resp.set_id(obj.id)
        data_resp.set_inst_name(obj.inst_name)
        data_resp.set_passing_year(obj.passing_year)
        data_resp.set_title(obj.title)
        data_resp.set_percentage(obj.percentage)
        data_resp.set_qualification(obj.qualification)

        return data_resp

    def del_employee_edu(self,  id):
        Employee_educationDetails.objects.filter(id=id).update(status=ActiveStatus.Delete)
        success_obj = Success()
        success_obj.set_status(SuccessStatus.SUCCESS)
        success_obj.set_message(SuccessMessage.DELETE_MESSAGE)
        return success_obj

#FOR OVERALL GET
    def fetch_emp_education(self, employee_id):
        empedu_obj = Employee_educationDetails.objects.filter(status=ActiveStatus.Active, employee_id=employee_id)
        list_data = []
        for obj in empedu_obj:
            data_resp = EmployeeEducationResponse()
            data_resp.set_id(obj.id)
            data_resp.set_inst_name(obj.inst_name)
            data_resp.set_passing_year(obj.passing_year)
            data_resp.set_title(obj.title)
            data_resp.set_percentage(obj.percentage)
            data_resp.set_qualification(obj.qualification)
            list_data.append(data_resp)
        # vpage = WisefinPaginator(empedu_obj, vys_page.get_index(), 10)
        # list_data.set_pagination(vpage)
        return list_data