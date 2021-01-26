from telnetlib import Telnet
from io import StringIO
import csv
import os

# Try to remove previous run
try:
    os.remove("onlinePlayers.csv") # output csv to plot
except OSError:
    pass

# Open CSV file to append data to
csvFile = open("onlinePlayers.csv", "a")
csvFile.write('name,steamid64,x,y,z\n')

# Connect to telnet
with Telnet('localhost', 8081) as tn:
    tn.read_until(b'Text that i am 99% sure wont come up in the header', timeout=0.1)
    tn.write(b'lp\r\n')
    data = tn.read_until(b'game', timeout=1)
    tn.write(b'exit\r\n')

data = data.decode('utf-8')

print(data)
print('--------------')

# Get each line
for line in data.splitlines():
    # We only want lines with player data
    if not line.startswith('Total'):
        # Remove the number prefix
        line = line[line.find('id'):]

        # Turn line into an array
        aline = []
        f = StringIO(line)
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            aline = row

        # Get wanted data
        name = aline[1]
        x = aline[2]
        y = aline[3]
        z = aline[4]
        steamid = aline[15]

        # Clean up values
        name = name[1:]
        x = x[x.find('(')+1:]
        y = y[1:]
        z = z[1:]
        z = z[:z.find(')')]
        steamid = steamid[steamid.find('=')+1:]

        # Append to csv
        csvFile.write(name + ',' + steamid + ',' + x + ',' + y + ',' + z + '\n')

        print(name + ',' + steamid + ',' + x + ',' + y + ',' + z)

# Close the csv file
csvFile.close()