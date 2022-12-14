# !/usr/bin/env python3
# _*_ encoding:utf-8 _*_

import sys
import requests
import time

JOB_URL = sys.argv[1]
JOB_NAME = sys.argv[2]
BUILD_NUMBER = sys.argv[3]
#GIT_BRANCH = sys.argv[4]
STATUS = sys.argv[4]
currenttime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
url = 'https://open.feishu.cn/open-apis/bot/v2/hook/xxxxxxxxxxxxxxxxxxxxxxxxx'
method = 'post'
headers = {
    'Content-Type': 'application/json'
}

def set_header(STATUS):
    if STATUS == 'success':
        header = {
        "template": "green",
        "title": {
          "content": "ðã " + JOB_NAME + " æå»ºæåã",
          "tag": "plain_text"
          }
        }
    elif STATUS == 'failed':
        header = {
        "template": "red",
        "title": {
          "content": "ð¡ã " + JOB_NAME + " æå»ºå¤±è´¥ã",
          "tag": "plain_text"
          }
        }
    return header

def alert():
    header = set_header(STATUS)
    json = {
        "msg_type": "interactive",
        "card": {
            "config": {
                "wide_screen_mode": True,
                "enable_forward": True
            },
            "elements": [{
                "tag": "div",
                "text": {
                    "content": "é¡¹ç®åç§°ï¼" + JOB_NAME + "\næå»ºç¼å·ï¼ç¬¬" + BUILD_NUMBER + "æ¬¡æå»º\nå®ææ¶é´ï¼" + currenttime + "\n",
                    "tag": "lark_md"
                }
            },{
                "actions": [{
                    "tag": "button",
                    "text": {
                        "content": "æ¥çæ¥å",
                        "tag": "lark_md"
                    },
                    "url": JOB_URL,
                    "type": "default",
                    "value": {}
                }],
                "tag": "action"
            }],
            "header": header
        }
    }
    requests.request(method=method, url=url, headers=headers, json=json)

if __name__ == '__main__':
    alert()
