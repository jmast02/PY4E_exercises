'''9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
'''

dictionary_addresses = dict()  # Initializes the dictionary
fname = input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

for line in fhand:
    words = line.split()
    if len(words) == 0 or len(words) < 2 or words[0] != 'From':
        continue
    else:
        if words[1] not in dictionary_addresses:
            dictionary_addresses[words[1]] = 1  # First entry
        else:
            dictionary_addresses[words[1]] += 1  # Additional counts

maximum = 0  # Initilizes the variable
for address in dictionary_addresses:
    if dictionary_addresses[address] > maximum:  # Checks if new maximum
        maximum = dictionary_addresses[address]  # Updates the maximum if need
        maximum_address = address  # Stores the address of maximum

print(maximum_address, maximum)
