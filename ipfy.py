#!/data/data/com.termux/files/bin/python
# Importing Modules \(o,,,o)/
import argparse
import requests, json
import sys
from sys import argv
import os
# Arguments *_*

parser = argparse.ArgumentParser()

parser.add_argument("-t", help="target ip address", type=str, dest='target', required=True)

args = parser.parse_args()

# I love Colors !
lightblue = '\033[94m'
lightgreen = '\033[92m'
clear = '\033[0m'
boldblue = '\033[01m''\033[94m'
cyan = '\033[36m'
bold = '\033[01m'
red = '\033[31m'
lightcyan = '\033[96m'
yellow = '\033[93m'
# Clear The Terminal
os.system('clear')
# Banner
print(bold+cyan+"""
1î1     1î1        11          1111111  1î1   11
1î1     1î1      111111       111       1î1  11
1î1111111î1    111   1111    1*1        1î111
1î1111111î1   111     1111   1*1        1î111
1î1     1î1  11-1111111-111  111        1î1 111
1î1     1î1  1111      1111   11111111  1î1  1111
===C==y==b==e==r==-==L==i==g==h==t==n==i==n==g===
                     For you
                No system IS SAVE
               CODE NAME:3T0$ C3N3L
                  -----IPFY-----
"""+clear)
print(lightcyan+bold+"[ Edited By ETOS Cenel ] | [Youtube.com/ETOS Cenel]\n"+clear)

ip = args.target
# Let's Begin
api = "http://ip-api.com/json/"
# Sending Requests And Getting Data
try:
        data = requests.get(api+ip).json()
        sys.stdout.flush()
        a = yellow+bold+"[~]"
        # Printing,Not Phising ; P
        print(a, "Target:", data['query'])
        print(a, "ISP:", data['isp'])
        print(a, "Organisation:", data['org'])
        print(a, "City:", data['city'])
        print(a, "Region:", data['region'])
        print(a, "Region name:", data['regionName'])
        print(a, "Latitude:", data['lat'])
        print(a, "Longitude:", data['lon'])
        print(a, "Timezone:", data['timezone'])
        print(a, "Zip code:", data['zip'])
        print(" "+clear)
# Error Handling
except KeyboardInterrupt:
        print('Exiting,Good Bye'+clear)
        sys.exit(0)
except requests.exceptions.ConnectionError as e:
    print(red+bold+"[!]"+" Please Check Your Internet Connection!"+clear)
    sys.exit(1)
    # Done!
