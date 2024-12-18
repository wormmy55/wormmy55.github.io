# -*- coding: utf-8 -*-
"""group1_threads.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1a7DRXAElBBZgXkczSnG4mBKjmnMw3JWo

Group 1<br>
Name: Salma Chaaban<br>
Student number: 301216551<br>
Name: Hodan Ahmed Yusuf <br>
Student number: 301226634 <br>
Name: Jonathan Au<br>
Student number: 300827701<br>
Name: Landon Essex<br>
Student number: 301349452 <br>
Name: Michael Angelo Cabalinan <br>
Student number: <br>

##Description:
This exercise consists of four parts: <br><br>
  1.	Write a function to download a single file. This function will take two arguments: the url of the file (in this case an image from bing) and the pathname (the name of the downloaded file). You will use the request library to do this.<br>
  To indicate to the user that the program is alive, you should display the name of the resulting file on the console.<br><br>
  2.	Second is to write a function to invoke the above function to download a set of images sequentially. That implies that this function will send the appropriate arguments to the above function. The urls are listed below.<br><br>
  3.	Third is to write a function to download the same set of images using threads. You will measure the time taken for both downloads to decide if there is any advantage of using threads.<br><br>
  4.	Write the logic to check if the script is being executed, if it is, it checks for the command line arguments and process them appropriately and then runs the program accordingly.<br><br>
Please download your images to a separate folder so, you can delete the entire folder afterwards.<br>

Python frameworks/Modules:<br>
•	requests: This is an external framework that you would have need to run the labs. This would have been on your machine because it was used in previous labs.<br>
•	time: This is an internal module that is a part of python standard distribution and does not require any separate installation.<br>
•	argparse: This is an internal module that is a part of python standard distribution and does not require any separate installation.<br>
•	threading: This is also an internal module that is a part of python standard distribution and does not require any separate installation.<br>
•	NO OTHER LIBRARY IS PERMITTED!!!. Unless you justify to me in your code.
"""

# Imports
import requests
from time import perf_counter
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

"""Part A
1.	Create a function to take a URL and a pathname that does the following.<br>
a.  Use the request library to download the content (specified by the argument) as bytes. <br>
[see wk05_a6_download_file.py]<br><br>
b.	Write the contents of the uri to the above file name (specified by the argument). <br>
[See wk05_a6_download_file.py]<br><br>
c.	Print a suitable message.

Note: If there is a problem with one of the urls in the list then you may substitute it with one of you own.
"""

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

"""Part B
1.	Create a function that does not require any argument and does the following:<br>
a.	Start timer.<br>
[import the time module<br>
use time.perf_counter() to get the current time.]<br><br>
b.	Call the function in Part A with appropriate arguments (first the supplied url list and the second one that you will have to generate) to sequentially each url. (Invoke the method after the previous download is completed).<br><br>
c.	End timer. <br>
[again use time.perf_counter() to get the current time.]<br><br>
d.	Print elapse times. <br>
[subtract (a) from (c).]<br><br>

Note: With my present internet connection, I got a time of 2359 milli seconds.

"""

def sequential_downloads():
  #start timer
  start_timer = perf_counter()

  for url in urls:
    filename = f'image_{urls.index(url) + 1}.jpg'
    downloadFile(url,filename)

  #end timer
  end_timer = perf_counter()

  #print elapsed time
  elapsed_time_result = end_timer - start_timer
  print(f'Total elapsed time =  {elapsed_time_result: .2f} seconds ')
sequential_downloads()

"""Part C
1.	Create a function that does not require an argument and does the following:<br><br>
a.	Start timer.<br><br>
b.	In a threaded fashion, call the function in Part A with appropriate arguments.<br>
[see wk03_d2_threading.py.]<br>
If your system complains about replacing the files in Part 2, you will need to remove/delete the files before running this part<br><br>
c.	End timer when all the threads have completed their downloads.<br><br>
d.	Print elapse times.<br><br>
See the hints for Part B.<br>

Note: With my present internet connection, I got a time of 2359 milli seconds.
"""

def dlThread():
  start = perf_counter()        #assigns the timer to a variable
  thread = []                   #creats an empty thread

  for i in urls:
    path = f'{filepath}threaded_image_{urls.index(i) + 1}.jpg'
    u1 = Thread(
        target = downloadFile,  #this sets the target method for threading
        #name= i,                #optional name
        args=(i, path)          #sets the argument as i - urls - and path
    )
    u1.start()                  #this starts the timer
    thread.append(u1)           #this add to the thread

  for i in thread:
    i.join()
    #lap = perf_counter()     #lap counter
    #print(f'Finished downloading in {round(lap-start, 4)} seconds.')   #individual download counter

  end = perf_counter()        #end counter
  print(f'Finished downloading all in {round(end-start, 4)} seconds.')  #overall time

#This is my path as in Jonathan Au
filepath = 'insert path here' #This will work if you put in a valid filepath
#filepath = 'E:\My Library\My Documents\Centennial College\A.I. - Soft_Engineering\Semester 4\COMP 216 - Networking for Software Devs\Assignments\Assignment 5\IMGs\'
dlThread()

"""Part D
1.	If the script is running as an executable, it does the following:<br><br>
a.	Creates an ArgumentParser and adds two arguments<br>
i.	A mandatory argument that may be either serial or threaded<br>
ii.	An optional argument that allows the user to specify a data folder to download the images to a seperate folder<br><br>
b.	If the mandatory argument is supplied, then invoke the appropriate method (either Part B or Part C).<br>

"""

import argparse

def main():
    parser = argparse.ArgumentParser(description='Download images')
    parser.add_argument('method', choices=['serial', 'threaded'], help='Download method')
    parser.add_argument('--folder', '-i', help='Data folder to download the images to')
    args = parser.parse_args()

    if args.method == 'serial':
      sequential_downloads()
    elif args.method == 'threaded':
      dlThread()