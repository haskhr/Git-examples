import  xmltodict


# get the XML file 
stream = open ( 'sample.xml' , 'r')

# Parse the XML file into an 'OrderedDict'
xml = xmltodict.parse(stream.read())

for e in xml["bookstore"]["book"]:
    print(e)
    print( " ")
