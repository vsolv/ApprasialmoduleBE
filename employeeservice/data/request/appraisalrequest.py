class AppraisalRequest:
    id, employee, designation, appraisal_status, grade, appraisal_date = (None,) * 6

    def __init__(self, user_obj):
        if 'id' in user_obj:
            self.id = user_obj['id']
        if 'employee' in user_obj:
            self.employee = user_obj['employee']
        if 'designation' in user_obj:
            self.designation = user_obj['designation']
        if 'appraisal_status' in user_obj:
            self.appraisal_status = user_obj['appraisal_status']
        if 'grade' in user_obj:
            self.grade = user_obj['grade']
        if 'appraisal_date' in user_obj:
            self.appraisal_date = user_obj['appraisal_date']

    def get_id(self):
        return self.id

    def get__employee(self):
        return self.employee

    def get_designation(self):
        return self.designation

    def get_appraisal_status(self):
        return self.appraisal_status

    def get_grade(self):
        return self.grade

    def get_appraisal_date(self):
        return self.appraisal_date