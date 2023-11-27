from pytube import YouTube
import sys

numbers = range(3)

print("Welcome to the YouTube downloader using pytube!")
print(" ")
link = str(input("Paste the link of the video:"))
print(" ")
export = str(input("Folder path: "))
print(" ")
print("Would you like to see the information about the video, or download it?")
print(" ")
print("1. View information")
print("2. Download video")
print(" ")
choice = int(input("Type a number:"))
if choice not in numbers:
    print("Our of range, try number 1 or 2.")
    sys.exit()
print("")
video = YouTube(link)
low = video.streams.get_lowest_resolution()
high = video.streams.get_highest_resolution()

if choice == 1:
        print("Title: ", video.title)
        print("Views: ", video.views)
        print("Uploader: ", video.author)
        print("Length (seconds): ",video.length)
        print("Age restricted?: ",video.age_restricted)
if choice == 2:
     print("Would you like to save the video in the best or the worst resolution?")
     print("1. Highest resolution")
     print("2. Lowest resolution")
answer = int(input())
if answer not in numbers:
    print("Our of range, try number 1 or 2.")
    sys.exit()
if answer == 1:
     high.download(export)
     print("The video was saved in the highest quality in " +export +".")
if answer == 2:
     low.download(export)
     print("The video was saved in the lowest quality in " +export +".")




