"""LABB1 GEODATA OCH SÖK"""

class Location(object):

        def __init__(self, name, desc, lat, longi, date):
                self.name = name
                self.desc = desc
                self.lat = lat
                self.longi = longi
                self.date = date


        def __str__(self):
                return self.name


def extractdata():
	"""läs in filen"""
	with open("geodataSW","r", encoding="utf-8") as f:
            array_list = []      
            a = 1

            for line in f:
                if line.strip() != "" and not line.startswith("#"):

                    if a == 1:
                        name = line
                        a=a+1
                    elif a == 2:
                        description = line
                        a=a+1
                    elif a == 3:
                        latitude = line
                        a=a+1
                    elif a == 4:
                        longitude = line
                        a=a+1
                    elif a == 5:
                        date = line
                        array_list.append(Location(name, description, latitude, longitude, date))
                        a=1

	


    return array_list



def main():
        all_places = extractdata()
        print(all_places)

main()

