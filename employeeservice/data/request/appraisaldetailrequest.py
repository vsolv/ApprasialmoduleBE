class AppraisalDetailRequest:
   id, appraisal_id, remarks, rating, goal_mapping = (None,)* 5

   def __init__(self, user_obj):
       if 'id' in user_obj:
           self.id = user_obj['id']
       if 'appraisal_id' in user_obj:
           self.appraisal_id = user_obj['appraisal_id']
       if 'remarks' in user_obj:
           self.remarks = user_obj['remarks']
       if 'rating' in user_obj:
           self.rating = user_obj['rating']
       if 'goal_mapping' in user_obj:
           self.goal_mapping = user_obj['goal_mapping']

   def get_id(self):
       return self.id

   def get_appraisal_id(self):
       return self.appraisal_id

   def get_remarks(self):
       return self.remarks

   def get_rating(self):
       return self.rating

   def get_goal_mapping(self):
       return self.goal_mapping