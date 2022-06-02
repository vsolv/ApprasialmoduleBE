class EmployeePersonalinfoRequest:
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
            if 'martial_status' in obj:
                data['martial_status'] = obj['martial_status']
            if 'wedding_date' in obj:
                data['wedding_date'] = obj['wedding_date']
            if 'emc_contact_person' in obj:
                data['emc_contact_person'] = obj['emc_contact_person']
            if 'phone_regex' in obj:
                data['phone_regex'] = obj['phone_regex']
            if 'emc_contact_person_number' in obj:
                data['emc_contact_person_number'] = obj['emc_contact_person_number']
            if 'nationality' in obj:
                data['nationality'] = obj['nationality']
            data['employee_id'] = employee_id

            if 'id' in data:
                update_arr.append(data)
            else:
                create_arr.append(data)
        val = {'create_arr': create_arr, 'update_arr': update_arr}

        return val
