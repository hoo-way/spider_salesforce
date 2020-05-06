

# coding=utf8
import io
import sys


# below info need to update when token invalid
cookies='hideFilesWarningModal=true; BrowserId=3uQHRValEeqcKa8XEUKe8Q; BrowserId_sec=3uQHRValEeqcKa8XEUKe8Q; _mkto_trk=id:634-SLU-379&token:_mch-force.com-1567649028733-67629; __utma=209274637.965676012.1567649032.1587697075.1587881110.45; __utmz=209274637.1587881110.45.37.utmcsr=silabs.com|utmccn=(referral)|utmcmd=referral|utmcct=/community/wireless/z-wave/forum.topic.html/application_codezgm130s-FgBH; AMCV_E5F28BE15673EFA87F000101%40AdobeOrg=1278862251%7CMCIDTS%7C18379%7CMCMID%7C61792657137586292790305158558945919155%7CMCAAMLH-1588485910%7C11%7CMCAAMB-1588485910%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1587888310s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.0.0; mbox=PC#0adbf2cb8c9a46119f1c9f9efb334e53.22_0#1651125911|session#a44e79ff204546c383c0d0e89acca3e1#1587882970; sfdc-stream=!sw4S5g4ZC8aLrtLAQOcnoyyXkvKzr3lfnWrpBSivLCRnUE448VPHVRFFzvJBR/xRDDk+XDFqfe2FDIw=; force-proxy-stream=!bh3Tt1xZZzYyjCS7MoQUKUk0cplVYhgh7uCgkm6eC2bOhPoQ/pYMw4X1KRcZW01RAIhsL2Be/bnevcU=; force-stream=!sw4S5g4ZC8aLrtLAQOcnoyyXkvKzr3lfnWrpBSivLCRnUE448VPHVRFFzvJBR/xRDDk+XDFqfe2FDIw=; sid=00DA0000000L2kI!AQMAQBTB.SqXGF6ZA_IQIm1PvtyBA0hJULX_J4A13yaOM08H9nOJWrWp2A5_Pg3Xxphhtx2NtB.uvkiqW_nu0pR1mX2nO9.T; sid_Client=M000007zvqZ0000000L2kI; clientSrc=58.251.52.66; inst=APP_1M'

token = 'eyJub25jZSI6InF3cTVhd2RWU1BUUGUzWlMyM0ZJTklfeG85aERvR1lOVE1IZ29WT2c0Vk1cdTAwM2QiLCJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImtpZCI6IntcInRcIjpcIjAwRDE2MDAwMDAwTkZZQ1wiLFwidlwiOlwiMDJHMU0wMDAwMDBEOWxpXCIsXCJhXCI6XCJjYWltYW5zaWduZXJcIn0iLCJjcml0IjpbImlhdCJdLCJpYXQiOjE1ODg3MjgzMzY0ODcsImV4cCI6MH0=..MHfVYYNlf2sZ3-SAPZXsr_zFAJUO7YO-V5oLMAE5rpw='

loadID='Kyn0wehQw3SSPh5ILpOmkg'


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