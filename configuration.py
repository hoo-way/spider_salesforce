

# coding=utf8
import io
import sys
from colorama import Fore


# below info need to update when token invalid
cookies='BrowserId=VPHDFrtBEeq4Bi31bvH4jQ; BrowserId_sec=VPHDFrtBEeq4Bi31bvH4jQ; AMCV_E5F28BE15673EFA87F000101%40AdobeOrg=-432600572%7CMCIDTS%7C18478%7CMCMID%7C79371758837705876332516812146828012363%7CMCAAMLH-1597044089%7C11%7CMCAAMB-1597044089%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1596446489s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.5.2; __utma=209274637.406119823.1593576334.1596161742.1596439289.6; __utmz=209274637.1596439289.6.4.utmcsr=silabs.com|utmccn=(referral)|utmcmd=referral|utmcct=/community/wireless/z-wave/forum.topic.html/multi_channel_commandencapsulationhowtointerp-08QS; mbox=PC#1e1d2881da874662a331dd9b97cf6a00.38_0#1659684441|session#52d6b45b902b4334ab0e3c558ad6203c#1596441149; force-proxy-stream=!774NDFeB0NaAEn5Bhw9D0vBUA1rXXXXXXXXXXXXXXXXXQVkstcCbd82HqU5ySiPyCE5F3iGoQV1+mIofZh6N4=; sid=00DA0000000L2kI!AQMAQD.b5d5IoybrItuRbMm62IyIf_1MjbENP.7M_HVO7uIvG0Kv1X1AGdc8.0RZ43tmYlJW05suBUKTjg.8gE7aX6IrXfBV; sid_Client=M000007zvqZ0000000L2kI; clientSrc=58.251.52.66; inst=APP_1M; sfdc-stream=!fM5vHzlfMZxSaU7AQOcnoyyXkvKzr6N2vOchIES74adMxYkTU2YzoAJ5AS22KJEbAD44E8qtRxLNnDk=; force-stream=!fM5vHzlfMZxSaU7AQOcnoyyXkvKzr6N2vOchIES74adMxYkTU2YzoAJ5AS22KJEbAD44E8qtRxLNnDk='

token = 'eyJub25jZSI6ImEwZXMyN082TjFUZW1sY09tT3ptSkFjZk1DX1BURVVhVThUYUJzbUxMbjhcdTAwM2QiLCJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImtpZCI6IntcInRcIjpcIjAwRDE2MDAwMDAwTkZZQ1wiLFwidlwiOlwiMDJHMU0wMDAwMDBEOWxpXCIsXCJhXCI6XCJjYWltYW5zaWduZXJcIn0iLCJjcml0IjpbImlhdCJdLCJpYXQiOjE1OTUyMDM5ODIwNjEsImV4cCI6MH0=..zd1taN5KZLGpS_N_8zJR9LYSbWLhKz_NgLyr9usV69g='

loadID='rrX_aoKklPQoCHzWNkkcew'

fwuid = 'axnV2upVY_ZFzdo18txAEw'


# below info need to update for the first time

userID='0051M000007zvqZQAQ'


take_list =[
    {
        "queueName":"MCU",                # queue name
        "queueID":'00B1M000009ZmXSUA0',   # queue ID that you find in a
        "take_region": 'APAC',            # the region that you want to
        "take_number":['1','5','7'],          # mantissa number of case num
        "display_color":Fore.GREEN        # the color for printing log
    },
     {
        "queueName":"Unspecified Part Support Team",
        "queueID":'00B16000008q3F5EAI',
        "take_region": 'ANY', # regardless region
        "take_number":[],
        "display_color":Fore.MAGENTA
    },
    {
        "queueName":"Z-Wave",
        "queueID":'00B1M000009ZU7RUAW',
        "take_region": 'APAC',
        "take_number":['0','1','2','3','4','5','6','7','8','9'],
        "display_color":Fore.BLUE
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