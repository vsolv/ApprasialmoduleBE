import json


class DepartementResponse:
    id, name, dept_id, description, short_notation, is_sys = (None,) * 6

    def get(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def set_id(self, id):
        self.id = id

    def set_name(self, name):
        self.name = name

    # def set_dept_id(self, dept_id):
    #     self.dept_id = dept_id

    def set_description(self, description):
        self.description = description

    # def set_short_notation(self, short_notation):
    #     self.short_notation = short_notation

    # def set_is_sys(self,is_sys):
    #     self.is_sys = is_sys