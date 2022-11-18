#This easy program was written to help me backup my LINUX machine with move tared file to another destination feel free to modify this code if you notice some issues/bugs

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

dest = os.path.join("/home/"+ getpass.getuser() +"/backup/")
bckp_file = dest + "backup_" + socket.gethostname() + '_' + ".tar.bz2"
mailout = []
path = "/home/"+ getpass.getuser() +"/backup"

if os.path.exists(path) == True:
    shutil.rmtree(path)

username = os.getlogin()
os.mkdir(path)
tar_out = tarfile.open(bckp_file, "w:bz2")

#BELOW ADD WHAT NEEDS TO BE BACKED UP

try:
   #tar_out.add("/home/"+ getpass.getuser() +"")
    tar_out.add("/home/"+ getpass.getuser() +"/.ssh")
finally:
    tar_out.close()

#BELOW IS PROCESS OF MOUNTING FS AND DESTINATION  
    
cmd1 = "mount.cifs -o username=oval22,password=*********** //192.168.XXX.XXX/install/temp/ondra/ /mnt/share/"

cmd2 = "rsync -az /backup/backup_" + socket.gethostname() + "_.tar.bz2 /mnt/share/"

cmd3 = "umount /mnt/share/"


os.system(cmd1)
 
os.system(cmd2)
   
os.system(cmd3)


#SENDING EMAIL ABOUT BACKUP WAS DONE

mailout.append("Zaloha uzivatele " + username + " stroje " + socket.gethostname() + " BYLA DOKONCENA")

pro = ["oval22@XYZ.com"]
od = "backup@XYZ.com"

msg = MIMEText('\n'.join(mailout),"plain", "utf-8")
msg['Subject'] = "Zaloha " + socket.gethostname()
msg['From'] = od
msg['To'] = " ,".join(pro)



s = smtplib.SMTP('mail.XYZ.com')
s.sendmail(od, pro, msg.as_string())
s.quit()
