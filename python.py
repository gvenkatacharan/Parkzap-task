import urllib, json, time

#getting data from the url 
url = "http://demo4657392.mockable.io/list-tag-ids"
response = urllib.urlopen(url)
data = json.loads(response.read())

#if data received from the url the update the data in the local data base ie. list-tag-ids.json file
if data :
    print("data received form the website")
    with open('list-tag-ids.json', 'w') as outfile:
        json.dump(data, outfile)
#If data is not received then, use the data form the local database ie. list-tag-ids.json file
else:
    print("Data has not been received. Loading from the local data")
    with open('list-tag-ids.json') as f:
        data = json.load(f)

# with open('list-tag-ids.json') as f:
#     data = json.load(f)

terminalin = raw_input('enter the data:'); 
length = len(data['student_id'])

#starting the timer
start_time = time.time()

for x in range(length):
    if(data['student_id'][x][str(x+1)] == terminalin):
        print("The id of the string is: %d" %(x+1))

#ending the timer
end_time = time.time()

print("Time complexity:%d" %(end_time-start_time))


