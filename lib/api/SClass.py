import requests
from hytest import INFO
from cfg.cfg import *
import json


def getFirstClass():
    # 获取第一个班级的信息
    r = sclass.list_class()
    listRet = r.json()
    # {'name': '实验二班', 'grade__name': '八年级', 'invitecode': '202563130374', 'studentlimit': 50, 'studentnumber': 0, 'id': 20256, 'teacherlist': []}
    return listRet['retlist'][0]


class SClass:

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

    def add_class(self, grade, classname, studentlimit):
        INFO('添加班级')
        response = requests.post(g_api_url_class,
                               data={
                                   "vcode": g_vcode,
                                   "action": "add",
                                   "grade": gradeToId[grade],
                                   "name": classname,
                                   "studentlimit": studentlimit
                               })
        self._printResponse(response)
        return response

    def list_class(self, grade=None):
        INFO("列出班级")
        params = {
            "vcode": g_vcode,
            "action": "list_classes_by_schoolgrade"
        }
        if grade is not None:
            params["gradeid"] = gradeToId[grade]
        response = requests.get(g_api_url_class, params=params)
        self._printResponse(response)
        return response

    def del_class(self, classid):
        INFO("删除班级")
        response = requests.delete(f'{g_api_url_class}/{classid}', data={"vcode": g_vcode})
        self._printResponse(response)
        return response

    def del_allclasses(self):
        INFO("删除所有班级")
        r = self.list_class()
        for info in r.json()["retlist"]:
            classid = info["id"]
            response = requests.delete(f'{g_api_url_class}/{classid}', data={"vcode": g_vcode})
            self._printResponse(response)

    def modify_class(self, classid, name=None, studentlimit=None):
        INFO("修改班级")
        data = {
            "vcode": g_vcode,
            "action": "modify",
        }
        if name is not None:
            data["name"] = name
        if studentlimit is not None:
            data["studentlimit"] = studentlimit
        response = requests.put(f'{g_api_url_class}/{classid}', data=data)
        self._printResponse(response)
        return response


sclass = SClass()

