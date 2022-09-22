from employeeservice.data.response.appraisaldetailresponse import AppraisalDetailResponse
from employeeservice.models import Appraisaldetails
from employeeservice.util.emputil import ActiveStatus
from masterservice.service.goalmappingservice import GoalMappingService
from utilityservice.data.response.emplist import WisefinList
from utilityservice.data.response.empmessage import WisefinMsg, SuccessMessage, Success, SuccessStatus
from utilityservice.data.response.emppaginator import WisefinPaginator


class AppraisalDetailService:
    def appraisal_detail_create(self, data_obj, appraisal_id):
        resp = WisefinMsg()
        if not data_obj.get_id() is None:
            obj = Appraisaldetails.objects.filter(id=data_obj.get_id()).update(appraisal_id=appraisal_id,
                                                                               remarks=data_obj.get_remarks(),
                                                                               rating=data_obj.get_rating(),
                                                                               goal_mapping=data_obj.get_goal_mapping())

            obj = Appraisaldetails.objects.get(id=data_obj.get_id())


        else:
            obj = Appraisaldetails.objects.create(appraisal_id=appraisal_id,
                                                  remarks=data_obj.get_remarks(),
                                                  rating=data_obj.get_rating(),
                                                  goal_mapping=data_obj.get_goal_mapping())

            resp.set_message(SuccessMessage.CREATE_MESSAGE)

        return resp


    def fetch_appraisal_detail(self,vys_page):
        obj = Appraisaldetails.objects.filter(status=ActiveStatus.Active)
        goal_mapping_id = []
        for i in obj:
            goal_mapping = i.goal_mapping
            goal_mapping_id.append(goal_mapping)
        goal_mapping_serv = GoalMappingService()
        goal_mapping = goal_mapping_serv.goal_mapping_info(goal_mapping_id)
        list_data = WisefinList()
        for x in obj:
            data_resp = AppraisalDetailResponse()
            data_resp.set_id(x.id)
            data_resp.set_appraisal_id(x.appraisal_id)
            data_resp.set_rating(x.rating)
            data_resp.set_remarks(x.remarks)
            data_resp.set_goal_mapping(x.goal_mapping,goal_mapping)
            list_data.append(data_resp)
        vpage = WisefinPaginator(obj, vys_page.get_index(), 10)
        list_data.set_pagination(vpage)
        return list_data

    def get_appraisal_detail(self, id):
        obj = Appraisaldetails.objects.get(id=id)
        data_resp = AppraisalDetailResponse()
        data_resp.set_id(obj.id)
        data_resp.set_appraisal_id(obj.appraisal_id)
        data_resp.set_rating(obj.rating)
        data_resp.set_remarks(obj.remarks)
        goal_mapping_serv =GoalMappingService()
        goal_mapping = goal_mapping_serv.get_goal_mapping(obj.goal_mapping)
        data_resp.set_goal_mapping_id(goal_mapping)
        return data_resp

    def del_appraisal_detail(self,id):
        obj = Appraisaldetails.objects.filter(id=id).update(status=ActiveStatus.Delete)
        success_obj = Success()
        success_obj.set_status(SuccessStatus.SUCCESS)
        success_obj.set_message(SuccessMessage.DELETE_MESSAGE)
        return success_obj


#FOR OVERALL_GET
    def get_appraisal_details(self, appraisal_id):
        details_obj = Appraisaldetails.objects.filter(status=ActiveStatus.Active, appraisal_id=appraisal_id)
        list_data = []
        for obj in details_obj:
            data_resp = AppraisalDetailResponse()
            data_resp.set_id(obj.id)
            data_resp.set_rating(obj.rating)
            data_resp.set_remarks(obj.remarks)
            data_resp.set_appraisal_id(obj.appraisal_id)
            goal_mapping_serv = GoalMappingService()
            goal_mapping = goal_mapping_serv.get_goal_mapping(obj.goal_mapping)
            data_resp.set_goal_mapping_id(goal_mapping)
            list_data.append(data_resp)

        return list_data

