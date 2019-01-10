import requests
import re

proxy_ip = {}

url = r'https://www.xicidaili.com/nn/'

url1 = r'http://www.baidu.com/'

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
}

response = requests.get(url,headers=headers,verify=False)

req = response.content

req = req.decode('utf-8')

l_host = re.findall(r'<td>(\d+\.\d+\.\d+\.\d+)</td>',req)
l_port = re.findall(r'<td>(\d+)</td>',req)

print(type(l_host))

print(len(l_host))

for i in range(len(l_host)):
    proxy_ip[l_host[i]] = l_port[i]


# print(l_host)
# print(l_port)
print(proxy_ip)
for k,v in proxy_ip.items():
    print(k,v)