import xml.etree.ElementTree as ET

tree = ET.parse('country_data.xml')
root = tree.getroot()

for child in root:
    print(child.tag, child.attrib)

print(root[0][1].text)

a = 1

# file = open("testfile.workflow","w") 
# file.write("Hello World") 
# file.close() 