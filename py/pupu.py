import requests
import time
import random


# 获取数据
def Get_json(url, headers):
    req = requests.get(url=url, headers=headers).json().get('data')
    return req


# 处理数据
def screen(req):
    price = float(req.get('price')) / 100
    data = {'name': req.get('name'),  # 商品名称
            'spec': req.get('spec'),  # 商品含量
            'price': str(price),  # 价格
            'content': req.get('share_content')  # 详细信息
            }
    return data


# 实时监控商品价格
def time_lapse(url, headers):
    var = 1
    while var == 1:  # 无限循环实现动态
        r = random.randint(1, 10)  # 设置随机1~10秒
        price = Get_json(url, headers).get('price')  # 获取数据
        time.sleep(r)  # 延时
        results = "当前时间为：" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ",价格为" + str(
            float(price) / 100)  # 显示结果
        print(results)


if __name__ == '__main__':
    # 头部信息，用来模拟浏览器发送请求
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip;q=1.0, compress;q=0.5',
        'Accept-Language': 'zh-Hans-CN;q=1.0',
        'User-Agent': 'Pupumall/2.9.0;iOS 14.4;D7CC2F22-7AA0-47B9-991E-44B33EA43CE6',
        'Connection': 'Keep-Alive',
        'Host': 'j1.pupuapi.com'
    }
    # json文件路径
    url = "https://j1.pupuapi.com/client/product/storeproduct/detail/deef1dd8-65ee-46bc-9e18-8cf1478a67e9/8485818c-d2aa-4885-9bf6-ad9aba8bca1d"
    # 存储json内容输出
    data = screen(Get_json(url, headers))
    print("------------------商品:" + data['name'] + "------------------")
    print("规格:" + data['spec'])
    print("价格:" + data['price'])
    print("详细内容：" + data['content'])
    # 实时监控商品价格
    print("------------------\"" + data['name'] + "\"的价格波动" "------------------")
    time_lapse(url, headers)