#!/usr/bin/env python


import os
import pyinotify
import smtplib

from email.mime.text import MIMEText

wm = pyinotify.WatchManager()
mailout = []
mask = pyinotify.IN_CREATE

class EventHandler(pyinotify.ProcessEvent):
    def process_IN_CREATE(self, event):
        print ("Creating:", event.pathname)
        self.email_send()

    def email_send(self):
        mailout.append("Kamera zaznamenala pohyb v serverovne")
        pro = ["valcik@******.com"]
        od = "kamera@******.com"
        msg = MIMEText('\n'.join(mailout),"plain", "utf-8")
        msg['Subject'] = "monitoring22"
        msg['From'] = od
        msg['To'] = " ,".join(pro)
        s = smtplib.SMTP('mail.******.com')
        s.sendmail(od, pro, msg.as_string())
        s.quit()

handler = EventHandler()
notifier = pyinotify.Notifier(wm, handler)
wdd = wm.add_watch('/motion_pics/', mask, rec=True)

notifier.loop() 
