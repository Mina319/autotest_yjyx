import requests
from hytest import INFO
from cfg.cfg import *
import json


def getFirstTeacher():
    # 获取第一个老师的信息
    r = teacher.list_teacher()
    listRet = r.json()
    # {'username': 'sunny', 'teachclasslist': [20247], 'realname': '孙四', 'id': 5214, 'phonenumber': '13451812456', 'email': 'sunny@163.com', 'idcardnumber': '3208251983080987799'}
    return listRet['retlist'][0]


class Teacher:

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

    def add_teacher(self, username, realname, subjectid, classlist, phonenumber, email, idcardnumber):
        INFO('添加老师')
        response = requests.post(g_api_url_teacher,
                                 data={
                                     "vcode": g_vcode,
                                     "action": "add",
                                     "username": username,
                                     "realname": realname,
                                     "subjectid": subjectid,
                                     "classlist": json.dumps(classlist),  # 转为 JSON 字符串
                                     "phonenumber": phonenumber,
                                     "email": email,
                                     "idcardnumber": idcardnumber
                                 })
        self._printResponse(response)
        return response

    def list_teacher(self, subject=None):
        INFO("列出老师")
        params = {
            "vcode": g_vcode,
            "action": "search_with_pagenation"
        }
        if subject is not None:
            params["subjectid"] = subjectToId[subject]
        response = requests.get(g_api_url_teacher, params=params)
        self._printResponse(response)
        return response

    def modify_teacher(self, teacherid, realname=None, subjectid=None, classlist=None, phonenumber=None, email=None, idcardnumber=None):
        INFO("修改老师")
        data = {
            "vcode": g_vcode,
            "action": "modify",
        }
        if realname is not None:
            data["realname"] = realname
        if subjectid is not None:
            data["subjectid"] = subjectid
        if classlist is not None:
            data["classlist"] = json.dumps(classlist)
        if phonenumber is not None:
            data["phonenumber"] = phonenumber
        if email is not None:
            data["email"] = email
        if idcardnumber is not None:
            data["idcardnumber"] = idcardnumber
        response = requests.put(f'{g_api_url_teacher}/{teacherid}', data=data)
        self._printResponse(response)
        return response

    def del_teacher(self, teacherid):
        INFO("删除老师")
        response = requests.delete(f'{g_api_url_teacher}/{teacherid}', data={"vcode": g_vcode})
        self._printResponse(response)
        return response

    def del_allteachers(self):
        INFO("删除所有老师")
        r = self.list_teacher()
        for info in r.json()["retlist"]:
            teacherid = info["id"]
            response = requests.delete(f'{g_api_url_teacher}/{teacherid}', data={"vcode": g_vcode})
            self._printResponse(response)


teacher = Teacher()
