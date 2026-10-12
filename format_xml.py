
from lxml import etree

# Read the XML file
tree = etree.parse("student.xml")

# Format XML with indentation
formatted_xml = etree.tostring(
    tree,
    pretty_print=True,
    encoding="unicode"
)

# Display formatted XML
print("Formatted XML:")
print(formatted_xml)

# Save formatted XML to a new file
with open("student_formatted.xml", "w", encoding="utf-8") as file:
    file.write(formatted_xml)

print("Formatted XML saved successfully!")
