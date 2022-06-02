import json


class EmployeeDocumentRequest:
    id = None
    file_path = None
    file_type = None
    file_name = None
    employee_id = None

    def get(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def __init__(self, user_obj):
        # if 'id' in user_obj:
        #     self.id = user_obj['id']
        if 'file_path' in user_obj:
            self.file_path = user_obj['file_path']
        if 'file_type' in user_obj:
            self.file_type = user_obj['file_type']
        if 'file_name' in user_obj:
            self.file_name = user_obj['file_name']
        if 'employee_id' in user_obj:
            self.employee_id = user_obj['employee_id']

    def get_id(self):
        return self.id

    def get_file_path(self):
        return self.file_path

    def get_file_type(self):
        return self.file_type

    def get_file_name(self):
        return self.file_name

    def get_employee_id(self):
        return self.employee_id

    # def fetch_id(self, obj):
    #     if 'id' in obj:
    #         return obj['id']
    #     else:
    #         return
    #
    # def fetch_request(self, user_obj, employee_id):
    #     data = dict()
    #     if 'id' in user_obj:
    #         data['id'] = user_obj['id']
    #     if 'file_path' in user_obj:
    #         data['file_path'] = user_obj['file_path']
    #     if 'file_type' in user_obj:
    #         data['file_type'] = user_obj['file_type']
    #     if 'file_name' in user_obj:
    #         data['file_name'] = user_obj['file_name']
    #     data['employee_id'] = employee_id
    #
    #     return data
