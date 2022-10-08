import xml.etree.ElementTree as ET

data = '''
<person>
    <name>Olive<name/>
    <phone type = "intl"> +254722-123-456 <phone/>
    <email hide = "yes"/>
<person/>
'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
