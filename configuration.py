

# coding=utf8
import io
import sys
from colorama import Fore


# below info need to update when token invalid
cookies='hideFilesWarningModal=true; BrowserId=3uQHRValEeqcKa8XEUKe8Q; BrowserId_sec=3uQHRValEeqcKa8XEUKe8Q; _mkto_trk=id:634-SLU-379&token:_mch-force.com-1567649028733-67629; __utma=209274637.965676012.1567649032.1587697075.1587881110.45; __utmz=209274637.1587881110.45.37.utmcsr=silabs.com|utmccn=(referral)|utmcmd=referral|utmcct=/community/wireless/z-wave/forum.topic.html/application_codezgm130s-FgBH; AMCV_E5F28BE15673EFA87F000101%40AdobeOrg=1278862251%7CMCIDTS%7C18379%7CMCMID%7C61792657137586292790305158558945919155%7CMCAAMLH-1588485910%7C11%7CMCAAMB-1588485910%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1587888310s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.0.0; mbox=PC#0adbf2cb8c9a46119f1c9f9efb334e53.22_0#1651125911|session#a44e79ff204546c383c0d0e89acca3e1#1587882970; sid_Client=M000007zvqZ0000000L2kI; inst=APP_1M; sfdc-stream=!NeLYiqtPtfRD+Mu4FiSGFaVC4w8+OSTbMp//JWAhnhhwJJFnzgCJbdanIku3jOJ5ELdZLR0dN8LIGCg=; force-proxy-stream=!MGoutUU9m6prh1S4FiSGFaVC4w8+OV5JlXEn3ZLR1R//GTlTII4AuwD2Wy+q/rG/YIJ+jfOGGlhPyy4=; force-stream=!NeLYiqtPtfRD+Mu4FiSGFaVC4w8+OSTbMp//JWAhnhhwJJFnzgCJbdanIku3jOJ5ELdZLR0dN8LIGCg=; sid=00DA0000000L2kI!AQMAQJjUO.cgnV2qNFn0rXEy9NtHcbzW7A2mVrMFXlR3UCkRkdlQCcUgsicOenONp5SgLw468fulSPgoh6Gv.iE_Xz3bMe9N; clientSrc=183.178.58.198'

token = 'eyJub25jZSI6IkYxSTJ4bkFBbWpSNG5CRTRaTXdZd2tjNGV1UF9KU05reWxKMkxWczByOHNcdTAwM2QiLCJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImtpZCI6IntcInRcIjpcIjAwRDE2MDAwMDAwTkZZQ1wiLFwidlwiOlwiMDJHMU0wMDAwMDBEOWxpXCIsXCJhXCI6XCJjYWltYW5zaWduZXJcIn0iLCJjcml0IjpbImlhdCJdLCJpYXQiOjE1ODkyNDY3MTIwNjgsImV4cCI6MH0=..rJPaOeGbm8WAi6Vsk8NDJ_W8dmZ5BCzFPcWbA2s92gM='

loadID='N3fGLDWYoA_VSIS79dk8Fw'


# below info need to update for the first time

userID='0051M000007zvqZQAQ'


take_list =[
    {
        "queueName":"MCU",
        "queueID":'00B1M000009ZmXSUA0',
        "take_region": 'APAC',
        "take_number":['1','5'],
        "display_color":Fore.GREEN
    },
     {
        "queueName":"Unspecified Part Support Team",
        "queueID":'00B16000008q3F5EAI',
        "take_region": 'ANY', # regardless region
        "take_number":['1','5'],
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
    return cookies,token,loadID

def get_queueID():
    return take_list[0]["queueID"]

def get_userID():
    return userID

def get_take_list():
    return take_list

def set_token(newtoken):
    token = newtoken