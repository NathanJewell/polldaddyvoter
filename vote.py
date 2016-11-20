#!/usr/bin/python
import requests, re, json, time, sys, random


url = 'https://polldaddy.com/poll/'
redirect = ""

def random_line(afile):
	lines = open(afile).read().splitlines()
	return random.choice(lines)

class voteOption:
	def __init__(self, ID, n, num):
		self.voteID = ID
		self.name = n
		self.numRequestedVotes = num

	voteID = 0
	name = ""
	numRequestedVotes = 0


proxyDict = {"https" : "https://localhost:8118", "http" : "http://localhost:8118"} #configure proxy to go through privoxy which routes to tor on socks5
def vote_once(form, value):
	c = requests.Session()
	init = c.get(url + str(form) + "/", headers=redirect, verify=True)
	data = re.search("data-vote=\"(.*?)\"",init.text).group(1).replace('&quot;','"')
	data = json.loads(data)
	pz = re.search("type='hidden' name='pz' value='(.*?)'",init.text).group(1)
	request = "https://polldaddy.com/vote.php?va=" + str(data['at']) + "&pt=0&r=0&p=" + str(form) + "&a=" + str(value) + "%2C&o=&t=" + str(data['t']) + "&token=" + str(data['n']) + "&pz=" + str(pz)
	send = c.get(request, headers=redirect, verify=False)
	return ('revoted' in send.url)


def vote(form, voterList, totalVotes):
	global redirect
	redirect = {"Referer": url + str(form) + "/", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.99 Safari/537.36", "Upgrade-Insecure-Requests":"1", "Accept-Encoding": "gzip, deflate, sdch", "Accept-Language": "en-US,en;q=0.8"}

	for i in range(totalVotes):
		for voter in voterList:
			for i in range(voter.numRequestedVotes):
				b = vote_once(form, voter.voteID)
				if not b:
					print "Voted for " + voter.name
					time.sleep(.1)
				else:
					#proxyDict = getProxy()
					#print "New Proxy Found Maybe"
					print "Locked.  Sleeping for 60 seconds."
					time.sleep(60)
					done = True



#create array of voteoptions ... here to pass into vote fxn
#specify pollid
#number of times to vote cumulatively
choices = [] 
poll_id = 
number_of_votes = 1000

vote(poll_id, choices, number_of_votes)

