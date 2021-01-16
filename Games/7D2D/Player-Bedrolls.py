import xml.etree.ElementTree as ET
from steamUser import steamUser
import os

# Steam Web API
# available at https://steamcommunity.com/dev/apikey
steamAPI = ''
# players.xml file to read from
# this is found in the 7 Days 2 Die Saves folder
xmlLocation = 'players.xml'
# output CSV file to write to
csvLocation = 'players.csv'

tree = ET.parse(xmlLocation)
root = tree.getroot()

try:
    os.remove(csvLocation) # output csv to plot
except OSError:
    pass

csvFile = open(csvLocation, "a")

csvFile.write('name,steamid64,x,y,z\n')
for elem in root:
    id = elem.attrib['id']
    for subelem in elem:
        if 'pos' in subelem.attrib:
            pos = subelem.attrib['pos']
    user = steamUser(id, steamAPI)
    userInfo = user.getUser()
    csvFile.write(userInfo['name'] + ',' + id + ',' + pos + '\n')

csvFile.close()

f = open(csvLocation, "r")
print(f.read())
f.close()
