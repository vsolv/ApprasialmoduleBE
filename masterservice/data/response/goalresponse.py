import json


class GoalResponse:
    id, goal, description = (None,)*3

    def get(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def set_id(self, id):
        self.id = id

    def set_goal(self, goal):
        self.goal = goal

    def set_description(self, description):
        self.description = description
