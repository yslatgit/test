from urllib import parse
import requests

# #执行API调用并存储响应
# url = 'https://www.baidu.com'
# r = requests.get(url)
#
# print()

# import requests
# import json
#
# host = "http://httpbin.org/"
# endpoint = "get"
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
# # url = ''.join([host,endpoint])
# params = {"env":"1"}
# proxies = {"httsp":"http://114.223.161.32:8118"}
# # r = requests.get(host+'/get',headers=headers,params=params,proxies=proxies)
# data = {"user":"ysl","passwd":"123456"}
# files = {"file":open("bomb.png","rb")}
# r = requests.post(host+'/post',proxies=proxies)
# response = r.json()
#
#
# # print (eval(r.text)['headers']['User-Agent'])
# # print(eval(r.text))
# # print(response["args"])
# print(r.json())
import requests

# proxies = {
#   "http": "http://user:pass@219.238.186.188:8118/"
# }
proxies = {"http":"http://219.238.186.188:8118/"}
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
r = requests.post("http://httpbin.org/post", proxies=proxies,verify=False)
print (r.json())