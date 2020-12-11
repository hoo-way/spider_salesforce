

# coding=utf8
import io
import sys
from colorama import Fore


# below info need to update when token invalid
cookies='BrowserId=VPHDFrtBEeq4Bi31bvH4jQ; BrowserId_sec=VPHDFrtBEeq4Bi31bvH4jQ; __utma=209274637.406119823.1593576334.1596161742.1596439289.6; __utmz=209274637.1596439289.6.4.utmcsr=silabs.com|utmccn=(referral)|utmcmd=referral|utmcct=/community/wireless/z-wave/forum.topic.html/multi_channel_commandencapsulationhowtointerp-08QS; force-proxy-stream=!5M8QDzT54slGNmps50U4m8uGC1eOhA51bl51cbRWV/H5hSu/cnNw+UNKanbGtWaZxLHsNpMqx/LVHm8=; sid_Client=M000007zvqZ0000000L2kI; inst=APP_1M; check=true; mbox=PC#1e1d2881da874662a331dd9b97cf6a00.38_0#1670831328|session#6ad7e978acf64710bf5e9ad0b6a9e20a#1607588388; AMCVS_E5F28BE15673EFA87F000101%40AdobeOrg=1; AMCV_E5F28BE15673EFA87F000101%40AdobeOrg=-637568504%7CMCIDTS%7C18606%7CMCMID%7C79371758837705876332516812146828012363%7CMCAAMLH-1608191327%7C11%7CMCAAMB-1608191327%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1607593727s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.1.1%7CMCCIDH%7C1427417421; s_cc=true; s_sq=siliconlabssharepointlive%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fsiliconlabs.force.com%25252Fidp%25252Flogin%25253Fapp%25253D0spG0000000006s%252526RelayState%25253DENxCJjf5za8DWNs-HF_CYPhH%252526binding%25253DHttpRedirect%252526inresponseto%25253Did7d25c708c92d41fbb859a68134b693eb%2526link%253DLog%252520in%2526region%253Dsfsso-form-div%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fsiliconlabs.force.com%25252Fidp%25252Flogin%25253Fapp%25253D0spG0000000006s%252526RelayState%25253DENxCJjf5za8DWNs-HF_CYPhH%252526binding%25253DHttpRedirect%252526inresponseto%25253Did7d25c708c92d41fbb859a68134b693eb%2526oid%253Dfunctiononclick%252528event%252529%25257BreturnA4J.AJAX.Submit%252528%252527j_id0%25253Aform%252527%25252Cevent%25252C%25257B%252527similarityGroupingId%252527%25253A%252527j_id0%25253Aform%25253A%2526oidt%253D2%2526ot%253DSUBMIT; sfdc-stream=!MSiXqcI/VFdMdpiwkPnUOC7ljB6IIExE3D+02sNibKbEKx9qYxf1dE3A92BhJGdwF5dwudwaxhH7L1U=; force-stream=!MSiXqcI/VFdMdpiwkPnUOC7ljB6IIExE3D+02sNibKbEKx9qYxf1dE3A92BhJGdwF5dwudwaxhH7L1U=; sid=00DA0000000L2kI!AQMAQL4MZX9UgiEm9ROchB3Yve9K7T3u9PX7pLfXKRm7.vN3yzz9ynCN.BBLm0E93sPuvnkTc34StzydkWi4l5CnJ3onGPP3; clientSrc=59.149.170.3'

token = 'eyJub25jZSI6ImEwZXMyN082TjFUZW1sY09tT3ptSkFjZk1DX1BURVVhVThUYUJzbUxMbjhcdTAwM2QiLCJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImtpZCI6IntcInRcIjpcIjAwRDE2MDAwMDAwTkZZQ1wiLFwidlwiOlwiMDJHMU0wMDAwMDBEOWxpXCIsXCJhXCI6XCJjYWltYW5zaWduZXJcIn0iLCJjcml0IjpbImlhdCJdLCJpYXQiOjE1OTUyMDM5ODIwNjEsImV4cCI6MH0=..zd1taN5KZLGpS_N_8zJR9LYSbWLhKz_NgLyr9usV69g='

loadID='XX'

fwuid = 'XX'


# below info need to update for the first time

userID='XXXXX'

take_list =[
    {
        "queueName":"MCU",                # queue name
        "queueID":'00B1M000009ZmXSUA0',   # queue ID that you find in a
        "take_region": 'APAC',            # the region that you want to
        "take_number":[],          # mantissa number of case num
        "display_color":Fore.LIGHTGREEN_EX        # the color for printing log
    },
    {
        "queueName":"BLE",                # queue name
        "queueID":'00B1M0000096usJUAQ',   # queue ID that you find in a
        "take_region": 'APAC',            # the region that you want to
        "take_number":[],          # mantissa number of case num
        "display_color":Fore.BLUE        # the color for printing log
    },
    {
        "queueName":"ZigBee",                # queue name
        "queueID":'00B1M0000096usLUAQ',   # queue ID that you find in a
        "take_region": 'APAC',            # the region that you want to
        "take_number":['9'],          # mantissa number of case num
        "display_color":Fore.LIGHTRED_EX       # the color for printing log
    },
    # {
    #     "queueName":"Unspecified Part Support Team",
    #     "queueID":'00B16000008q3F5EAI',
    #     "take_region": 'ANY', # regardless region
    #     "take_number":[],
    #     "display_color":Fore.MAGENTA
    # },
    {
        "queueName":"Z-Wave",
        "queueID":'00B1M000009ZU7RUAW',
        "take_region": 'APAC',
        "take_number":['0','1','2','3','4','5','6','7','8','9'],
        "display_color":Fore.LIGHTBLUE_EX
    }
]

def get_login_parameters():
    return cookies,token,loadID,fwuid

def get_queueID():
    return take_list[0]["queueID"]

def get_userID():
    return userID

def get_take_list():
    return take_list

def set_token(newtoken):
    token = newtoken