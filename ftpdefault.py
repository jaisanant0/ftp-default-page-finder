import ftplib
from socket import*

def defpage(stp) :
      try :
            dirlist = ftp.nlst()
      except:
            dirlist = []
            print("[-] Unable to find default pages on " + host + ' : ' + str(hostip))
            print("[-] Skipping ")
            return

      retlist=[]
      for file in dirlist :
            fn = file.lower()
            if '.asp' in fn or '.html' in fn or '.php' in fn or '.htm' in fn :
                  print("[+] Found default pages : " + file)
                  retlist.append(file)
      return retlist




print("Enter the vulnerable host :")
host=str(input())
print("Enter the username found :")
user=str(input())
print("Enter the password found :")
password=str(input())

hostip=gethostbyname(host)
ftp=ftplib.FTP(str(hostip))
ftp.login(user,password)

defpage(ftp)
