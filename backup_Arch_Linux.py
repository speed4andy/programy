#!/usr/bin/env python
import os
import datetime
import sys
import time
import tarfile
import shutil
import smtplib

from email.mime.text import MIMEText

dest = os.path.join("/backup/")
bckp_file = dest + "backup_machine22" + '_' + ".tar.bz2"
mailout = []
path = "/backup"

if os.path.exists(path) == True:
    shutil.rmtree(path)
    os.mkdir(path)
    tar_out = tarfile.open(bckp_file, "w:bz2")
    try:
        tar_out.add('/etc', '/root', '/home/walle/*****')
        tar_out.add('/home/walle/Desktop', '/opt', '/boot')
        tar_out.add('/home/walle/.thunderbird/', '/home/walle/******')
    finally:
        tar_out.close()
else:
    os.mkdir(path)
    tar_out = tarfile.open(bckp_file, "w:bz2")
    try:
        tar_out.add('/etc', '/root', '/home/walle/.ssh')
        tar_out.add('/home/walle/Desktop', '/opt', '/boot')
        tar_out.add('/home/walle/.thunderbird/', '/home/walle/*******')
    finally:
        tar_out.close()

cmd1 = "mount.cifs -o username=ondrej.valcik,password=************ //192.168.X.X/install/temp/ondra/backup/ /mnt/share/"

cmd2 = "rsync -az /backup/backup_machine22_.tar.bz2 /mnt/share/"

cmd3 = "umount /mnt/share/"


os.system(cmd1)

os.system(cmd2)

os.system(cmd3)




mailout.append("Zaloha uzivatele ondrej.valcik stroje machine22 BYLA DOKONCENA")

pro = ["valcik@*****.com"]
od = "machine22@*****.com"

msg = MIMEText('\n'.join(mailout),"plain", "utf-8")
msg['Subject'] = "Zaloha machine22"
msg['From'] = od
msg['To'] = " ,".join(pro)



s = smtplib.SMTP('mail.******.com')
s.sendmail(od, pro, msg.as_string())
s.quit()
