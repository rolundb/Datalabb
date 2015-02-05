import time
import os
from operator import attrgetter

# Reads from .txt-file and extracts relevant lines which becomes attributes for objects that are
#placed in an array.
#
#parameter1 a_filename      Name of a txt-file.
# return: the_array_list        List of objects created based on content of .txt file.

def readFile(a_filename):
    with open(a_filename, "r", encoding="utf-8") as f:
        the_array_list = []
        the_reset = 0
        i= the_reset
        for line in f:
            if line.strip() != "" and not line.startswith("#"):
                i+=1
                
                if i == 1:
                    name = line

                elif i == 2:
                    description = line

                elif i == 3:
                    latitude = line

                elif i == 4:
                    longitude = line

                elif i == 5:
                    date = line
                    the_array_list.append(Place(name, description, latitude, longitude, date))
                    i = the_reset
               
    return the_array_list


# Matches the users input with object in list and runs the __str__-method for said object
#
# parameter1 an_intext      User input that is matched with attribute "name" of objects in an_array. 
# parameter2 an_array       An array with objects.
# return: None

def findPlace(an_intext, an_array):
    the_time_start = time.time()
    for an_object in an_array:
        if an_object.getName().lower() == an_intext.lower(): 
            print(an_object)
            the_time_end = time.time()
            the_time_passed = the_time_end-the_time_start 
            print("Time for search:" + str(the_time_passed)+ " seconds.")
            return

    print("\n" + an_intext +" could not be found. Please restart the program to try again.\n\n")
    os._exit(0)

    


# Sorts an array with objects for attribute "longitude" and runs the __str__ method for object with lowest number for "longitude".
#
# parameter1 an_arrray     An array with objects that has the attribute "longitude".
# return: None
          
def southernPlace(an_array):
    all_places_sorted = sorted(an_array, key=attrgetter('longitude')) 
    print("However, the most southern place is " + str(all_places_sorted[0]) + ". If you want to search for another location, please restart the program.")
    

class Place:
    '''Creates a class with attributes; name, description, latitude, longitude, date'''

    def __init__(self, name, description, latitude, longitude, date):
        self.name = name.strip()
        self.description = description.strip()
        self.latitude = latitude.strip()
        self.longitude = longitude.strip()
        self.date = date.strip()


    def __str__(self):
        '''Returns a string of the name and description of the object'''
        return  str(self.name)+ ", often refferd to as " +str(self.description)

    def getName(self):
        '''Returns the name of the object'''
        return self.name

    def getLongitude(self):
        '''Returns the longitude of the object'''
        return int(self.longitude)

    def getDate(self):
        """Returns the Date of the object"""
        return int(self.date)
        
        
    

def main():
    all_places = readFile("geodataCH.txt")
    intext = input("Welcome to Locator! \n You can search for a location and get information about it. As a bonus, we'll throw in the name of the most southern place.\n Type in a geografic location: ")
    findPlace(intext, all_places)
    southernPlace(all_places)
    

main()
