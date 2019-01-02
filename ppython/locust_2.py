import requests

#获取全网职位得到接口
url_d = 'https://mobile-application.mofanghr.com/member/wholeNetworkJob/search.json?params=' \
        '{"page":0,"size":15,"sortType":"smart","cityCode":"864401","text":"专员","defaultCityCode":"8611"}'

r = requests.get(url_d)
print(r.cookies)
ck_dict = requests.utils.dict_from_cookiejar(r.cookies)
print(ck_dict)
# print(r.json())