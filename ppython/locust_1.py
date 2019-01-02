import requests
import json
import time
# url =  "https://mobile-application.mofanghr.com/member/wholeNetworkJob/search.json"
# cookie = {"auth_token":"d8a2579e0b09f4ab93dada0a697556103d8345141ce45fb736ec93a37a6ed67e5dc9011253ec4df39d6dff5b485836af",
#            "session":"eyJzb3VyY2UiOnsiIGIiOiJhRFU9In19.DwjEAw.3k0UzYU5I-GSwmBSTebobqZlD-Y"}
# #            # "cookie_info":"0f0386335290edf3809d2ea622b206adda46430ca38244da4a95ddac7ab76ffa"}
# # param = {"param":{"page":0,"size":15,"sortType":"smart","cityCode":"864401","text":"专员","defaultCityCode":"8611"}}
# cookie = json.dumps(cookie)
# headers = {"Cookie":cookie}

# headers = {"Cookie":"auth_token=efd80c6c4a6299b4ea760ee783837c1a69536036da020b27495c2d446dc52f7887ff206341ee5191a7dda8d6b6eb148f;"
#                     " refresh_time=1546074332170; cookie_info=0f0386335290edf3809d2ea622b206adda46430ca38244da4a95ddac7ab76ffa; "
#                     "session=.eJyrVirOLy1KTlWyqlZSSFKyUkp0CbVVqtVRKi1OLYrPTFGyyivNyYFy8xJzUyECtQAEhRLv.DwjKXA.d_0ytRMuhn6lgi4DepbI5_Wjacs"}

headers = {"Cookie":"auth_token=efd80c6c4a6299b4ea760ee783837c1a69536036da020b27495c2d446dc52f7887ff206341ee5191a7dda8d6b6eb148f;"
                    " refresh_time=1546074332170; cookie_info=0f0386335290edf3809d2ea622b206adda46430ca38244da4a95ddac7ab76ffa; "
                    "session=.eJyrVirOLy1KTlWyqlZSSFKyUkp0CbVVqtVRKi1OLYrPTFGyyivNyYFy8xJzUyECtQAEhRLv.DwjKXA.d_0ytRMuhn6lgi4DepbI5_Wjacs"}

headerss = {"Cookie":"auth_token=d5221be373651a480086bc39ee5e7729a2a2150e3a1a76097f42cbca1ecd5935a03ba16a5e0d779c2a04608212fc5fd5; refresh_time=1546077823291; cookie_info=bae4f3f8239cb998288da2567512eaa34952e17e273ecae7a79ebd48bef227a3; session=.eJyrVirOLy1KTlWyqlZSSFKyUkp0CbVVqtVRKi1OLYrPTFGyyivNyYFy8xJzUyECtQAEhRLv.DwjX_w.GOghKlBopVlFTeOIVdF-mX55rlY"}
# print(r)
# r = r.json()
# joblist = r['data']['resultList']
# # print(joblist[0])
# print(len(joblist))
# for i in joblist:
#     if i['jobSourceDesc'] in['智联','前程']:
#         print(i)
#投递的参数
# params: {"accountSource":"3","jobID":"CZ698370520J00096773814","companyID":"f0b351560fd519f2"}

# https://i.mofanghr.com/job-detail?jobID=CZ815217520J00276450101&companyID=1ec37a19e6a04f7b&accountSource=3
#投递的接口
url_zhilian = 'https://mobile-application.mofanghr.com/member/outside/loginByCookieAndDelivery.json?params=' \
              '{"accountSource":"3","jobID":"CZ404930730J00152825202","companyID":"daa0122dc3846082"}'
# try:
    # requests.get('https://i.mofanghr.com/job-detail?jobID=CZ815217520J00276451701&companyID=1ec37a19e6a04f7b&accountSource=3')

    # time.sleep(1)
r = requests.get(url_zhilian,headers=headerss,timeout=20)
print(r.json())
# except Exception as msg:
#     print(msg)

# {"Cookie":"auth_token=efd80c6c4a6299b4ea760ee783837c1a69536036da020b27495c2d446dc52f7887ff206341ee5191a7dda8d6b6eb148f; refresh_time=1546074332170; cookie_info=0f0386335290edf3809d2ea622b206adda46430ca38244da4a95ddac7ab76ffa; session=.eJyrVirOLy1KTlWyqlZSSFKyUkp0CbVVqtVRKi1OLYrPTFGyyivNyYFy8xJzUyECtQAEhRLv.DwjKXA.d_0ytRMuhn6lgi4DepbI5_Wjacs"}