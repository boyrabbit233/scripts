#!/usr/bin/env python3
#conding=utf-8
import requests,json,sys

def get_tenant_access_token():
    tokenurl = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/"
    headers = {"Content-Type":"application/json"}
    data = {
        "app_id": "xxxxxxxxxxxxxxx",
        "app_secret": "xxxxxxx"

    }
    request = requests.post(url=tokenurl, headers=headers, json=data)
    response = json.loads(request.content)['tenant_access_token']
    return response

def get_userid(tenant_access_token):
    userurl = "https://open.feishu.cn/open-apis/contact/v3/users/batch_get_id?user_id_type=open_id"
    data = {
        "mobiles": [
            "XXXXXXXXXX"
        ]
    }
    headers = {
        'Content-Type': 'application/json',
        "Authorization": "Bearer %s" %tenant_access_token
    }
    request = requests.post(url=userurl, data=json.dumps(data), headers=headers)
    response = json.loads(request.content)['data']['user_list'][0]['user_id']
    #print("user_id: ", response)
    return response

def get_chatid(tenant_access_token):
    #获取chatid
    chaturl = "https://open.feishu.cn/open-apis/im/v1/chats?page_size=20"
    headers = {"Authorization":"Bearer %s"%tenant_access_token,"Content-Type":"application/json"}
    request = requests.get(url=chaturl,headers=headers)
    response = json.loads(request.content)['data']['items'][0]['chat_id']
    print('chat_id: ', response)
    return response

def send_messages(user_id,chat_id,tenant_access_token):
    #向群里发送消息
    sendurl = "https://open.feishu.cn/open-apis/im/v1/messages"
    params = {"receive_id_type": "chat_id"}
    headers = {"Authorization": "Bearer %s"%tenant_access_token,"Content-Type":"application/json"}
    msgContent = {
        'text': '%s <at user_id=\"%s\">test</at>' %(MESSAGES, user_id)
    }
    data = {
        'receive_id': chat_id,
        'msg_type': 'text',
        'content': json.dumps(msgContent)
    }
    #print(json.dumps(data))
    #print(type(json.dumps(data)))
    request = requests.post(url=sendurl, params=params, headers=headers, data=json.dumps(data))
    #print(request.content)

if __name__ == '__main__':
    USER = sys.argv[1]
    SUBJECT = sys.argv[2]
    MESSAGES = sys.argv[3]
    tenant_access_token = get_tenant_access_token()
    user_id = get_userid(tenant_access_token)
    chat_id = get_chatid(tenant_access_token)
    send_messages(user_id,chat_id,tenant_access_token)
