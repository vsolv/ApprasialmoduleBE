class ErrorMessage:
    # Login
    INVALID_USER_ID = 'INVALID_USER_ID'
    INVALID_PORT_ID = 'INVALID_PORT_ID'
    INVALID_PORT_MODULE_ID = 'INVALID_PORT_MODULE_ID'
    INVALID_DATA = 'INVALID_DATA'
    UNEXPECTED_ERROR = 'UNEXPECTED_ERROR'
    INVALID_EMPLOYEE_ID = 'INVALID_EMPLOYEE_ID'

    # user
    EMPLOYEE_ADMIN = 'PERMISSION DENIED'


class ErrorDescription:
    # Login
    INVALID_USER_ID = 'INVALID_USER_ID'
    INVALID_PORT_ID = 'INVALID_PORT_ID'
    INVALID_PORT_MODULE_ID = 'INVALID_PORT_MODULE_ID'
    INVALID_DATA = 'INVALID_DATA'
    UNEXPECTED_ERROR ='UNEXPECTED_ERROR'
    # user
    EMPLOYEE_ADMIN = 'PERMISSION DENIED'


import json


class WisefinMsg:
    status = None
    message = None

    def get(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def set_status(self, status):
        self.status = status

    def set_message(self, message):
        self.message = message


class SuccessStatus:
    DEFAULT = 'true'
    HTTP = 200
    SUCCESS = 'success'


class SuccessMessage:
    ACTIVATED='Successfully Activated'
    INACTIVATED='Successfully Inactivated'
    DELETE_MESSAGE = 'Successfully Deleted'
    CREATE_MESSAGE = 'Successfully Created'
    UPDATE_MESSAGE = 'Successfully Updated'
    CLOSED_MESSAGE = 'Successfully Closed'
    SUCCESSFULLY_LOGOUT = 'Successfully logout'
    APPROVED_MESSAGE = 'Approved Successfully'
    REJECTED_MESSAGE = 'Rejected Successfully'
    EMAIL = ' Email Successfully Sended'



class Error:
    code = None
    description = None
    errorcode=None
    def __init__(self):
        pass

    def set_code(self, code):
        self.code = code

    def errorcode(self, errorcode):
        self.errorcode = errorcode

    def set_description(self, description):
        self.description = description

    def get_code(self):
        return self.code

    def get_description(self):
        return self.description

    def get(self):
        return json.dumps(self, default=lambda o: o.__dict__,sort_keys=True, indent=4)

class Success:
    status = None
    message = None

    def get(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def set_status(self, status):
        self.status = status

    def set_message(self, message):
        self.message = message
