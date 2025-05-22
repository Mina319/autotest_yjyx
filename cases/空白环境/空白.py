from hytest import CHECK_POINT, STEP
from lib.webapi import apimgr, getRetlist


class Case_0209:
    name = '修改客户-API-0209'

    def teststeps(self):
        STEP(1, '获取修改客户的ID')
        self.address, self.customerId, self.name1, self.phonenumber = getRetlist().values()
        STEP(2, '修改客户:修改name与已经存在的一样')
        r = apimgr.customer_modify(self.customerId, name='武汉市桥西医院1')
        addRet = r.json()
        print('addRet----', addRet)
        expected = {
                    "ret": 1,
                    "msg": "客户名已经存在"
                }

        CHECK_POINT('返回的ret值=1', addRet == expected)

        STEP(2, '检查系统数据')
        r = apimgr.customer_list(2, 1)
        listRet = r.json()

        retlist = []
        cid = self.customerId
        for i in range(2, 0, -1):
            ele = {}
            ele['address'] = f'武汉市桥西医院北路{i}'
            ele['id'] = cid
            ele['name'] = f'武汉市桥西医院{i}'
            ele['phonenumber'] = f'133456799{i:02d}'
            cid -= 1
            retlist.append(ele)
        expected = {
            "ret": 0,
            "retlist": retlist,
            'total': 2
        }
        print('expected----', expected)
        print('listRet----', listRet)

        CHECK_POINT('返回的消息体数据正确，未成功修改', listRet == expected)

    def teardown(self):
        # 无论用例是否失败，都将name修改回来
        apimgr.customer_modify(self.customerId, name=self.name1)
