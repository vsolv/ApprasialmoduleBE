import json

from employeeservice.util.emputil import grade_type_val
from masterservice.service.designationservice import DesignationService
from masterservice.service.goalservice import GoalService


class GoalMappingResponse:
    id, sub_goal, grade, designation_id, goal_id = (None,)*5

    def get(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def set_id(self, id):
        self.id = id

    def set_sub_goal(self, sub_goal):
        data = []
        val = {
            'description': sub_goal
        }
        data.append(val)
        self.sub_goal = data

    def set_grade(self, grade):
        val = grade_type_val(grade)
        self.grade = val

    def set_designation_id(self, designation,arr):
        designation = int(designation)
        self.designation = None
        for i in arr:
            if i.id == designation:
                self.designation = i
                break


    def set_goal_id(self, goal_id,arr):
        self.goal = None
        for i in arr:
            if i.id == goal_id:
                self.goal_id = i
                break

    def set_designation(self, designation):
        self.designation = designation

    def set_goal(self,goal):
        self.goal = goal