import pyshorteners

url = input("Enter URL : \n")

print("URL after Shortenning : \n" , pyshorteners.Shortener().tinyurl.short(url))