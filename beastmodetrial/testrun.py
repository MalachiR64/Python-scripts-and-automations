from datetime import datetime
import pyuac

endTime = datetime(2024,10,10,20)

# type the website to block
site_to_block = ['www.smashkarts.io','smashkarts.io' ]

#hostPathM= r"/etc/host"
hostPathW= r"C:\Windows\System32\drivers\etc\hosts"

redirect = "127.0.0.1"

def block_sites():
    if datetime.now() < endTime:
        print("block sites")
        with open(hostPathW, 'r+') as hostsfile:
            host_content= hostsfile.read()
            for site in site_to_block:
                if site not in host_content:
                    hostsfile.write(redirect + " " + site + "\n")
    else:
        print("unblock sites") 
        with open(hostPathW, 'r+') as hostsfile:
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
    
    #1. run manually
    #2. cron job
    #
    else:
        block_sites()