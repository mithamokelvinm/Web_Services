import xml.etree.ElementTree as ET

data = '''
<person>
    <name>Georgina<name/>
    <phone type = "intl"> +254724675689 <phone/>
    <email hide = "yes"/>
<person/>
'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
