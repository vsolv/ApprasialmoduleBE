class DepartmentRequest:
    def fetch_id(self, obj):
        if 'id' in obj:
            return obj['id']
        else:
            return

    def fetch_request(self, user_obj):
        data = dict()

        if 'id' in user_obj:
            data['id'] = user_obj['id']
        if 'name' in user_obj:
            data['name'] = user_obj['name']
        # if 'dept_id' in user_obj:
        #     data['dept_id'] = user_obj['dept_id']
        if 'description' in user_obj:
            data['description'] = user_obj['description']
        # if 'short_notation' in user_obj:
        #     data['short_notation'] = user_obj['short_notation']
        # if 'is_sys' in user_obj:
        #     data['is_sys'] = user_obj['is_sys']

        return data