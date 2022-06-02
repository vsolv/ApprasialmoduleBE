from utilityservice.data.response.emplist import WisefinList
from utilityservice.data.response.wisefinlitelist import WisefinLiteList


class ActiveStatus:
    Active = 1
    Delete = 0

class UserrefType:
    EMPI = 'EMPI'

class Martial_Status:
    single = {"id": 1, "text": "Single"}
    married = {"id": 2, "text": "Married"}

def get_martial_status(type):
    if(type==Martial_Status.single['id']):
        m = Martial_Status.single

    elif(type==Martial_Status.married['id']):
        m = Martial_Status.married
    else:
        m = None
    return m

class AddressType:
    type1 = {"id": 1, "text": "permanent"}
    type2 = {"id": 2, "text": "temporary"}


def get_type_val(type):

    if(type==AddressType.type1['id']):
        d = AddressType.type1
    elif (type==AddressType.type2['id']):
        d = AddressType.type2
    else:
        d = None
    return d

class document_upload:
    # file1 = {"id": 1, "text": "profile"}
    # file2 = {"id": 2, "text": "other"}
    file1 = 1
    file2 = 2
# def doc_type_val(type):
#     if(type==document_uplode.file1['id']):
#         d = document_uplode.file1
#     elif(type==document_uplode.file2['id']):
#         d = document_uplode.file2
#     else:
#         d = None
#     return d

# class Employee_type:
#     type1 = {"id": 1, "text": "Employee"}
#     type2 = {"id": 2, "text": "Student"}
#     type3 = {"id": 3, "text": "Traniee"}
#     type4 = {"id": 4, "text": "Contractor"}
#     type5 = {"id": 5, "text": "Freelance"}
#
# def employee_type_val(type):
#     if type == Employee_type.type1['id']:
#         e = Employee_type.type1
#     elif type == Employee_type.type2['id']:
#         e = Employee_type.type2
#     elif type == Employee_type.type3['id']:
#         e = Employee_type.type3
#     elif type == Employee_type.type4['id']:
#         e = Employee_type.type4
#     elif type == Employee_type.type5['id']:
#         e = Employee_type.type5
#     else:
#         e = None
#     return e

class Gender:
    type1 = {"id": 1, "text": "Male"}
    type2 = {"id": 2, "text": "Female"}

def gender_type_val(type):
    if type == Gender.type1['id']:
        g = Gender.type1
    elif type == Gender.type2['id']:
        g = Gender.type2
    else:
        g = None
    return g

def get_fileextension_val(extension):
    if extension in ['txt','doc','pdf','ppt','pot','pps','pptx','odt','odg','odp','ods','docx','docm','dotx','dotm','docb',
                     'xlsx','xls','xlt','xlm','xlsm','xltx','xltm','jpg', 'jpeg','tiff', 'tif','png']:
        return True
    else:
        return False


class Employee_type:
    EMPLOYEE = 1
    STUDENT = 2
    TRAINEE = 3
    CONTRACTOR = 4
    FREELANCER = 5

    EMPLOYEE_VAL = 'EMPLOYEE'
    STUDENT_VAL = 'STUDENT'
    TRAINEE_VAL = 'TRANIEE'
    CONTRACTOR_VAL = 'CONTRACTOR'
    FREELANCER_VAL = 'FREELANCER'

def employee_type_val(type):
   if(type == Employee_type.EMPLOYEE):
       vys_list = WisefinLiteList()
       vys_list.value = type
       vys_list.name = 'EMPLOYEE'
       return vys_list
   if (type == Employee_type.STUDENT):
       vys_list = WisefinLiteList()
       vys_list.value = type
       vys_list.name = 'STUDENT'
       return vys_list
   if (type == Employee_type.TRAINEE):
       vys_list = WisefinLiteList()
       vys_list.value = type
       vys_list.name = "TRAINEE"
       return vys_list
   if (type == Employee_type.CONTRACTOR):
       vys_list = WisefinLiteList()
       vys_list.value = type
       vys_list.name = 'CONTRACTOR'
       return vys_list
   if (type == Employee_type.FREELANCER):
       vys_list = WisefinLiteList()
       vys_list.value = type
       vys_list.name = 'FREELANCER'
       return vys_list

def employee_type_compostie():
    idarr = [Employee_type.EMPLOYEE, Employee_type.STUDENT, Employee_type.TRAINEE, Employee_type.CONTRACTOR,
             Employee_type.FREELANCER]
    typearr = [Employee_type.EMPLOYEE_VAL, Employee_type.STUDENT_VAL, Employee_type.TRAINEE_VAL,
               Employee_type.CONTRACTOR_VAL,
               Employee_type.FREELANCER_VAL]
    length = len(idarr)
    list_data = WisefinList()
    for x in range(length):
        vyslite = WisefinLiteList()
        vyslite.value = idarr[x]
        vyslite.name = typearr[x]
        list_data.append(vyslite)
    return list_data
