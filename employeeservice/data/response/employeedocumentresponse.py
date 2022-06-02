import json

# from employeeservice.util.emputil import doc_type_val


class EmployeeDocumentResponse:
    id, file_path, file_type, file_name, status = (None,)*5

    def get(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def set_id(self, id):
        self.id = id

    def set_file_path(self, file_path):
        self.file_path = file_path

    def set_file_type(self, file_type):
        # val = doc_type_val(file_type)
        self.file_type = file_type

    def set_file_name(self, file_name):
        self.file_name = file_name

    def set_status(self, status):
        self.status = status
