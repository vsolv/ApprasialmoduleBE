import json


class GoalMappingResponse:
    id, sub_goal, grade, designation_id, goal_id = (None,)*5

    def get(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def set_id(self, id):
        self.id = id

    def set_sub_goal(self, sub_goal):
        self.sub_goal = sub_goal

    def set_grade(self, grade):
        self.grade = grade

    def set_designation_id(self, designation_id):
        self.designation_id = designation_id

    def set_goal_id(self,goal_id):
        self.goal_id = goal_id
