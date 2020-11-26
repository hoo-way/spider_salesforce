

# coding=utf8
import io
import sys
from colorama import Fore


# below info need to update when token invalid
cookies='BrowserId=VPHDFrtBEeq4Bi31bvH4jQ; BrowserId_sec=VPHDFrtBEeq4Bi31bvH4jQ; __utma=209274637.406119823.1593576334.1596161742.1596439289.6; __utmz=209274637.1596439289.6.4.utmcsr=silabs.com|utmccn=(referral)|utmcmd=referral|utmcct=/community/wireless/z-wave/forum.topic.html/multi_channel_commandencapsulationhowtointerp-08QS; AMCV_E5F28BE15673EFA87F000101%40AdobeOrg=870038026%7CMCIDTS%7C18569%7CMCMID%7C79371758837705876332516812146828012363%7CMCAAMLH-1604885025%7C11%7CMCAAMB-1604885025%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1604287425s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.0.0%7CMCCIDH%7C1427417421; mbox=PC#1e1d2881da874662a331dd9b97cf6a00.38_0#1667525030|session#49394c7c08f24a1dbc9XXXXXXXXXXX sid_Client=M000007zvqZ0000000L2kI; clientSrc=218.255.149.34; inst=APP_1M; sfdc-stream=!S/KnW2E/h1z2zmVh7vHMPURbmQUELkxI2AN2TGOJboiNxFNDClkmb+cczUfvNOFI9CJjkEsCkm8pdSs=; force-proxy-stream=!lZQ46U8V83cvG9eqDPTwLetG9KgXuvmbbduj5bKGqB/11LUkRBlBiNiT74nSjXYpMxfCihW718Jl/tg=; force-stream=!S/KnW2E/h1z2zmVh7vHMPURbmQUELkxI2AN2TGOJboiNxFNDClkmb+cczUfvNOFI9CJjkEsCkm8pdSs=; sid=00DA0000000L2kI!AQMAQBT55hzpL398tYhN19soW0nXbCCGzTwwDmDGmolwJmVJC3Hg8xmO1I1Pgqu4xlNQ07_R0PXMo.bUJctFulMcY7cZIw85'

token = 'eyJub25jZSI6ImEwZXMyN082TjFUZW1sY09tT3ptSkFjZk1DX1BURVVhVThUYUJzbUxMbjhcdTAwM2QiLCJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImtpZCI6IntcInRcIjpcIjAwRDE2MDAwMDAwTkZZQ1wiLFwidlwiOlwiMDJHMU0wMDAwMDBEOWxpXCIsXCJhXCI6XCJjYWltYW5zaWduZXJcIn0iLCJjcml0IjpbImlhdCJdLCJpYXQiOjE1OTUyMDM5ODIwNjEsImV4cCI6MH0=..zd1taN5KZLGpS_N_8zJR9LYSbWLhKz_NgLyr9usV69g='

loadID='Vb1ZsrqgswXUHT9OdA_hBw'

fwuid = 'dDIdorNC3N22LalQ5i3slQ'


# below info need to update for the first time

userID='0051M00000XXXXXX'


take_list =[
    {
        "queueName":"MCU",                # queue name
        "queueID":'00B1M000009ZmXSUA0',   # queue ID that you find in a
        "take_region": 'APAC',            # the region that you want to
        "take_number":[],          # mantissa number of case num
        "display_color":Fore.GREEN        # the color for printing log
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