from employeeservice.data.response.employeeexpresponse import EmployeeExpResponse
from utilityservice.data.response.empmessage import WisefinMsg, SuccessMessage, ErrorMessage, Success, SuccessStatus, Error, ErrorDescription
from utilityservice.data.response.emplist import WisefinList
from employeeservice.util.emputil import ActiveStatus
from utilityservice.data.response.emppaginator import WisefinPaginator
from employeeservice.models.employeemodels import EmployeeExperiences


class EmployeeExpService:
    def create_employee_exp(self, data_obj, employee_id):
        resp = WisefinMsg()
        create_arr = data_obj['create_arr']
        update_arr = data_obj['update_arr']
        if len(update_arr) > 0:
            for val in update_arr:
                EmployeeExperiences.objects.filter(id=val['id']).update(**val)

        else:
            if len(create_arr) > 0:
                explist = [EmployeeExperiences(**val) for val in create_arr]
                EmployeeExperiences.objects.bulk_create(explist)
            resp.set_message(SuccessMessage.CREATE_MESSAGE)

        return resp

    def fetch_employeexp(self, employee_id):
        employeeexp_obj = EmployeeExperiences.objects.filter(status=ActiveStatus.Active, employee_id=employee_id)
        list_data = WisefinList()
        for obj in employeeexp_obj:
            data_resp = EmployeeExpResponse()
            data_resp.set_id(obj.id)
            data_resp.set_company(obj.company)
            data_resp.set_role(obj.role)
            data_resp.set_city(obj.city)
            data_resp.set_work_experience(obj.work_experience)
            data_resp.set_period_from(obj.period_from)
            data_resp.set_period_to(obj.period_to)
            list_data.append(data_resp)
        # vys_page = WisefinPaginator(employeeexp_obj, vys_page.get_index(), 10)
        # list_data.set_pagination(vys_page)
        return list_data

    def get_employee_exp(self, id):
        obj = EmployeeExperiences.objects.get(id=id)
        data_resp = EmployeeExpResponse()
        data_resp.set_id(obj.id)
        data_resp.set_company(obj.company)
        data_resp.set_role(obj.role)
        data_resp.set_city(obj.city)
        data_resp.set_work_experience(obj.work_experience)
        data_resp.set_period_from(obj.period_from)
        data_resp.set_period_to(obj.period_to)

        return data_resp

    def del_employee_exp(self, id):
        EmployeeExperiences.objects.filter(id=id).update(status=ActiveStatus.Delete)
        success_obj = Success()
        success_obj.set_status(SuccessStatus.SUCCESS)
        success_obj.set_message(SuccessMessage.DELETE_MESSAGE)
        return success_obj

#FOR OVERALL GET
    def fetch_employeexperience(self, employee_id):
        employeeexp_obj = EmployeeExperiences.objects.filter(status=ActiveStatus.Active, employee_id=employee_id)
        list_data = []
        for obj in employeeexp_obj:
            data_resp = EmployeeExpResponse()
            data_resp.set_id(obj.id)
            data_resp.set_company(obj.company)
            data_resp.set_role(obj.role)
            data_resp.set_city(obj.city)
            data_resp.set_work_experience(obj.work_experience)
            data_resp.set_period_from(obj.period_from)
            data_resp.set_period_to(obj.period_to)
            list_data.append(data_resp)
        # vys_page = WisefinPaginator(employeeexp_obj, vys_page.get_index(), 10)
        # list_data.set_pagination(vys_page)
        return list_data
