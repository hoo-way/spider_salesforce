"# spider_salesforce" 

Make sure you log into the saleforce and stop in the queue you want
# Climbing web info
* click F12 to enter chrome debug mode, choose NetWork tab and clean all log in window.
* Fresh queue (Not F5)
# Find cookies, token and loadID
* After fresh, you will find a item in debug window, choose it. You will find all kinds of paramter in Header tab.
* Please find 3 important parameter in headers.

Please see the picture below to know how to get cookies.
![cookies](./img/02.png)

Please see the picture below to know how to get loadID and token.
![token](./img/03.png)
# Find Queue id, user id
Queue id can be found in your link address, such as https://siliconlabs.lightning.force.com/lightning/o/Case/list?filterName=00B1M0000096zClUAI
"00B1M0000096zClUAI" is the queue id.

User id can be found it your user page.
![token](./img/04.png)

# Fill up paramter into python file
Open configuration.py and fill up the 5 paramters above.

# Add take rule to take_list
take_list is a python array, you need to add a or several take rule to this array. The rule struct is below.
```
take_list =[
    {
        "queueName":"MCU",               # queue name
        "queueID":'00B1M000009ZmXSUA0',  # queue ID that you find in above step
        "take_region": 'APAC',           # the region that you want to take
        "take_number":['1','5'],         # mantissa number of case number
        "display_color":Fore.GREEN       # the color for printing log
    }
]
```
If you want to monitor multi queue, configure it as below.
```
take_list =[
    {
        "queueName":"ZZZ",               # queue name
        "queueID":'ZZZZZZZZZZZZ',  # queue ID that you find in above step
        "take_region": 'APAC',           # the region that you want to take
        "take_number":['1','5'],         # mantissa number of case number
        "display_color":Fore.GREEN       # the color for printing log
    },
    {
        "queueName":"XXX",               # queue name
        "queueID":'XXXXXXXXXXX',  # queue ID that you find in above step
        "take_region": 'APAC',           # the region that you want to take
        "take_number":['1','5'],         # mantissa number of case number
        "display_color":Fore.GREEN       # the color for printing log
    },
    {
        "queueName":"YYY",               # queue name
        "queueID":'YYYYYYYYYY',  # queue ID that you find in above step
        "take_region": 'APAC',           # the region that you want to take
        "take_number":['1','5'],         # mantissa number of case number
        "display_color":Fore.GREEN       # the color for printing log
    }
]
```


# Start run
python start_spider

# Note
* If the spider run correctly, it will output the caputure result. When the case number in take_list and belong to APAC, the case will be assigned to you by spider.
![token](./img/05.png)
* Spider caputre the case info every 1 minute
* We can log into salesforce since we feed it cookies(include token and loadID)  from chrome, the cookies has life cycle, about 2-3 days. That means you may need to feed them again after the cookies became invalid.

Please contact me if it can't work on your side

Welcome add more feature to the code to make it more friendly.