<?xml version="1.0"?>
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
        <head><title>Student Records</title></head>
        <body>
            <h2>Student Details</h2>
            <table border="1" cellpadding="8">
                <tr>
                    <th>Roll No</th>
                    <th>Name</th>
                    <th>Department</th>
                    <th>Year</th>
                </tr>
                <xsl:for-each select="students/student">
                    <tr>
                        <td><xsl:value-of select="rollno"/></td>
                        <td><xsl:value-of select="name"/></td>
                        <td><xsl:value-of select="department"/></td>
                        <td><xsl:value-of select="year"/></td>
                    </tr>
                </xsl:for-each>
            </table>
        </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
