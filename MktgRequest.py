#Combines the retrive file and the read file to answer marketing's requests
from os.path import exists as exist

#Creates a local copy of the log if it doesn't already exist
if not exist('local_copy.log'):
    from urllib.request import urlretrieve
    URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
    LOCAL_FILE = 'local_copy.log'

    # Use urlretrieve() to fetch a remote copy and save into the local file path
    local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE)

#moves the log into a searchable list
FILE_NAME = 'local_copy.log'

with open(FILE_NAME) as f:
    lines = [line.rstrip('\n') for line in f]

#returns the number of lines in lines;
#it is also the nubmer of requests in the life of the log
length = len(lines)

#Will return the number of requests in the last 6 months
numreq = lines.count("Feb/2022") + lines.count("Jan/2022") + lines.count("Dec/2021") + lines.count("Nov/2021") + lines.count("Oct/2021") + lines.count("Sep/2021")

#Prints out the information for the marketing request
print("Here are the number of requests to the server in the last 6 months: " + str(numreq))
print("Here are the number of requests in the life of the log: " + str(length))
