#coded by : Ravularohit
#github :https://github.com/ravularohit/
#Instagram :@Ravularohit

import optparse
import subprocess


def process(inter,mac):
    subprocess.call(["ifconfig", inter, "down", "hw", "ether", mac])
    subprocess.call(["ifconfig", inter, "up"])
    print("[+] mac changed to " + mac)


def input():
    p = optparse.OptionParser()
    p.add_option("-i", "--interface", dest="inter", help="Interface to which mac should be changed")
    p.add_option("-m", "--mac", dest="mac", help="custom mac input")
    (opt,arg)= p.parse_args()
    if not opt.inter:
        p.error("\033[1;31;40m[-] please specify the interface, use -h,--help for more info")
    elif not opt.mac:
        p.error("\033[1;31;40m[-] please specify the custom mac, use -h,--help for more info")
        return opt


intro=(''''########:::::::'####:::::::'########::
 ##.... ##:::::'##. ##:::::: ##.... ##:
 ##:::: ##:::::. ####::::::: ##:::: ##:
 ########::::::'####:::::::: ########::
 ##.. ##::::::'##. ##'##:::: ##.. ##:::
 ##::. ##::::: ##:. ##:::::: ##::. ##::
 ##:::. ##::::. ####. ##:::: ##:::. ##:
..:::::..::::::....::..:::::..:::::..::
\033[1;32;40mCoded by @Ravularohit :
''')
subprocess.call("clear")
print(intro)
opt=input()
process(opt.inter,opt.mac)