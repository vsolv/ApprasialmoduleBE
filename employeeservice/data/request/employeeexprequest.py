class EmployeeExpRequest:
    def fetch_id(self, obj):
        if 'id' in obj:
            return obj['id']
        else:
            return

    def fetch_request(self, user_obj, employee_id):
        create_arr = []
        update_arr = []
        for obj in user_obj:
            data = dict()
            if 'id' in obj:
                data['id'] = obj['id']
            if 'company' in obj:
                data['company'] = obj['company']
            if 'work_experience' in obj:
                data['work_experience'] = obj['work_experience']
            if 'period_from' in obj:
                data['period_from'] = obj['period_from']
            if 'period_to' in obj:
                data['period_to'] = obj['period_to']
            if 'role' in obj:
                data['role'] = obj['role']
            if 'city' in obj:
                data['city'] = obj['city']
            data['employee_id'] = employee_id

            if 'id' in data:
                update_arr.append(data)
            else:
                create_arr.append(data)

        val = {'create_arr': create_arr, 'update_arr': update_arr}

        return val

