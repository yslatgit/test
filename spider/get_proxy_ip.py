import requests
import re
import random
import pymysql

proxy_ip = {}

def set_url():
    url = r'https://www.xicidaili.com/nn/'
    x = random.randint(0,20)
    if x == 0:
        return url
    else:
        return url+'%d'%x

# print(set_url())
def req(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
    }
    req = requests.get(url,headers=headers,verify=False)
    req = req.content.decode('utf-8')
    l_host = re.findall(r'<td>(\d+\.\d+\.\d+\.\d+)</td>', req)
    l_port = re.findall(r'<td>(\d+)</td>', req)
    for i in range(len(l_host)):
        proxy_ip[l_host[i]] = l_port[i]

def write_ip():
        with open('ip.txt','a+') as f:
            for k, v in proxy_ip.items():
                line = str(k) + ":" + str(v) + "\n"
                f.write(line)

def connect_mysql():
    conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='root',db='test',charset='utf8')
    cur = conn.cursor()
    # cur.execute('SELECT * FROM SpiderIp')
    # # cur.execute('select * from users')
    # res = cur.fetchall()
    # print(res)
    for k, v in proxy_ip.items():
        cur.execute('insert into SpiderIp VALUES ("%s","%s")'%(str(k),str(v)))
    conn.commit()
    cur.close()
    conn.close()


def mm():
    req(set_url())
    write_ip()

if __name__ == '__main__':
    req(set_url())
    connect_mysql()