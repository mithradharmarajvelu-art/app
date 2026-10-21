from lxml import etree

parser = etree.XMLParser(dtd_validation=True)

try:
    tree = etree.parse("students.xml", parser)
    print("XML is VALID")
    print("DTD verification successful!")
except etree.XMLSyntaxError as e:
    print("XML is INVALID")
    print(e)
