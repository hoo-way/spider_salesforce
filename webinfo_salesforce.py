

# coding=utf8
import io
import sys


# below info need to update when token invalid
cookies='_mkto_trk=id:183-SCJ-412&token:_mch-force.com-1567649028733-67629; hideFilesWarningModal=true; BrowserId=3uQHRValEeqcKa8XEUKe8Q; BrowserId_sec=3uQHRValEeqcKa8XEUKe8Q; sid_Client=M000007zvqZ0000000L2kI; inst=APP_1M; check=true; AMCV_E5F28BE15673EFA87F000101%40AdobeOrg=1278862251%7CMCIDTS%7C18331%7CMCMID%7C61792657137586292790305158558945919155%7CMCAAMLH-1584327401%7C11%7CMCAAMB-1584327401%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1583729801s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.0.0; AMCVS_E5F28BE15673EFA87F000101%40AdobeOrg=1; __utmc=209274637; __utmz=209274637.1583722602.36.30.utmcsr=silabs.com|utmccn=(referral)|utmcmd=referral|utmcct=/community/wireless/z-wave/forum.topic.html/flashed_applicationsoftwareforzgm130snolonger-K2I8; __utma=209274637.965676012.1567649032.1583458950.1583722602.36; mbox=PC#0adbf2cb8c9a46119f1c9f9efb334e53.22_0#1646967403|session#0d5b6501b2104676a4db0b50754990d5#1583724462; s_cc=true; s_sq=siliconlabssharepointlive%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fsiliconlabs.force.com%25252Fidp%25252Flogin%25253Fapp%25253D0sp16000000PBKn%2526link%253DLog%252520in%2526region%253Dsfsso-form-div%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fsiliconlabs.force.com%25252Fidp%25252Flogin%25253Fapp%25253D0sp16000000PBKn%2526oid%253Dfunctiononclick%252528event%252529%25257BreturnA4J.AJAX.Submit%252528%252527j_id0%25253Aform%252527%25252Cevent%25252C%25257B%252527similarityGroupingId%252527%25253A%252527j_id0%25253Aform%25253A%2526oidt%253D2%2526ot%253DSUBMIT; sfdc-stream=!zY7bpvsqlfzuW0DAQOcnoyyXkvKzr84zWOGJNtbEL6J3B/iFjpjrybgg/4+MU6MafH3WbYnim++sn2I=; force-proxy-stream=!tMV7D+gWfpZiWT5Bhw9D0vBUA1rV7wCIpvC1O5CRSQY0MEEZCGR1oYeEUuE/vkpJDeRVO+/PkHk7qqw=; force-stream=!zY7bpvsqlfzuW0DAQOcnoyyXkvKzr84zWOGJNtbEL6J3B/iFjpjrybgg/4+MU6MafH3WbYnim++sn2I=; sid=00DA0000000L2kI!AQMAQIDxiA9w7i3xjJ9XF1O9Co.2poPg5nIBvCQwO5xyN3rUqlhP0dDmctn4oLlwn7IGUznhWPlno0ew8UNEkkKuJCmjAYTR; clientSrc=185.114.76.123'

token = 'eyJub25jZSI6IkxJTVRaSVVzcm9hUTc1eVFDZ1QtZUdlajZQQkxRODlGSFZCUjBfLXZkem9cdTAwM2QiLCJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImtpZCI6IntcInRcIjpcIjAwRDE2MDAwMDAwTkZZQ1wiLFwidlwiOlwiMDJHMU0wMDAwMDBEOWxpXCIsXCJhXCI6XCJjYWltYW5zaWduZXJcIn0iLCJjcml0IjpbImlhdCJdLCJpYXQiOjE1ODQzMjI2NTgxMDEsImV4cCI6MH0=..m3SS31wWi8MXBpofGMTF8_NkMHVIQBY03Zpt4VxvGek='

loadID='k90Zxg82VnRcX3QEUFg-0g'


# below info need to update for the first time

queueID='00B1M000009ZmXSUA0'
userID='0051M000007zvqZQAQ'

take_list=['1','5']

def get_login_parameters():
    return cookies,token,loadID

def get_queueID():
    return queueID

def get_userID():
    return userID

def get_take_list():
    return take_list

def set_token(newtoken):
    token = newtoken