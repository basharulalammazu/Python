# pip install pyshorteners


import pyshorteners

long_url = input("Enter the URL to shorten: ")
type_tiny = pyshorteners.Shortener()
short_url = type_tiny.tinyurl.short(long_url)

# Display the shortened URL
print("The Shortened URL is: + short_url)