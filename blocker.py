import time 
from datetime import datetime as dt 

# change hosts path according to your OS
hosts_path ="C:\Windows\System32\drivers\etc\hosts"
# localhost's IP 
redirect = "127.0.0.1"

# websites That you want to block
no_of_site=int(input("how many no of site you want to block"))

for i in range(1,no_of_site+1):
    website_list=[]
    website=input("enter the site url name: ")
    website_list.append(website)

startTime=int(input("enter the start time (in 24hrs format):"))
endTime=int(input("enter the end time (in 24hrs format):"))
while True: 

	# time of your work 
	if dt(dt.now().year, dt.now().month, dt.now().day,startTime)< dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,endTime): 
		print("Working hours...time to block the site") 
		with open(hosts_path, 'r+') as file:
			content = file.read()
			for site in website_list: 
				if website in content: 
					pass
				else: 
					#wrinting the localhost ip and website
					file.write(redirect + " " + website + "\n") 
	else: 
		with open(hosts_path, 'r+') as file: 
			content=file.readlines() 
			file.seek(0) 
			for line in content: 
				if not any(website in line for website in website_list): 
					file.write(line) 

			# removing hostnmes from host file 
			file.truncate() 

		print("Fun hours...unblocking all site") 
	time.sleep(5) 
