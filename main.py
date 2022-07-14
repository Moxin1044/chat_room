import requests
import socket
import os
# import urllib3
# import json
# import base64
import time
# import sys
# import calendar
# from urllib.parse import quote, unquote

url = "http://192.168.31.59:8880/"
name = "末心"
ip = socket.gethostbyname(socket.gethostname())
sleep_time = 10


def send_request(send_data):
    headers = {
        'Cookie': 'check='+ip
    }
    post_data = {
        "a": name,
        "b": send_data
    }
    response = requests.request("POST", url+"core.php", headers=headers, data=post_data, verify=False)
    print(response.text)


# 读聊天日志
def rdata():
    response = requests.request("GET", url+"data.cht", verify=False)
    print(response.text)


# 刷新
def refresh():
    # 由于刷新时容易导致输入未完成，暂不提供 或后期改成修改字符的方式
    # time.sleep(sleep_time)
    rdata()
    foot()


def exit_chat():
    send_request("|-- 此设备已下线 ↓ --|")


def foot():
    ta = input("您>>>:")
    if ta == "exit()":
        exit()
    elif ta == "refresh()":
        refresh()
    else:
        send_request(ta)
    l = os.system(r'cls')
    # os.system("clear")
    loops()


def loops():
    rdata()
    foot()


def main():
    send_request("|-- 新设备上线 请注意核实当前IP --|")
    print("""
 ██████╗██╗  ██╗ █████╗ ████████╗
██╔════╝██║  ██║██╔══██╗╚══██╔══╝
██║     ███████║███████║   ██║   
██║     ██╔══██║██╔══██║   ██║   
╚██████╗██║  ██║██║  ██║   ██║   
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   Ver: 1.0.0
                                 By : M0x1n
    """)
    loops()


main()
