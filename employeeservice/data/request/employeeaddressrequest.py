class EmployeeAddressRequest:
    def fetch_id(self, obj):
        if 'id' in obj:
            return obj['id']
        else:
            return

    def fetch_request(self, user_obj, employee_id):

        arr_create = []
        arr_update = []
        for obj in user_obj:
            data = dict()
            if 'id' in obj:
                data['id'] = obj['id']
            if 'line1' in obj:
                data['line1'] = obj['line1']
            if 'line2' in obj:
                data['line2'] = obj['line2']
            if 'line3' in obj:
                data['line3'] = obj['line3']
            if 'pincode_id' in obj:
                data['pincode_id'] = obj['pincode_id']
            if 'city_id' in obj:
                data['city_id'] = obj['city_id']
            if 'district_id' in obj:
                data['district_id'] = obj['district_id']
            if 'state_id' in obj:
                data['state_id'] = obj['state_id']
            if 'type' in obj:
                data['type'] = obj['type']
            data['employee_id'] = employee_id

            if 'id' in data:
                arr_update.append(data)
            else:
                arr_create.append(data)

        val = {'update_arr': arr_update, 'create_arr': arr_create}

        return val
