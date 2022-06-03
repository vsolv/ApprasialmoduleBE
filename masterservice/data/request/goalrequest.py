class GoalRequest:
    def fetch_id(self,obj):
        if 'id' in obj:
            return obj['id']
        else:
            return

    def fetch_request(self, user_obj):
        data = dict()
        if 'id' in user_obj:
            data['id'] = user_obj['id']
        if 'goal' in user_obj:
            data['goal'] = user_obj['goal']
        if 'description' in user_obj:
            data['description'] = user_obj['description']

        return data