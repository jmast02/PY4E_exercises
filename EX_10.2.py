
'''10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
'''

name = input("Enter file:")
if len(name) < 1: name = "mbox-short.txt"
fhand = open(name)
dictionary_hours = dict()

for line in fhand:
    words = line.split()
    if len(words) == 0 or len(words) < 2 or words[0] != 'From':
        continue
    else:
        colpos = words[5].find(':')
        hour = words[5][:colpos]
        if hour not in dictionary_hours:
            dictionary_hours[hour] = 1  # First entry
        else:
            dictionary_hours[hour] += 1  # Additional counts

lst = list()  # Initializes the lst
for key, val in list(dictionary_hours.items()):
    lst.append((key, val))  # fills list with hour, count of dict

lst.sort()  # sorts by hour

for key, val in lst:  #
    print(key, val)