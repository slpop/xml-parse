# Calling arguments: plant_catalog.xml plantName percentChange
import xml.etree.ElementTree as ET
import sys
import re

# input parameters
searchName = sys.argv[2]
percent = float(sys.argv[3])

# parse XML data file
tree = ET.parse(sys.argv[1])
# request root from tree
root = tree.getroot()

# findall
plants = root.findall('PLANT')
# for each plant in result
for plant in plants:
    plantName = plant.find('COMMON').text
    # compare name to name passed in command line
    if plantName == searchName:
        # if match found, then apply percentage change
        price = float(plant.find('PRICE').text)
        new_price = round(price+(price*(percent/100)), 2)
        # save to tree
        plant.find('PRICE').text = str(new_price)

# write tree back to new file
tree.write('updated_catalog.xml')