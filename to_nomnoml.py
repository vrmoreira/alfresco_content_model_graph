from bs4 import BeautifulSoup
import sys

filename = sys.argv[1]

# Reading the data inside the xml
# file to a variable under the name
# data
with open(filename, 'r') as f:
    data = f.read()

# Passing the stored data inside
# the beautifulsoup parser, storing
# the returned object
Bs_data = BeautifulSoup(data, "xml")

b_aspects = Bs_data.find_all('aspect')
b_types = Bs_data.find_all('type')


def print_type_aspect(list):
    for b_type in list:
        try:
            # <type/aspect name="acme:qrCode">
            print(f"[{b_type.attrs['name']}")
            for b_content in b_type.contents:
                # <type/aspect name="acme:qrCode">
                #   <properties>
                if b_content.name == "properties":
                    for b_property in b_content.contents:
                        # <type/aspect name="acme:qrCode">
                        #   <properties>
                        #      <property name="acme:text">
                        if b_property.name == "property":
                            print(f"|{b_property.attrs['name']}")
            print("]")
        except KeyError:
            continue


print_type_aspect(b_types)
print_type_aspect(b_aspects)

# to generate a PNG file, please use https://kroki.io, select "Nomnoml" and past the output produced by this script
