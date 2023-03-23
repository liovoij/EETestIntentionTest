import allure
import pytest
import json
import os

from Common.base import request_get_ceshi
from TestData.intention_data import *


@allure.epic('项目名称：泛微小e意图识别')
@allure.feature('考勤管理')
class TestKaoQin:
    @allure.story('考勤管理>打卡>签到')
    @pytest.mark.parametrize('circle', attendance_sign_in)
    def test_attendance_sign_in(self, circle):
        # 请求接口并获取返回的data
        request = request_get_ceshi(circle['text'])
        response = json.loads(request['data'])
        # 接口返回的值
        response_title = response['intentInfo']['title']
        response_name = response['intentInfo']['name']
        response_text = response['text']
        response_userId = response['userId']
        response_status = response['status']
        response_action = response['invoker']['action']
        # 期待的结果
        except_title = '签到'
        except_name = 'attendance.sign_in'
        except_text = circle['text']
        except_userId = '11634'
        except_status = 'FINISH'
        except_action = 'url:/mobile/plugin/siri/ajaxApi.jsp?method=attendance_sign_in'
        # 添加至allure
        allure.attach(str(request), '返回内容', allure.attachment_type.JSON)
        # 断言
        assert response_title == except_title, "意图title不同，期望：%s，实际：%s" % (except_title, response_title)
        assert response_name == except_name, "意图name不同，期望：%s，实际：%s" % (except_name, response_name)
        assert response_text == except_text, "语音纠错前后不同，期望：%s，实际：%s" % (except_text, response_text)
        assert response_userId == except_userId, "发送请求者的userId不同，期望：%s，实际：%s" % (except_userId, response_userId)
        assert response_status == except_status, "意图动作不同，期望：%s，实际：%s" % (except_status, response_status)
        assert response_action == except_action, "URL不同，期望：%s，实际：%s" % (except_action, response_action)

    @allure.story('考勤管理>打卡>签退')
    @pytest.mark.parametrize('circle', attendance_sign_back)
    def test_attendance_sign_back(self, circle):
        # 请求接口并获取返回的data
        request = request_get_ceshi(circle['text'])
        response = json.loads(request['data'])
        # 接口返回的值
        response_title = response['intentInfo']['title']
        response_name = response['intentInfo']['name']
        response_text = response['text']
        response_userId = response['userId']
        response_status = response['status']
        response_action = response['invoker']['action']
        # 期待的结果
        except_title = '签退'
        except_name = 'attendance.sign_back'
        except_text = circle['text']
        except_userId = '11634'
        except_status = 'FINISH'
        except_action = 'url:/mobile/plugin/siri/ajaxApi.jsp?method=attendance_sign_back'
        # 添加至allure
        allure.attach(str(request), '返回内容', allure.attachment_type.JSON)
        # 断言
        assert response_title == except_title, "意图title不同，期望：%s，实际：%s" % (except_title, response_title)
        assert response_name == except_name, "意图name不同，期望：%s，实际：%s" % (except_name, response_name)
        assert response_text == except_text, "语音纠错前后不同，期望：%s，实际：%s" % (except_text, response_text)
        assert response_userId == except_userId, "发送请求者的userId不同，期望：%s，实际：%s" % (except_userId, response_userId)
        assert response_status == except_status, "意图动作不同，期望：%s，实际：%s" % (except_status, response_status)
        assert response_action == except_action, "URL不同，期望：%s，实际：%s" % (except_action, response_action)

    @allure.story('考勤管理>打卡>外勤签到')
    @pytest.mark.parametrize('circle', attendance_outside_sign_in)
    def test_attendance_outside_sign_in(self, circle):
        # 请求接口并获取返回的data
        request = request_get_ceshi(circle['text'])
        response = json.loads(request['data'])
        # 接口返回的值
        response_title = response['intentInfo']['title']
        response_name = response['intentInfo']['name']
        response_text = response['text']
        response_userId = response['userId']
        response_status = response['status']
        response_action = response['invoker']['action']
        # 期待的结果
        except_title = '外勤签到'
        except_name = 'attendance.outside_sign_in'
        except_text = circle['text']
        except_userId = '11634'
        except_status = 'FINISH'
        except_action = "redirect:https://www.e-cology.com.cn/spa/hrm/static4mobile/index.html#/outSign?moduleid" \
                        "=799174578"
        # 添加至allure
        allure.attach(str(request), '返回内容', allure.attachment_type.JSON)
        # 断言
        assert response_title == except_title, "意图title不同，期望：%s，实际：%s" % (except_title, response_title)
        assert response_name == except_name, "意图name不同，期望：%s，实际：%s" % (except_name, response_name)
        assert response_text == except_text, "语音纠错前后不同，期望：%s，实际：%s" % (except_text, response_text)
        assert response_userId == except_userId, "发送请求者的userId不同，期望：%s，实际：%s" % (except_userId, response_userId)
        assert response_status == except_status, "意图动作不同，期望：%s，实际：%s" % (except_status, response_status)
        assert response_action == except_action, "URL不同，期望：%s，实际：%s" % (except_action, response_action)

    @allure.story('考勤管理>打卡>外勤签退')
    @pytest.mark.parametrize('circle', attendance_outside_sign_back)
    def test_attendance_outside_sign_back(self, circle):
        # 请求接口并获取返回的data
        request = request_get_ceshi(circle['text'])
        response = json.loads(request['data'])
        # 接口返回的值
        response_title = response['intentInfo']['title']
        response_name = response['intentInfo']['name']
        response_text = response['text']
        response_userId = response['userId']
        response_status = response['status']
        response_action = response['invoker']['action']
        # 期待的结果
        except_title = '外勤签退'
        except_name = 'attendance.outside_sign_back'
        except_text = circle['text']
        except_userId = '11634'
        except_status = 'FINISH'
        except_action = "redirect:https://www.e-cology.com.cn/spa/hrm/static4mobile/index.html#/outSign?moduleid" \
                        "=799174578"
        # 添加至allure
        allure.attach(str(request), '返回内容', allure.attachment_type.JSON)
        # 断言
        assert response_title == except_title, "意图title不同，期望：%s，实际：%s" % (except_title, response_title)
        assert response_name == except_name, "意图name不同，期望：%s，实际：%s" % (except_name, response_name)
        assert response_text == except_text, "语音纠错前后不同，期望：%s，实际：%s" % (except_text, response_text)
        assert response_userId == except_userId, "发送请求者的userId不同，期望：%s，实际：%s" % (except_userId, response_userId)
        assert response_status == except_status, "意图动作不同，期望：%s，实际：%s" % (except_status, response_status)
        assert response_action == except_action, "action不同，期望：%s，实际：%s" % (except_action, response_action)

    @allure.story('考勤管理>打卡>打卡规定查询')
    @pytest.mark.parametrize('circle', clock_rules)
    def test_clock_rules(self, circle):
        # 请求接口并获取返回的data
        request = request_get_ceshi(circle['text'])
        response = json.loads(request['data'])
        # 接口返回的值
        response_title = response['intentInfo']['title']
        response_name = response['intentInfo']['name']
        response_text = response['text']
        response_userId = response['userId']
        response_status = response['status']
        response_action = response['invoker']['action']
        # 期待的结果
        except_title = '打卡规定查询'
        except_name = 'attendance_punch.clock_query.clock.rules'
        except_text = circle['text']
        except_userId = '11634'
        except_status = 'FINISH'
        except_action = 'url:https://test.ai.easst.cn/easst/findUser?method=find_person'
        # 添加至allure
        allure.attach(str(request), '返回内容', allure.attachment_type.JSON)
        # 断言
        assert response_title == except_title, "意图title不同，期望：%s，实际：%s" % (except_title, response_title)
        assert response_name == except_name, "意图name不同，期望：%s，实际：%s" % (except_name, response_name)
        assert response_text == except_text, "语音纠错前后不同，期望：%s，实际：%s" % (except_text, response_text)
        assert response_userId == except_userId, "发送请求者的userId不同，期望：%s，实际：%s" % (except_userId, response_userId)
        assert response_status == except_status, "意图动作不同，期望：%s，实际：%s" % (except_status, response_status)
        assert response_action == except_action, "URL不同，期望：%s，实际：%s" % (except_action, response_action)

    @allure.story('考勤管理>请假>请假')
    @pytest.mark.parametrize('circle', leave_create)
    def test_leave_create(self, circle):
        # 请求接口并获取返回的data
        request = request_get_ceshi(circle['text'])
        response = json.loads(request['data'])
        # 接口返回的值
        response_title = response['intentInfo']['title']
        response_name = response['intentInfo']['name']
        response_text = response['text']
        response_userId = response['userId']
        response_status = response['status']
        response_action = response['action']
        # 期待的结果
        except_title = '请假'
        except_name = 'leave.create'
        except_text = circle['text']
        except_userId = '11634'
        except_status = 'CHECK_ONE'
        # except_action = '[{ "name": "base.jump", "title": "跳过"}, {"name": "base.leave", "title": "离开"}]'
        # except_selectItems = "[['284', '带薪事假-初始化'], ['1', '事假'], ['286', '事假-初始化'], ['2', '病假'], ['3', '婚假'], ['5',
        # " \ "'哺乳假'], ['133', '福利年假']," \ " ['7', '产假及看护假'], ['8', '哺乳假'], ['9', '丧假'], ['10', '带薪事假']]" 添加至allure
        allure.attach(str(request), '返回内容', allure.attachment_type.JSON)
        # 断言
        assert response_title == except_title, "意图title不同，期望：%s，实际：%s" % (except_title, response_title)
        assert response_name == except_name, "意图name不同，期望：%s，实际：%s" % (except_name, response_name)
        assert response_text == except_text, "语音纠错前后不同，期望：%s，实际：%s" % (except_text, response_text)
        assert response_userId == except_userId, "发送请求者的userId不同，期望：%s，实际：%s" % (except_userId, response_userId)
        assert response_status == except_status, "意图动作不同，期望：%s，实际：%s" % (except_status, response_status)
        # assert response_action == except_action, "action，期望：%s，实际：%s" % (except_action, response_action)

    @allure.story('考勤管理>请假>撤回请假')
    @pytest.mark.parametrize('circle', attendance_leave_recall)
    def test_attendance_leave_recall(self, circle):
        # 请求接口并获取返回的data
        request = request_get_ceshi(circle['text'])
        response = json.loads(request['data'])
        # 接口返回的值
        response_title = response['intentInfo']['title']
        response_name = response['intentInfo']['name']
        response_text = response['text']
        response_userId = response['userId']
        response_status = response['status']
        # 期待的结果
        except_title = '撤回请假'
        except_name = 'attendance_leave_recall'
        except_text = circle['text']
        except_userId = '11634'
        except_status = 'FINISH'
        # 添加至allure
        allure.attach(str(request), '返回内容', allure.attachment_type.JSON)
        # 断言
        assert response_title == except_title, "意图title不同，期望：%s，实际：%s" % (except_title, response_title)
        assert response_name == except_name, "意图name不同，期望：%s，实际：%s" % (except_name, response_name)
        assert response_text == except_text, "语音纠错前后不同，期望：%s，实际：%s" % (except_text, response_text)
        assert response_userId == except_userId, "发送请求者的userId不同，期望：%s，实际：%s" % (except_userId, response_userId)
        assert response_status == except_status, "意图动作不同，期望：%s，实际：%s" % (except_status, response_status)

    @allure.story('考勤管理>请假>查询请假制度')
    @pytest.mark.parametrize('circle', attendance_leave_query_system)
    def test_attendance_leave_query_system(self, circle):
        # 请求接口并获取返回的data
        request = request_get_ceshi(circle['text'])
        response = json.loads(request['data'])
        # 接口返回的值
        response_title = response['intentInfo']['title']
        response_name = response['intentInfo']['name']
        response_text = response['text']
        response_userId = response['userId']
        response_status = response['status']
        response_action = response['invoker']['action']
        # 期待的结果
        except_title = '查询请假制度'
        except_name = 'attendance_leave_query.system'
        except_text = circle['text']
        except_userId = '11634'
        except_status = 'FINISH'
        except_action = 'url:https://test.ai.easst.cn/easst/faq/execute_easst?method=faq'
        # 添加至allure
        allure.attach(str(request), '返回内容', allure.attachment_type.JSON)
        # 断言
        assert response_title == except_title, "意图title不同，期望：%s，实际：%s" % (except_title, response_title)
        assert response_name == except_name, "意图name不同，期望：%s，实际：%s" % (except_name, response_name)
        assert response_text == except_text, "语音纠错前后不同，期望：%s，实际：%s" % (except_text, response_text)
        assert response_userId == except_userId, "发送请求者的userId不同，期望：%s，实际：%s" % (except_userId, response_userId)
        assert response_status == except_status, "意图动作不同，期望：%s，实际：%s" % (except_status, response_status)
        assert response_action == except_action, "URL不同，期望：%s，实际：%s" % (except_action, response_action)

    @allure.story('考勤管理>假期额度')
    @pytest.mark.parametrize('circle', report_vacation)
    def test_report_vacation(self, circle):
        # 请求接口并获取返回的data
        request = request_get_ceshi(circle['text'])
        response = json.loads(request['data'])
        # 接口返回的值
        response_title = response['intentInfo']['title']
        response_name = response['intentInfo']['name']
        response_text = response['text']
        response_userId = response['userId']
        response_status = response['status']
        response_action = response['invoker']['action']
        # 期待的结果
        except_title = '假期额度'
        except_name = 'report.vacation'
        except_text = circle['text']
        except_userId = '11634'
        except_status = 'FINISH'
        except_action = 'url:/mobile/plugin/siri/ajaxApi.jsp?method=report_vacation'
        # 添加至allure
        allure.attach(str(request), '返回内容', allure.attachment_type.JSON)
        # 断言
        assert response_title == except_title, "意图title不同，期望：%s，实际：%s" % (except_title, response_title)
        assert response_name == except_name, "意图name不同，期望：%s，实际：%s" % (except_name, response_name)
        assert response_text == except_text, "语音纠错前后不同，期望：%s，实际：%s" % (except_text, response_text)
        assert response_userId == except_userId, "发送请求者的userId不同，期望：%s，实际：%s" % (except_userId, response_userId)
        assert response_status == except_status, "意图动作不同，期望：%s，实际：%s" % (except_status, response_status)
        assert response_action == except_action, "URL不同，期望：%s，实际：%s" % (except_action, response_action)

    @allure.story('考勤管理>考勤报表')
    @pytest.mark.parametrize('circle', report_attendance)
    def test_report_attendance(self, circle):
        # 请求接口并获取返回的data
        request = request_get_ceshi(circle['text'])
        response = json.loads(request['data'])
        # 接口返回的值
        response_title = response['intentInfo']['title']
        response_name = response['intentInfo']['name']
        response_text = response['text']
        response_userId = response['userId']
        response_status = response['status']
        response_action = response['invoker']['action']
        # 期待的结果
        except_title = '考勤报表'
        except_name = 'report.attendance'
        except_text = circle['text']
        except_userId = '11634'
        except_status = 'FINISH'
        except_action = 'url:/mobile/plugin/siri/ajaxApi.jsp?method=report_attendance'
        # 添加至allure
        allure.attach(str(request), '返回内容', allure.attachment_type.JSON)
        # 断言
        assert response_title == except_title, "意图title不同，期望：%s，实际：%s" % (except_title, response_title)
        assert response_name == except_name, "意图name不同，期望：%s，实际：%s" % (except_name, response_name)
        assert response_text == except_text, "语音纠错前后不同，期望：%s，实际：%s" % (except_text, response_text)
        assert response_userId == except_userId, "发送请求者的userId不同，期望：%s，实际：%s" % (except_userId, response_userId)
        assert response_status == except_status, "意图动作不同，期望：%s，实际：%s" % (except_status, response_status)
        assert response_action == except_action, "URL不同，期望：%s，实际：%s" % (except_action, response_action)

    @allure.story('考勤管理>加班>申请加班')
    @pytest.mark.parametrize('circle', attendance_work_overtime_apply)
    def test_attendance_work_overtime_apply(self, circle):
        # 请求接口并获取返回的data
        request = request_get_ceshi(circle['text'])
        response = json.loads(request['data'])
        # 接口返回的值
        response_title = response['intentInfo']['title']
        response_name = response['intentInfo']['name']
        response_text = response['text']
        response_userId = response['userId']
        response_status = response['status']
        # 期待的结果
        except_title = '申请加班'
        except_name = 'attendance_work.overtime_apply'
        except_text = circle['text']
        except_userId = '11634'
        except_status = 'FINISH'
        # 添加至allure
        allure.attach(str(request), '返回内容', allure.attachment_type.JSON)
        # 断言
        assert response_title == except_title, "意图title不同，期望：%s，实际：%s" % (except_title, response_title)
        assert response_name == except_name, "意图name不同，期望：%s，实际：%s" % (except_name, response_name)
        assert response_text == except_text, "语音纠错前后不同，期望：%s，实际：%s" % (except_text, response_text)
        assert response_userId == except_userId, "发送请求者的userId不同，期望：%s，实际：%s" % (except_userId, response_userId)
        assert response_status == except_status, "意图动作不同，期望：%s，实际：%s" % (except_status, response_status)