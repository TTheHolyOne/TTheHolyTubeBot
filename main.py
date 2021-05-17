import youtube_dl
import os
import sys
import pandas as pd
import time
from textblob import TextBlob
import sys
import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk
from main import *
import webbrowser
import colorama
from colorama import *

init()


print(Fore.RED + "Starting TTheHolyTubeBot..")
time.sleep(1)
print(Fore.CYAN + "\nTTheHolyTubeBot Started.\nDeveloper: TTheHolyOne#1642\n\n")
def wholeprogram():
    print(Fore.RED + "Okay then... Starting program\n\n")
    def download_vid(vid):
        vid = vid.strip()
        ydl = youtube_dl.YoutubeDL()
        try:
            ydl.download([vid])
        except:
            print("Darn! Invalid URL!")




    link_of_the_video = input("Copy & paste the URL of the YouTube video you want to download:- \n")
    vid = link_of_the_video.strip()

    download_vid(vid)
    print(Fore.CYAN + f"Check your folder where this script is located to find video!\nYou just downloaded {vid}!")
