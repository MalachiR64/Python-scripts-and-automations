# Website Blocker

- A Python script to block access to specified websites on Window and Mac devices. It acomplishes this by manipulating the host file.

## Table of Contents
- [How It Works](#how-it-works)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Notes](#notes)
- [Future Improvements](#future-improvements)
- [Contributors](#contributors)

## How It Works
 - The script works by modifying the host file on the specified operating system. It redirects the specified websites to the local loopback address (127.0.0.1), effectively blocking access to those sites

## Prerequisites

- Make sure you have Python installed on your system. Additionally, install the required module:

```bash
pip install pyuac
```
## Usage
1. Define Websites to Block: Open the script and modify the `site_to_block` list with the websites you want to block.
    * write the website's full name with and without `www.` at the front

```python
site_to_block = ['www.example.com', 'example.com']
```
2. Specify Host File Path:
    * For MacOS, set the hostPathM variable.
    * For Windows, set the hostPathW variable.
```python
# For MacOS
hostPathM = r"/etc/hosts"

# For Windows
hostPathW = r"C:\Windows\System32\drivers\etc\hosts"

# Use the appropriate host path based on the operating system
hostPath = hostPathW  # Change this to hostPathM if on MacOS

```
3. Run the Script:
    * If not already running as an administrator, the script will relaunch itself with administrative privileges.

    * The script will check the current time against the endTime variable. If the current time is before endTime, it will block the specified websites; otherwise, it will unblock them.


## Notes
- Make sure to adjust the `hostPath` variable to the correct path of the host file on your system.

## Future improvements 
- The script should be run periodically to maintain blocking/unblocking functionality.

## Contributors
- Malachi Rosario