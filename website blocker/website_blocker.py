from datetime import datetime
import pyuac

endTime = datetime()

# type the website to block
#site_to_block = ['www.WebsiteName','WebsiteName' ]
site_to_block = []

#for mac
hostPathM= r"/etc/host"

#for Windows
hostPathW= r"C:\Windows\System32\drivers\etc\hosts"

hostPath = hostPathW

redirect = "127.0.0.1"

def block_sites():
    if datetime.now() < endTime:
        print("block sites")
        with open(hostPath, 'r+') as hostsfile:
            host_content= hostsfile.read()
            for site in site_to_block:
                if site not in host_content:
                    hostsfile.write(redirect + " " + site + "\n")
    else:
        print("unblock sites") 
        with open(hostPath, 'r+') as hostsfile:
            lines = hostsfile.readlines()
            hostsfile.seek(0)
            for line in lines:
                if not any(site in line for site in site_to_block):
                    hostsfile.write(line)
            hostsfile.truncate()

if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        print("Re-launching as admin!")
        pyuac.runAsAdmin()
    
   
    else:
        block_sites()