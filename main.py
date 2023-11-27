from pytube import YouTube
from sys import argv

print("Welcome to the YouTube downloader using pytube!")
print("Would you like to see info of the video you're about to download?")
link = str(input(argv[1]))
youtube = YouTube(link)

print()