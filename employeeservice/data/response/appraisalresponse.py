import json


from employeeservice.util.emputil import grade_type_val, Appraisal_type_val



class AppraisalResponse:
    id, employee, designation, appraisal_status, grade, appraisal_date = (None,) * 6

    def get(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def set_id(self, id):
        self.id = id

    def set_employee(self, employee,arr):
        self.employee = None
        for i in arr:
            if i.id == employee:
                self.employee = i
                break

    def set_designation(self, designation,arr):
        designation = int(designation)
        self.designation = None
        for i in arr:
            if i.id == designation:
                self.designation = i
                break


    def set_appraisal_status(self, appraisal_status):
        val = Appraisal_type_val(appraisal_status)
        self.appraisal_status = val

    def set_grade(self, grade):
        val = grade_type_val(grade)
        self.grade = val

    def set_appraisal_date(self, appraisal_date):
        self.appraisal_date = appraisal_date

    def set_designation_id(self,designation_id):
        self.designation = designation_id

    def set_employee_id(self,employee_id):
        self.employee = employee_id

