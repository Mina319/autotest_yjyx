import requests
from hytest import INFO
from cfg.cfg import *


def getFirstClass():
    # 获取第一个班级的id
    r = sclass.list_class()
    listRet = r.json()
    return listRet['retlist'][0]['id']


class SClass:

    def _printResponse(self, response):
        INFO('\n\n-------- HTTP response * begin -------')
        INFO(response.status_code)

        for k, v in response.headers.items():
            INFO(f'{k}: {v}')
        INFO('')

        body = response.content.decode('utf8')
        INFO(body)

        try:
            response.json()
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


sclass = SClass()


