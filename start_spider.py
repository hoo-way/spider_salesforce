# coding=utf8
# update 2020.01.01 ,--victor

import io
import sys
import requests
import json
import time
import configuration
from datetime import datetime
from colorama import Fore,Back,Style
import colorama

#  https://siliconlabs.lightning.force.com/aura?r=5&ui-force-components-controllers-lists-listViewDataManager.ListViewDataManager.getItems=1&ui-force-components-controllers-lists-listViewManagerGrid.ListViewManagerGrid.getRecordLayoutComponent=1

# cookies=''

# token = 'eyJub25jZSI6IkxJTVRaSVVzcm9hUTc1eVFDZ1QtZUdlajZQQkxRODlGSFZCUjBfLXZkem9cdTAwM2QiLCJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImtpZCI6IntcInRcIjpcIjAwRDE2MDAwMDAwTkZZQ1wiLFwidlwiOlwiMDJHMU0wMDAwMDBEOWxpXCIsXCJhXCI6XCJjYWltYW5zaWduZXJcIn0iLCJjcml0IjpbImlhdCJdLCJpYXQiOjE1ODQzMjI2NTgxMDEsImV4cCI6MH0=..m3SS31wWi8MXBpofGMTF8_NkMHVIQBY03Zpt4VxvGek='

# loadID=''
# queueID='00B1M000009ZmXSUA0'
# userID='0051M000007zvqZQAQ'
# take_list=['1','5']

cookies, token,loadID = configuration.get_login_parameters()

queueID = configuration.get_queueID()
userID = configuration.get_userID()

take_list = configuration.get_take_list()


# print len(take_list)
# for take in take_list:
#     print take["queueName"]
#     print take["queueID"]
#     print take["take_number"]

#     if '0' in take["take_number"]:
#         print "yes"
#     else:
#         print "false"

# Do NOT touch the code below

# header = {
#     "Host": "siliconlabs.lightning.force.com",
#     "origin": "https://siliconlabs.lightning.force.com",
#     "Referer": "https://siliconlabs.lightning.force.com/lightning/o/Case/list?filterName="+queueID,
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
#     'Cookie': cookies
# }

postUrl = "https://siliconlabs.lightning.force.com/aura?r=62&ui-force-components-controllers-lists-listViewDataManager.ListViewDataManager.getItems=1&ui-force-components-controllers-lists-listViewManagerGrid.ListViewManagerGrid.getRecordLayoutComponent=1"

postData = {
    "message": '{"actions":[{"id":"51987;a","descriptor":"serviceComponent://ui.force.components.controllers.lists.listViewManagerGrid.ListViewManagerGridController/ACTION$getRecordLayoutComponent","callingDescriptor":"UNKNOWN","params":{"listReference":{"entityKeyPrefixOrApiName":"Case","listViewIdOrName":"'+queueID+'","inContextOfRecordId":null,"isMRU":false,"isSearch":false},"layoutType":"LIST","layoutMode":"EDIT","inContextOfComponent":"force:listViewManagerGrid","enableMassActions":true,"enableRowErrors":true,"useHoversForLookup":false}},{"id":"51990;a","descriptor":"serviceComponent://ui.force.components.controllers.lists.listViewDataManager.ListViewDataManagerController/ACTION$getItems","callingDescriptor":"UNKNOWN","params":{"filterName":"'+queueID+'","entityName":"Case","pageSize":50,"layoutType":"LIST","sortBy":null,"getCount":false,"enableRowActions":false,"offset":0},"storable":true}]}',
    "aura.context": '{"mode":"PROD","fwuid":"kHqYrsGCjDhXliyGcYtIfA","app":"one:one","loaded":{"APPLICATION@markup://one:one":"'+loadID+'"},"dn":[],"globals":{"eswConfigDeveloperName":null,"isVoiceOver":null,"setupAppContextId":null,"density":"VIEW_TWO","srcdoc":null,"appContextId":"06m1M000000KhjGQAS","dynamicTypeSize":null},"uad":true}',
    "aura.pageURI": '/lightning/o/Case/list?filterName='+queueID,
    "aura.token": token
}

takeUrl = 'https://siliconlabs.lightning.force.com/aura?r=368&ui-force-components-controllers-ownerChangeContent.OwnerChangeContent.performOwnerChange=1'

def update_postData(queueID_t):
    global postData
    global token
    global loadID
    postData = {
        "message": '{"actions":[{"id":"51987;a","descriptor":"serviceComponent://ui.force.components.controllers.lists.listViewManagerGrid.ListViewManagerGridController/ACTION$getRecordLayoutComponent","callingDescriptor":"UNKNOWN","params":{"listReference":{"entityKeyPrefixOrApiName":"Case","listViewIdOrName":"'+queueID_t+'","inContextOfRecordId":null,"isMRU":false,"isSearch":false},"layoutType":"LIST","layoutMode":"EDIT","inContextOfComponent":"force:listViewManagerGrid","enableMassActions":true,"enableRowErrors":true,"useHoversForLookup":false}},{"id":"51990;a","descriptor":"serviceComponent://ui.force.components.controllers.lists.listViewDataManager.ListViewDataManagerController/ACTION$getItems","callingDescriptor":"UNKNOWN","params":{"filterName":"'+queueID_t+'","entityName":"Case","pageSize":50,"layoutType":"LIST","sortBy":null,"getCount":false,"enableRowActions":false,"offset":0},"storable":true}]}',
        "aura.context": '{"mode":"PROD","fwuid":"kHqYrsGCjDhXliyGcYtIfA","app":"one:one","loaded":{"APPLICATION@markup://one:one":"'+queueID_t+'"},"dn":[],"globals":{"eswConfigDeveloperName":null,"isVoiceOver":null,"setupAppContextId":null,"density":"VIEW_TWO","srcdoc":null,"appContextId":"06m1M000000KhjGQAS","dynamicTypeSize":null},"uad":true}',
        "aura.pageURI": '/lightning/o/Case/list?filterName='+queueID_t,
        "aura.token": token
    }

# r=None
i=0
colorama.init(autoreset=True)
requests.adapters.DEFAULT_RETRIES = 5
s = requests.session()
s.keep_alive = False
while True:
    for take in take_list:
        header = {
            "Host": "siliconlabs.lightning.force.com",
            "origin": "https://siliconlabs.lightning.force.com",
            "Referer": "https://siliconlabs.lightning.force.com/lightning/o/Case/list?filterName="+take["queueID"],
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
            'Cookie': cookies
        }
        # print header
        try:
            update_postData(take["queueID"])
            r= requests.post(postUrl, data = postData, headers = header)
            status = r.status_code
        except requests.exceptions.ConnectionError:
            if status:
                print"Connection refused"
            else:
                status = "Connection refused"
            # if 'r' in dir() :
            #     print str(r.status_code)
            # else:
            #    pass
            # time.sleep(60)
        except Exception, e:
            print("status: "+str(status))
            print(e)
            continue
        # print type(status)
        # print r.content
        if status == 200:
            try:
                text2 = json.loads(r.content)
            except Exception, e:
                # if token valid, will print below so that we can update token
                #  */{"event":{"descriptor":"markup://aura:invalidSession","attributes":{"values":{"newToken":"eyJub25jZSI6InBPY3dTZUt2c0xqbXJ0QzF6VkoxX3ZvZVJfdS1QQU1BX2U1ekxBR1BMbjRcdTAwM2QiLCJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImtpZCI6IntcInRcIjpcIjAwRDE2MDAwMDAwTkZZQ1wiLFwidlwiOlwiMDJHMU0wMDAwMDBEOWxpXCIsXCJhXCI6XCJjYWltYW5zaWduZXJcIn0iLCJjcml0IjpbImlhdCJdLCJpYXQiOjE1ODQ1ODI4MTkzNDEsImV4cCI6MH0=..Yo9i8VNOyBzFzU8qZsAB5m9G2Dwfwx8yBKRaGc46jkg="}}},"exceptionEvent":true}/*ERROR*/
                print str(datetime.now().strftime('%Y-%m-%d %H:%M:%S '))
                newtoken_exist = r.content.find('newToken')
                if newtoken_exist > 0 and r.content.find('ey') > 0:
                    newtoken_start = newtoken_exist + 11
                    newtoken_end = r.content.find('"}}},')
                    token = r.content[newtoken_start:newtoken_end]
                    print("find new token: " + token)
                    update_postData(take["queueID"])
                    # print postData
                    continue
                else:
                    print str(e)  
                    print "---error content: " + r.content            
            else:
                # print text2["context"]["globalValueProviders"][6]["values"]["records"]
                # print text2["context"]["componentDefs"]["globalValueProviders"][5]
                # print text2["context"]["globalValueProviders"][5]["values"]
                # print text2["context"]["componentDefs"][0]["fa"][0].keys()
                length = len(text2["context"]["globalValueProviders"])
                # print length
                
                if length==7:  #len(text2["context"]["globalValueProviders"]) == 6 代表有case，等于5代表没有case
                    # print len(text2["context"]["globalValueProviders"][5]["values"]["records"]) # case amount
                    for key in text2["context"]["globalValueProviders"][6]["values"]["records"].keys():
                        # print key
                        case_number =text2["context"]["globalValueProviders"][6]["values"]["records"][key]["Case"]["record"]["fields"]["CaseNumber"]["value"] # case number, type:string
                        case_district= text2["context"]["globalValueProviders"][6]["values"]["records"][key]["Case"]["record"]["fields"]["District__c"]["value"] # district
                        print take["display_color"] + str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + " query ["+ take["queueName"]+"] for " + str(i) + " time: find case " + str(case_number) +' '+ str(case_district)
                        if (case_number[len(case_number)-1] in take["take_number"]) and (case_district == 'APAC'):
                            print Fore.RED + str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + " query ["+ take["queueName"]+"] for " + str(i) + " time: get case " + str(case_number) +' '+ str(case_district)
                            message_data = '{"actions":[{"id":"56925;a","descriptor":"serviceComponent://ui.force.components.controllers.ownerChangeContent.OwnerChangeContentController/ACTION$performOwnerChange","callingDescriptor":"UNKNOWN","params":{"recordIds":["' + key + '"],"newOwnerId":"'+userID+'","changeOwnerOptions":{"editableOptions":[{"label":"Send notification email","optionName":"SendEmail","isChecked":true,"isEditable":true,"isDisabled":false}],"nonEditableOptions":[{"label":"Notes and attachments","optionName":"TransferNotesAndAttachments","isChecked":true,"isEditable":false,"isDisabled":false},{"label":"Open activities","optionName":"TransferOpenActivities","isChecked":true,"isEditable":false,"isDisabled":false}],"qualifiedApiName":"Case","ownerFieldLabel":"Case Owner","ownerForeignKeyDomains":[{"name":"User","label":"User","labelPlural":"People","icon":"https://siliconlabs.my.salesforce.com/img/icon/t4v35/standard/user_120.png","color":"65CAE4"},{"name":"Group","label":"Queue","labelPlural":"Queues"}]},"doAccessCheck":false}}]}'
                            takeData = {
                                "message": message_data,
                                "aura.context": '{"mode":"PROD","fwuid":"kHqYrsGCjDhXliyGcYtIfA","app":"one:one","loaded":{"APPLICATION@markup://one:one":"'+loadID+'"},"dn":[],"globals":{"eswConfigDeveloperName":null,"isVoiceOver":null,"setupAppContextId":null,"density":"VIEW_TWO","srcdoc":null,"appContextId":"06m1M000000KhjGQAS","dynamicTypeSize":null},"uad":true}',
                                "aura.token":token
                                }
                            takeResponse= requests.post(takeUrl, data = takeData, headers = header)
                            takeResponse_status = takeResponse.status_code
                            print takeResponse_status
                            print takeResponse.content

                else:
                    print str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + " query ["+ take["queueName"]+"] for " + str(i) + " time: no case"
        else:
            print str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + " query ["+ take["queueName"]+"] for " + str(i) + " time: log in error--- status: "+str(status) +' '+ str(r.content)
    print '\n'
    i+=1
    time.sleep(60)
