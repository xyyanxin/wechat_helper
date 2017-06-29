#! /user/bin/env python3.4
# -*- coding: utf-8 -*-
# Date: 2017-06-10
# Author: xy

import datetime
import time
import itchat
from itchat.content import TEXT, MAP, CARD, NOTE, SHARING


@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    print(msg.type)
    print(msg.text)
    if msg.text == 'f=10':
        interval_time = 1*60
        msg.user.send('时间频率已更改为{interval_time}分'.format(
            interval_time=interval_time/60))


def find_user_name(name):
    friendList = itchat.get_friends(update=True)
    for index, user in enumerate(friendList):
        if name in user['RemarkName']\
                or name in user['DisplayName']\
                or name in user['NickName']:
            return friendList[index]['UserName']


def job_test():
    print('start func job test')
    target_user = find_user_name('xy')
    hello_msg = 'hello xy(from xy_helper)'
    itchat.send(hello_msg, toUserName=target_user)


def job_drink():
    print('start func job drink')
    bella_name = find_user_name()
    _msg = '美女,到时间喝水了!(from xy_secretary)'
    itchat.send(_msg, toUserName=bella_name)


def job_wake():
    bella_name = find_user_name()
    _msg = '美女,该起床了(from xy_secretary)'
    itchat.send(_msg, toUserName=bella_name)


def main():
    itchat.auto_login(hotReload=True)
    job_test()
    #while True:
    #    now = datetime.datetime.now()
    #    if 7 <= now.hour < 8\
    #            and 30 <= now.minute <= 50:
    #        job_wake()
    #        time.sleep(5*60)


if __name__ == '__main__':
    main()
