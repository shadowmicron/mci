try:
    import os
    import sys
    import time
    import urllib
    import platform
    import requests
except ImportError:
    os.system('pip2 install requests') #Module Not found Eror :(

def home(): #main menu
    os.system("clear")
    arm = platform.architecture()[0] #Checking arm
    print logo #raw
    print 47*("-")
    print('Your Device Is \033[0;92m'+arm).center(45)  #Show Raw
    print 47*("\033[0;97m-")
    baba("\tRunning => ")
    os.system("clear")
    print logo
    device = platform.architecture()[0]
    if device == '64bit':
        from librdx import xd_xd
        xd_xd()
    elif device == '32bit':
        os.system("clear")
        os.system("exit")
        os.system("cd $HOME") #Home 
        os.system("cat /data/data/com.termux/files/usr/etc/motd") # Show Termux Info Text 
        print("$ Your Device Has Been No Support :( ")
    else:
        os.system("clear")
        os.system("cat /data/data/com.termux/files/usr/etc/motd") # Show Termux Info Text 
        os.system("exit")

if __name__ == '__main__':
    home()
