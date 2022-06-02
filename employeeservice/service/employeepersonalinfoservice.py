from employeeservice.util.emputil import ActiveStatus
from utilityservice.data.response.emplist import WisefinList
from utilityservice.data.response.empmessage import WisefinMsg, SuccessMessage, Success, SuccessStatus
from utilityservice.data.response.emppaginator import WisefinPaginator
from employeeservice.models.employeemodels import EmployeePersionalInfo
from employeeservice.data.response.employeepersonalinforesponse import EmployeePersonalinfoResponse


class EmployeePersonalinfoService:
    def create_personalinfo(self, data_obj, personalinfo_id):
        resp = WisefinMsg()
        create_arr = data_obj['create_arr']
        update_arr = data_obj['update_arr']
        if len(update_arr) > 0:
            for val in update_arr:
                EmployeePersionalInfo.objects.filter(id=val['id']).update(**val)

        else:
            if len(create_arr) > 0:
                perinfolist = [EmployeePersionalInfo(**val) for val in create_arr]
                EmployeePersionalInfo.objects.bulk_create(perinfolist)
            resp.set_message(SuccessMessage.CREATE_MESSAGE)

        return resp


    def fetch_personalinfo(self, employee_id):
        emp_personalinfo = EmployeePersionalInfo.objects.filter(status=ActiveStatus.Active, employee_id=employee_id)
        list_data = WisefinList()
        for obj in emp_personalinfo:
            data_resp = EmployeePersonalinfoResponse()
            data_resp.set_id(obj.id)
            data_resp.set_martial_status(obj.martial_status)
            data_resp.set_wedding_date(obj.wedding_date)
            data_resp.set_emc_contact_person_number(obj.emc_contact_person_number)
            data_resp.set_emc_contact_person(obj.emc_contact_person)
            data_resp.set_nationality(obj.nationality)
            list_data.append(data_resp)
        # vpage = WisefinPaginator(emp_personalinfo, vys_page.get_index(), 10)
        # list_data.set_pagination(vpage)
        return list_data

    def get_employee_perinfo(self, id):
        obj = EmployeePersionalInfo.objects.get(id=id)
        data_resp = EmployeePersonalinfoResponse()
        data_resp.set_id(obj.id)
        data_resp.set_martial_status(obj.martial_status)
        data_resp.set_wedding_date(obj.wedding_date)
        data_resp.set_emc_contact_person_number(obj.emc_contact_person_number)
        data_resp.set_emc_contact_person(obj.emc_contact_person)
        data_resp.set_nationality(obj.nationality)

        return data_resp

    def del_employee_perinfo(self, id):
        EmployeePersionalInfo.objects.filter(id=id).update(status=ActiveStatus.Delete)
        success_obj = Success()
        success_obj.set_status(SuccessStatus.SUCCESS)
        success_obj.set_message(SuccessMessage.DELETE_MESSAGE)
        return success_obj

#FOR OVERALL GET
    def fetch_personalinformation(self, employee_id):
        emp_personalinfo = EmployeePersionalInfo.objects.filter(status=ActiveStatus.Active, employee_id=employee_id)
        list_data = []
        for obj in emp_personalinfo:
            data_resp = EmployeePersonalinfoResponse()
            data_resp.set_id(obj.id)
            data_resp.set_martial_status(obj.martial_status)
            data_resp.set_wedding_date(obj.wedding_date)
            data_resp.set_emc_contact_person_number(obj.emc_contact_person_number)
            data_resp.set_emc_contact_person(obj.emc_contact_person)
            data_resp.set_nationality(obj.nationality)
            list_data.append(data_resp)
        # vpage = WisefinPaginator(emp_personalinfo, vys_page.get_index(), 10)
        # list_data.set_pagination(vpage)
        return list_data




