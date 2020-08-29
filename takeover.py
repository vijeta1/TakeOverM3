import os
import sys
import requests
import argparse
import pyfiglet

fingerprint = [
	"If this is your website and you've just created it, try refreshing in a minute",
	"The specified bucket does not exist",
	"Repository not found",
	"Trying to access your account?",
	"404 Not Found",
	"Fastly error: unknown domain:",
	"The feed has not been found.",
	"404 Not Found",
	"The thing you were looking for is no longer here, or never was",
	"There isn't a Github Pages site here.",
	"404 Blog is not found",
	"We could not find what you're looking for.",
	"No settings were found for this company:",
	"No such app",
	"Uh oh. That page doesn't exist.",
	"is not a registered InCloud YouTrack",
	"No Site For Domain",
	"It looks like you may have taken a wrong turn somewhere. Don't worry...it happens to all of us.",
	"Unrecognized domain",
	"Tunnel *.ngrok.io not found",
	"404 error unknown site!",
	"Project doesnt exist... yet!",
	"Sorry, this shop is currently unavailable.",
	"This job board website is either expired or its domain name is invalid.",
	"page not found",
	"project not found",
	"Whatever you were looking for doesn't currently exist at this address",
	"Please renew your subscription",
	"The requested URL was not found on this server.",
	"page not found",
	"This UserVoice subdomain is currently available!",
	"The page you are looking for doesn't exist or has been moved.",
	"Do you want to register *.wordpress.com?",
	"You are being <a href=\"https://www.statuspage.io\">redirected",
]

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'}

def takeover(mainfile):
	count = len(open(sys.argv[1]).readlines( ))
	print("\n"+str(count) + " Subdomains found in " + str(sys.argv[1]))
	print("Checking for possible Subdomain Takeover....")
	readfile = open(sys.argv[1],'r')
	list = readfile.read().split('\n')

	for subd in list:
		if subd == "":
			continue
		try:
			response = requests.get("https://"+subd,headers=headers)
			response.text
		except requests.exceptions.ConnectionError:
			continue
		subdResponse = response.text
		for text in fingerprint:
			if text in subdResponse:
				print("Possible Subdomain Takeover Found: "+subd)
				break
		print("No possible Takeover Found: "+subd)
	readfile.close()

def Main():
	ascii_banner = pyfiglet.figlet_format("TakeOverM3")
	print(ascii_banner)
	parser = argparse.ArgumentParser()
	parser.add_argument("SubdomainList", help="Usage python3.7 takeover.py subdomain.txt", type= str)
	args = parser.parse_args()
	takeover(args.SubdomainList)

if __name__ == "__main__":
    Main()
