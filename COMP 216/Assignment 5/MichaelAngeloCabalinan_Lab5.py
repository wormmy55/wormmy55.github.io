#Name: Michael Angelo Cabalinan
#Student No: 300924795
#Date: February 17, 2024
#COMP216 Lab5

#Import modules/frameworks
import requests                                                             
import time
from threading import Thread
import argparse
import os

#PART A - Download single file

print(f"PART A\n")
def img_dl(url, pathname):                                              #Method that will take 2 arguments, url and pathname, to download a single image
    response = requests.get(url, stream=True)
    if response.status_code == 200:                                     #Improvement 1: Used error handling prior to file download
        with open(pathname, 'wb') as file:
            for chunk in response.iter_content(chunk_size=50):          
                    file.write(chunk)
        print(f"{pathname} successfully downloaded.")
    else:
        print(f"{pathname} failed to download from {url}.")
        
#Implementation of PART A code
img_pathname = 'Lab5_img.jpg'
img_url = 'https://th.bing.com/th/id/OIP.z-dkECmUFma29zYrb27JkwAAAA?w=264&h=180&c=7&r=0&o=5&pid=1.7'
img_dl(img_url,img_pathname);

#PART B - Download set of images sequentially

print(f"=======================================================")
print(f"\nPART B\n")

def seqimg_download():
    urls = [
'https://th.bing.com/th/id/OIP.z-dkECmUFma29zYrb27JkwAAAA?w=264&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.MhwSzfXnBG1MpuuA6IFi-AAAAA?w=218&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.m8b7Y9-81Q4UMCBMaFkw2QAAAA?w=198&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.XN9D7tH47WNJ8h214YgqTwAAAA?w=220&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.cFvfW8dARmuVtR3zOxfTSAHaE9?w=274&h=183&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.dU_vZ3d41uBHV3HUB8BaLgHaE8?pid=ImgDet&w=60&h=60&c=7&rs=1',
'https://th.bing.com/th/id/OIP.27OE2fVfhyHJ8tZ5g1sq6AHaE7?pid=ImgDet&w=60&h=60&c=7&rs=1',
'https://th.bing.com/th/id/OIP.JYXSCIpGskpiOxYTw1vuwgAAAA?w=252&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.QjWOHkojgYSz1LhaypSB-gAAAA?w=190&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.Wlfm_lF4VWlYLiPNfbmbDwHaHa?w=181&h=181&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.qegHjIc1S6QhWpPBLRxoLAHaIN?pid=ImgDet&w=60&h=60&c=7&rs=1',
'https://th.bing.com/th/id/OIP.C6q29lesR7-Ork5YKuI6LwAAAA?w=257&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.A7o1Bm-XNr9A_4pLPCCujgAAAA?w=252&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.n6jfttFUKpFKESmKxbk_RwHaEK?pid=ImgDet&w=60&h=60&c=7&rs=1',
'https://th.bing.com/th/id/OIP.AroTG9KnmisPIhICyGjoDAHaFj?w=223&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.bvEquy-hTbxHgAv5C0l4dQHaE8?pid=ImgDet&w=60&h=60&c=7&rs=1',
'https://th.bing.com/th/id/OIP.pGTxkbwreLj7l2ORZrtA8gAAAA?w=147&h=184&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.5SaLUh616MU7KDIP2_0VCwAAAA?w=204&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.S-lrZd2TFhSEpI3VRQyKqQAAAA?w=173&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.sDmZWxXBrF329vZvDu2HrAAAAA?w=266&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.7NzbWE55a7-J_PS-wbmJEgHaFH?pid=ImgDet&w=60&h=60&c=7&rs=1',
'https://th.bing.com/th/id/OIP.Er7g9WNX2l-q0eT0kmaifgHaE7?pid=ImgDet&w=60&h=60&c=7&rs=1',
'https://th.bing.com/th/id/OIP.OeLv1q1dEfGkl1bRHfM5awHaFj?w=240&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.MksSZEmu5Cgly2HNvRp4NQAAAA?w=180&h=163&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.GHbdZZHVGW0k96skiIB6DQHaFj?pid=ImgDet&w=60&h=60&c=7&rs=1'
]
 
    ovrl_start_time = time.perf_counter()                                       #Start timer

    for i, url in enumerate(urls, start=0):                                     #For loop to iterate through the url in the urls array, download each image, and calculate time for each download
        start_time = time.perf_counter()
        img_pathname = f'Lab5_img{i}.jpg'
        img_dl(url, img_pathname)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"Image {i} downloaded in {elapsed_time:.2f} seconds")
        print(f"------------------------------------------------------")

    ovr_end_time = time.perf_counter()                                          #End timer
    total_time = int(round((ovr_end_time - ovrl_start_time) * 1000))            #Total elapsed time calculation

    print(f"\nTotal time elapsed(sequential): {total_time} milliseconds")

#Calling the method
seqimg_download()

#PART C
print(f"=======================================================")
print(f"\nPART C\n")

def threadedimg_download(): 
    urls = [
'https://th.bing.com/th/id/OIP.z-dkECmUFma29zYrb27JkwAAAA?w=264&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.MhwSzfXnBG1MpuuA6IFi-AAAAA?w=218&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.m8b7Y9-81Q4UMCBMaFkw2QAAAA?w=198&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.XN9D7tH47WNJ8h214YgqTwAAAA?w=220&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.cFvfW8dARmuVtR3zOxfTSAHaE9?w=274&h=183&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.dU_vZ3d41uBHV3HUB8BaLgHaE8?pid=ImgDet&w=60&h=60&c=7&rs=1',
'https://th.bing.com/th/id/OIP.27OE2fVfhyHJ8tZ5g1sq6AHaE7?pid=ImgDet&w=60&h=60&c=7&rs=1',
'https://th.bing.com/th/id/OIP.JYXSCIpGskpiOxYTw1vuwgAAAA?w=252&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.QjWOHkojgYSz1LhaypSB-gAAAA?w=190&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.Wlfm_lF4VWlYLiPNfbmbDwHaHa?w=181&h=181&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.qegHjIc1S6QhWpPBLRxoLAHaIN?pid=ImgDet&w=60&h=60&c=7&rs=1',
'https://th.bing.com/th/id/OIP.C6q29lesR7-Ork5YKuI6LwAAAA?w=257&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.A7o1Bm-XNr9A_4pLPCCujgAAAA?w=252&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.n6jfttFUKpFKESmKxbk_RwHaEK?pid=ImgDet&w=60&h=60&c=7&rs=1',
'https://th.bing.com/th/id/OIP.AroTG9KnmisPIhICyGjoDAHaFj?w=223&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.bvEquy-hTbxHgAv5C0l4dQHaE8?pid=ImgDet&w=60&h=60&c=7&rs=1',
'https://th.bing.com/th/id/OIP.pGTxkbwreLj7l2ORZrtA8gAAAA?w=147&h=184&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.5SaLUh616MU7KDIP2_0VCwAAAA?w=204&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.S-lrZd2TFhSEpI3VRQyKqQAAAA?w=173&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.sDmZWxXBrF329vZvDu2HrAAAAA?w=266&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.7NzbWE55a7-J_PS-wbmJEgHaFH?pid=ImgDet&w=60&h=60&c=7&rs=1',
'https://th.bing.com/th/id/OIP.Er7g9WNX2l-q0eT0kmaifgHaE7?pid=ImgDet&w=60&h=60&c=7&rs=1',
'https://th.bing.com/th/id/OIP.OeLv1q1dEfGkl1bRHfM5awHaFj?w=240&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.MksSZEmu5Cgly2HNvRp4NQAAAA?w=180&h=163&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.GHbdZZHVGW0k96skiIB6DQHaFj?pid=ImgDet&w=60&h=60&c=7&rs=1'
]
    t_start = time.perf_counter()                               #Start timer
    threads = []                                                
    for i, url in enumerate(urls, start=0):                                 
        pathname = f'Lab5_img{i}.jpg'
        t = Thread(
            target=img_dl,                                      #PART A method to run as a thread
            args=(url, pathname))
        
        t.start()                                               #Start the thread
        threads.append(t)                                       #Append to threads list

    for thread in threads:
        thread.join()

    t_end = time.perf_counter()
    t_overall_time = int(round((t_end - t_start) * 1000))
    print(f"\nTotal time elapsed(threaded): {t_overall_time} milliseconds")


# Calling PART C function
threadedimg_download()

#PART D
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
        threadedimg_download()

if __name__ == "__main__":
    main()
else: print("script not running")





        