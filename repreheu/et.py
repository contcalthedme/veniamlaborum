import xml.etree.ElementTree as ET

# Sample XML data
xml_data = '''<root>
    <required_header>
        <url>http://example.com</url>
    </required_header>
</root>'''

# Parse the XML data
root = ET.fromstring(xml_data)

# Find the 'url' element within the 'required_header' element and get its text
url_link = root.find('required_header').find('url').text

# Print the URL
print(url_link)
