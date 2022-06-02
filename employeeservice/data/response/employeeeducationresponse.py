import json
class EmployeeEducationResponse:
    id, inst_name, passing_year, percentage, title, qualification = (None,)* 6

    def get(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def set_id(self, id):
        self.id = id

    def set_inst_name(self, inst_name):
        self.inst_name = inst_name

    def set_passing_year(self, passing_year):
        self.passing_year = passing_year

    def set_percentage(self, percentage):
        self.percentage = percentage

    def set_title(self, title):
        self.title = title

    def set_qualification(self, qualification):
        self.qualification = qualification