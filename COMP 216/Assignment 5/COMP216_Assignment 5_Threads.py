# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 12:59:16 2024

@author: drago
"""
# Imports
import os
import requests
import argparse
from time import perf_counter
from random import randint
from threading import Thread

urls = [
'https://th.bing.com/th/id/OIP.z-dkECmUFma29zYrb27JkwAAAA?w=264&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.MhwSzfXnBG1MpuuA6IFi-AAAAA?w=218&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.m8b7Y9-81Q4UMCBMaFkw2QAAAA?w=198&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.XN9D7tH47WNJ8h214YgqTwAAAA?w=220&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.cFvfW8dARmuVtR3zOxfTSAHaE9?w=274&h=183&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.wcEy7Ow-TaAohBCz6USqCAAAAA?w=265&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.9FWt0sWpi4UOee5o3WdI-QHaFj?w=224&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.JYXSCIpGskpiOxYTw1vuwgAAAA?w=252&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.QjWOHkojgYSz1LhaypSB-gAAAA?w=190&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.Wlfm_lF4VWlYLiPNfbmbDwHaHa?w=181&h=181&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.ZquJ_NwCCyWfvpAEeU-vngAAAA?w=142&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.C6q29lesR7-Ork5YKuI6LwAAAA?w=257&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.A7o1Bm-XNr9A_4pLPCCujgAAAA?w=252&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.oSjt2rY3YUScDY7pw3b1WAHaFj?w=236&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.AroTG9KnmisPIhICyGjoDAHaFj?w=223&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.zSyHBN9_rn_O9XBkdPx-agAAAA?w=189&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.pGTxkbwreLj7l2ORZrtA8gAAAA?w=147&h=184&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.5SaLUh616MU7KDIP2_0VCwAAAA?w=204&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.S-lrZd2TFhSEpI3VRQyKqQAAAA?w=173&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.sDmZWxXBrF329vZvDu2HrAAAAA?w=266&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.5umgRLykyWn-v_5HmOS0NAHaE7?w=243&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.MPayRq2bYdhfVUj5O9BCnwAAAA?w=125&h=184&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.OeLv1q1dEfGkl1bRHfM5awHaFj?w=240&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.MksSZEmu5Cgly2HNvRp4NQAAAA?w=180&h=163&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.HCpPn-IRV8SVidBlRoBRUwHaE7?w=287&h=191&c=7&r=0&o=5&pid=1.7'
]
#test_url = 'https://th.bing.com/th/id/OIP.z-dkECmUFma29zYrb27JkwAAAA?w=264&h=180&c=7&r=0&o=5&pid=1.7'
#path = './IMGs/image_{urls.index(url) + 1}.jpg'
filepath = './IMGs/'
#path = 'E:\My Library\My Documents\Centennial College\A.I. - Soft_Engineering\Semester 4\COMP 216 - Networking for Software Devs\Assignments\Assignment 5\IMGs'

#Part A
def downloadFile(URL, pathname):
    try:
        r = requests.get(URL, stream=True)               # make a HTTP GET request
        with open(pathname, 'wb') as fd:
            for chunk in r.iter_content(chunk_size=50):  # small size
                print('+', end='')                       # give user feedback
                fd.write(chunk)                          # write the bit to file
            print('\n...download completed')             # complete
    except requests.exceptions.RequestException as e:    # in case of exceptions
        print(f"Error downloading content: {e}")

#downloadFile(test_url, path)

#Part B
def seqimg_download():
    # start timer
    from time import perf_counter
    import requests
    
    #implement part A
    #start timer
    start_timer = perf_counter()
    
    #sequential download
    for url in urls:
        filename = f'{filepath}image_{urls.index(url) + 1}.jpg'
        downloadFile(url,filename)
        
        #end timer
        end_timer = perf_counter()
        
        #print elapsed time = a - c
        elapsed_time_result = end_timer - start_timer
        print(f'Total elapsed time: {elapsed_time_result: .2f} seconds')
seqimg_download()

#Part C
def dlThread():
  start = perf_counter()
  thread = []

  for i in urls:
    path = f'{filepath}threaded_image_{urls.index(i) + 1}.jpg'
    u1 = Thread(
        target = downloadFile,
        name= i, 
        args=(i, path)
    )
    u1.start()
    thread.append(u1)

  for i in thread:
    i.join()
    lap = perf_counter()
    print(f'Finished downloading in {round(lap-start, 4)} seconds.')
    
  end = perf_counter()
  print(f'Finished downloading all in {round(end-start, 4)} seconds.')

dlThread()

#Part D
"""
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download images')
    parser.add_argument('method', choices=['serial', 'threaded'], help='Download method')
    parser.add_argument('--folder', help='Data folder to download the images to')
    args = parser.parse_args()

    path = args.folder

    if args.method == 'serial':
     for url in urls:
        filename = url.split('/')[-1]
        filepath = f"{path}/{filename}"
        downloadFile(url, filepath)
    elif args.method == 'threaded':
     dlThread(urls, path)

print(f"=======================================================")
print(f"\nPART D\n")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=['serial', 'threaded'], help='download mode to use')
    parser.add_argument('--images_dir', '-i', help='directory to download images to')
    args = parser.parse_args()

    # Optionally change directory if images_dir is provided
    if args.images_dir:
        os.makedirs(args.images_dir, exist_ok=True)
        os.chdir(args.images_dir)

    # Based on the chosen mode, call the respective function
    if args.mode == 'serial':
        seqimg_download()
    elif args.mode == 'threaded':
        dlThread()

if __name__ == "__main__":
    main()
else: print("script not running")
"""

def main():
    parser = argparse.ArgumentParser(description='Download images')
    parser.add_argument('method', choices=['serial', 'threaded'], help='Download method')
    parser.add_argument('--folder', '-i', help='Data folder to download the images to')
    args = parser.parse_args()

    if args.method == 'serial':
      downloadFile()
    elif args.method == 'threaded':
      dlThread()
#main()








