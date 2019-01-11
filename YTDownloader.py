#! YouTube Videos Downloader Python Script - For Educational Purpose only
# This script can search any video on YouTube
# Select any Format for video and
# Download it on your risk.
# Use this for educational purpose only!
# This script was developed by Talha Siddique


import urllib.request as req 
import urllib.parse as par
import bs4 as bs  
import pafy


print(" ")
protocol = "https://"
site = "www.youtube.com"
term = "/results?"
search = input("What do you want to search on YouTube: ")  # User Input here

query = par.urlencode({"search_query" : search})  # encode search query

web = protocol + site + term + query

print(" ")
print("You searched for: ",search)
print(" ")
print("Resulted Url: ", web)
print(" ")
print("Getting Videos...")

res = req.urlopen(web)    # Open the url named web
source = res.read()       # reading the whole webpage
soup = bs.BeautifulSoup(source, 'html.parser')   # parsing the webpage with Beautiful Soup
print(" ")


count_url = 0
find_in_soup = soup.find_all('a', attrs={'class':'yt-uix-tile-link'}) # using Beautiful Soup to find attributes


get_url=[]           # empty list
for i in find_in_soup:
	get_url.insert(count_url, i.get('href'))   # populating the list
	get_title = i.get('title')                 # find the title of video
	print(count_url,get_title,"     ",protocol+site+get_url[count_url])
	count_url+=1


print(" ")
select = int(input("Choose (0 for 1st video): "))	

count_download = 0
for z in get_url:
	if select == count_download:
		download_url = protocol+site+get_url[select]	
	else:
		count_download += 1


def downloadYouTube(videourl):    # function for downloading the video
    yt = pafy.new(videourl)       # pafy object
    print("Video Title: ",yt.title," Views: ", yt.viewcount, " Duration: ", yt.duration) 
    # using pafy to get title, views, duration and description of video 
    print(" ")
    print("Description: ")
    print(yt.description)
    print(" ")
    stream = yt.streams # a list to get all video formats

    res_itr = 0        # iterator
    print("Formats...")
    for reslt in stream: 
    	print(res_itr,reslt)   # printing all formats of video
    	res_itr += 1

    best = yt.getbest() # get best resolution regardless of format
    print(" ") 
    choice = int(input("Choose any format (resolution): "))  

    choice_itr = 0
    for Vid in stream:
    	if choice == choice_itr:
    		stream[choice].download()        # downloading the selected video format
    	else: 
    		choice_itr += 1



print(" ")
print("Fetching Video Details...")
downloadYouTube(download_url)

print(" ")
quit = input("Wanna Quit this app? Press Q: ")
if quit == 'q' or 'Q':
	exit


