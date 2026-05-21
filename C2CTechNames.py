# TO-DO: Extract all tech names from Civ4TechInfos from C2C
import xml.etree.ElementTree as ET

if __name__ == "__main__":
    pathOfC2C = '/home/nicholas/Desktop/C2C/Tech Names/CIV4TechInfos.xml'
    exEmEl = ET.parse(pathOfC2C)
    root = exEmEl.getroot()
    # TO-DO: Only print tech names, not all XML text:
    # Current iteration lists every tag in XML:
    for result in root.iter():
        with open("TechyNames.txt", "a") as f:
            f.write(result.text)