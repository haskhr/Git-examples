import xml.etree.ElementTree as ET
# get the xml file data
stream = open('sample.xml','r')

#Parse the data into ElementTree object
xml = ET.parse(stream)

#Get the 'root' Element object from the ElementTree 
root = xml.getroot()


# Iterate through each child of the root Element 
for e in root:
    #print the 'Id' Attribute of tje Element object
    print(e.get("category"))
    #print the stringfield version of the element
    print(ET.tostring(e))
    print("")

    #print the 'Id' Attribute of tje Element object
    #print(e.get("category"))