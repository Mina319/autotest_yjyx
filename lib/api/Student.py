import requests
from hytest import INFO
from cfg.cfg import *
import json


def getFirstStudent():
    # 获取第一个学生的信息
    r = student.list_student()
    listRet = r.json()
    # "classid": 19,"username": "lxz002","realname": "李钟硕33","phonenumber": "13433335569","id": 174
    return listRet['retlist'][0]


class Student:

    def _printResponse(self, response):
        INFO('\n\n-------- HTTP response * begin -------')
        INFO(response.status_code)

        for k, v in response.headers.items():
            INFO(f'{k}: {v}')
        INFO('')

        try:
            r = response.json()
            INFO(json.dumps(r, ensure_ascii=False, indent=2))
        except:
            INFO('消息体不是json格式！！！')
        INFO('-------- HTTP response * end -------\n\n')

    def add_student(self, username, realname, gradeid, classid, phonenumber):
        INFO('添加学生')
        response = requests.post(g_api_url_student,
                                 data={
                                     "vcode": g_vcode,
                                     "action": "add",
                                     "username": username,
                                     "realname": realname,
                                     "gradeid": gradeid,
                                     "classid": classid,
                                     "phonenumber": phonenumber,
                                 })
        self._printResponse(response)
        return response

    def list_student(self):
        INFO("列出学生")
        params = {
            "vcode": g_vcode,
            "action": "search_with_pagenation"
        }
        response = requests.get(g_api_url_student, params=params)
        self._printResponse(response)
        return response

    def modify_student(self, studentid, realname=None, subjectid=None, classlist=None, phonenumber=None, email=None, idcardnumber=None):
        INFO("修改学生")
        data = {
            "vcode": g_vcode,
            "action": "modify",
        }
        if realname is not None:
            data["realname"] = realname
        if phonenumber is not None:
            data["phonenumber"] = phonenumber
        response = requests.put(f'{g_api_url_student}/{studentid}', data=data)
        self._printResponse(response)
        return response

    def del_student(self, studentid):
        INFO("删除学生")
        response = requests.delete(f'{g_api_url_student}/{studentid}', data={"vcode": g_vcode})
        self._printResponse(response)
        return response

    def del_allstudents(self):
        INFO("删除所有学生")
        r = self.list_student()
        for info in r.json()["retlist"]:
            studentid = info["id"]
            response = requests.delete(f'{g_api_url_student}/{studentid}', data={"vcode": g_vcode})
            self._printResponse(response)


student = Student()
