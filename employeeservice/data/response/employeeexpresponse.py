import json


class EmployeeExpResponse:
    id, company, work_experience, period_from, period_to, role, city = (None,) * 7

    def get(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def set_id(self, id):
        self.id = id

    def set_company(self, company):
        self.company = company

    def set_work_experience(self, work_experience):
        self.work_experience = work_experience

    def set_period_from(self, period_from):
        self.period_from = str(period_from)

    def set_period_to(self, period_to):
        self.period_to = str(period_to)

    def set_role(self, role):
        self.role = role

    def set_city(self, city):
        self.city = city
