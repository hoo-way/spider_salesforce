

# coding=utf8
import io
import sys
from colorama import Fore


# below info need to update when token invalid
cookies='XXX'

token = 'eyJub25jZSI6IkYxSTJ4bkFBbWpSNG5CRTRaTXdZd2tjNGV1UF9KU05reWxKMkxWczByOHNcdTAwM2QiLCJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImtpZCI6IntcInRcIjpcIjAwRDE2MDAwMDAwTkZZQ1wiLFwidlwiOlwiMDJHMU0wMDAwMDBEOWxpXCIsXCJhXCI6XCJjYWltYW5zaWduZXJcIn0iLCJjcml0IjpbImlhdCJdLCJpYXQiOjE1ODkyNDY3MTIwNjgsImV4cCI6MH0=..rJPaOeGbm8WAi6Vsk8NDJ_W8dmZ5BCzFPcWbA2s92gM='

loadID='N3fGLDWYoA_VSIS79dk8Fw'


# below info need to update for the first time

userID='0051M000007zvqZQAQ'


take_list =[
    {
        "queueName":"MCU",                # queue name
        "queueID":'00B1M000009ZmXSUA0',   # queue ID that you find in a
        "take_region": 'APAC',            # the region that you want to
        "take_number":['1','5'],          # mantissa number of case num
        "display_color":Fore.GREEN        # the color for printing log
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