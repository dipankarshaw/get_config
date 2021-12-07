# get_config
The code takes the commands from commands text file & fires show commands on the set of nodes mentioned under hostname file.
Then it saves those outputs in a folder created with the current timestamp - > node wise -> command wise.
Used multi theading to fasten the collection.
note : Currently the code assumes that your target node is iosxr.

# Sample use
dshaw@ubuntu-box:~/get_config$ ls -lrt
total 16
-rw-r--r-- 1 dshaw dshaw 2190 Dec  8 00:08 cisco_ios_netmiko.py
-rw-r--r-- 1 dshaw dshaw   26 Dec  8 00:08 commands.txt
-rw-r--r-- 1 dshaw dshaw   26 Dec  8 00:09 hostname.txt
-rw-r--r-- 1 dshaw dshaw  243 Dec  8 00:22 README.md

dshaw@ubuntu-box:~/get_config$ cat hostname.txt 
sandbox-iosxr-1.cisco.com
dshaw@ubuntu-box:~/get_config$ cat commands.txt 
show version
show platform

dshaw@ubuntu-box:~/get_config$ python3 cisco_ios_netmiko.py 
Enter username : admin
Enter Password : 
***** connected to sandbox-iosxr-1.cisco.com
**** Program Ended, get the outputs at : /home/dshaw/get_config/2021_12_07_185513Z
dshaw@ubuntu-box:~/get_config$ ls -lrt
total 20
-rw-r--r-- 1 dshaw dshaw 2190 Dec  8 00:08 cisco_ios_netmiko.py
-rw-r--r-- 1 dshaw dshaw   26 Dec  8 00:08 commands.txt
-rw-r--r-- 1 dshaw dshaw   26 Dec  8 00:09 hostname.txt
-rw-r--r-- 1 dshaw dshaw  355 Dec  8 00:25 README.md
drwxr-xr-x 3 dshaw dshaw 4096 Dec  8 00:25 2021_12_07_185513Z
dshaw@ubuntu-box:~/get_config$ cd 2021_12_07_185513Z/
dshaw@ubuntu-box:~/get_config/2021_12_07_185513Z$ ls -lrt
total 4
drwxr-xr-x 2 dshaw dshaw 4096 Dec  8 00:25 sandbox-iosxr-1_cisco_com
dshaw@ubuntu-box:~/get_config/2021_12_07_185513Z$ cd sandbox-iosxr-1_cisco_com/
dshaw@ubuntu-box:~/get_config/2021_12_07_185513Z/sandbox-iosxr-1_cisco_com$ ls -lrt
total 8
-rw-r--r-- 1 dshaw dshaw 548 Dec  8 00:25 sandbox-iosxr-1_cisco_com_show_version.txt
-rw-r--r-- 1 dshaw dshaw 416 Dec  8 00:25 sandbox-iosxr-1_cisco_com_show_platform.txt
dshaw@ubuntu-box:~/get_config/2021_12_07_185513Z/sandbox-iosxr-1_cisco_com$