class EmployeeRequest:
    id, user_id, code, first_name, middle_name, last_name, email_id, role, doj, gender, dob, departement, manager, employee_type = (None,)*14

    def __init__(self, user_obj):
        if 'id' in user_obj:
            self.id = user_obj['id']
        if 'user_id' in user_obj:
            self.user_id = user_obj['user_id']
        # if 'code' in user_obj:
        #     self.code = user_obj['code']
        if 'first_name' in user_obj:
            self.first_name = user_obj['first_name']
        if 'middle_name' in user_obj:
            self.middle_name = user_obj['middle_name']
        if 'last_name' in user_obj:
            self.last_name = user_obj['last_name']
        if 'email_id' in user_obj:
            self.email_id = user_obj['email_id']
        if 'role' in user_obj:
            self.role = user_obj['role']
        if 'doj' in user_obj:
            self.doj = user_obj['doj']
        if 'gender' in user_obj:
            self.gender = user_obj['gender']
        if 'dob' in user_obj:
            self.dob = user_obj['dob']
        if 'departement' in user_obj:
            self.departement = user_obj['departement']
        if 'manager' in user_obj:
            self.manager = user_obj['manager']
        if 'employee_type' in user_obj:
            self.employee_type = user_obj['employee_type']

    def get_id(self):
        return self.id

    def get_user_id(self):
        return self.user_id

    def get_first_name(self):
        return self.first_name

    def get_middle_name(self):
        return self.middle_name

    def get_last_name(self):
        return self.last_name

    def get_email_id(self):
        return self.email_id

    def get_role(self):
        return self.role

    def get_doj(self):
        return self.doj

    def get_gender(self):
        return self.gender

    def get_dob(self):
        return self.dob

    def get_departement(self):
        return self.departement

    def get_manager(self):
        return self.manager

    def get_employee_type(self):
        return self.employee_type
    # def get_code(self):
    #     return self.code