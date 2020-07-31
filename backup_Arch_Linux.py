#!/usr/bin/env python
import os 
import datetime
import sys
import time
import tarfile
import shutil
import smtplib
import getpass
import socket

from email.mime.text import MIMEText

dest = os.path.join("/backup/")
bckp_file = dest + "backup_" + socket.gethostname() + '_' + ".tar.bz2"
mailout = []
path = "/backup"

if os.path.exists(path) == True:
    shutil.rmtree(path)

username = os.getlogin()
os.mkdir(path)
tar_out = tarfile.open(bckp_file, "w:bz2")
try:
    tar_out.add('/etc', '/home/' + username + '/.ssh')
    tar_out.add('/home/' + username + '/Desktop')
    tar_out.add('/home/' + username + '/.thunderbird/')
finally:
    tar_out.close()

cmd1 = "mount.cifs -o username=ondrej.valcik,password=*********** //192.168.XXX.XXX/install/temp/ondra/ /mnt/share/"

cmd2 = "rsync -az /backup/backup_" + socket.gethostname() + "_.tar.bz2 /mnt/share/"

cmd3 = "umount /mnt/share/"


os.system(cmd1)
 
os.system(cmd2)
   
os.system(cmd3)




mailout.append("Zaloha uzivatele " + username + " stroje " + socket.gethostname() + " BYLA DOKONCENA")

pro = ["valcik@proebiz.com"]
od = "backup@proebiz.com"

msg = MIMEText('\n'.join(mailout),"plain", "utf-8")
msg['Subject'] = "Zaloha " + socket.gethostname()
msg['From'] = od
msg['To'] = " ,".join(pro)



s = smtplib.SMTP('mail.proebiz.cz')
s.sendmail(od, pro, msg.as_string())
s.quit()
