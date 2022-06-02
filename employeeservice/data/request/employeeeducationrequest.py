class EmployeeEducationRequest:
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
            if 'inst_name' in obj:
                data['inst_name'] = obj['inst_name']
            if 'passing_year' in obj:
                data['passing_year'] = obj['passing_year']
            if 'percentage' in obj:
                data['percentage'] = obj['percentage']
            if 'title' in obj:
                data['title'] = obj['title']
            if 'qualification' in obj:
                data['qualification'] = obj['qualification']
            data['employee_id'] = employee_id

            if 'id' in data:
                update_arr.append(data)

            else:
                create_arr.append(data)

        val = {'create_arr': create_arr, 'update_arr': update_arr}

        return val