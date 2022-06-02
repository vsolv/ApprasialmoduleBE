import json

from employeeservice.util.emputil import get_type_val


class EmployeeAddressResponse:
    id, line1, line2, line3, pincode_id, city_id, district_id, state_id, type = (None,) * 9


    def get(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


    def set_id(self, id):
        self.id = id

    def set_line1(self, line1):
        self.line1 = line1

    def set_line2(self, line2):
        self.line2 = line2

    def set_line3(self, line3):
        self.line3 = line3

    def set_pincode_id(self, pincode_id):
        self.pincode_id = pincode_id

    def set_city_id(self, city_id):
        self.city_id = city_id

    def set_district_id(self, district_id):
        self.district_id = district_id

    def set_state_id(self, state_id):
        self.state_id = state_id

    def set_type(self, type):
        val = get_type_val(type)
        self.type = val