import pytest
from yaml_util import read_yaml
import requests
class Test_api:
    @pytest.mark.parametrize("data",read_yaml('test.yml'))
    def test_weather(self,data):
        # print(data)
        # print(data['name'])
        # print(data['request']['url'])
        # print(data['request']['method'])
        # print(data['request']['data'])
        # print(data['validate'])
        res=requests.get(data['request']['url'],data['request']['data'])
        return_value=res.json()
        #print(res.text) #文本字符串
        print(return_value) #json格式

        #处理断言
        for key,value in dict(data['validate']).items():
            if key=='eq':
                for assert_key,assert_value in dict(value).items():
                    if return_value[assert_key]==assert_value:
                        #print(return_value[assert_key],assert_value)
                        print("断言成功")
                    else:
                        print("断言失败")
            else:
                print("不支持的断言方式")

if __name__=='__main__':
    pytest.main(['-vs'])