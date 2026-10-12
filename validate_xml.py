
from lxml import etree

try:
    with open("student.dtd", "rb") as dtd_file:
        dtd = etree.DTD(dtd_file)

    xml_doc = etree.parse("student.xml")

    if dtd.validate(xml_doc):
        print("XML is valid!")
        print("DTD validation successful!")
    else:
        print("XML is invalid!")
        print(dtd.error_log)

except Exception as error:
    print("Error:", error)
