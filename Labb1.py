import time
import sys
import os
from operator import attrgetter

# Reads from .txt-file and extracts relevant lines which becomes attributes for objects that are
#placed in an array.
#
# return: the_array_list        List of objects created based on content of .txt file.

def readFile():
    with open("geodataSW.txt", "r", encoding="utf-8") as f:
        the_array_list = []
        the_reset = 0
        a= the_reset
        for line in f:
            if line.strip() != "" and not line.startswith("#"):
                a+=1
                
                if a == 1:
                    name = line

                elif a == 2:
                    description = line

                elif a == 3:
                    latitude = line

                elif a == 4:
                    longitude = line

                elif a == 5:
                    date = line
                    the_array_list.append(Place(name, description, latitude, longitude, date))
                    a = the_reset
               
    return the_array_list


# Matches the users input with object in list and runs the __str__-method for said object.
#If input does not match any object, the program will shutdown.
#
# parameter1 an_intext      User input that is matched with attribute "name" of objects in an_array. 
# parameter2 an_array       An array with objects.
# return: None

def findPlace(an_intext, an_array):
    the_time_start = time.time()
    for x in an_array:
        if x.getName().lower() == an_intext.lower(): 
            the_time_end = time.time()
            the_time_passed = the_time_end-the_time_start 
            return x, the_time_passed
    return None, None

    


# Sorts an array with objects for attribute "longitude" and runs the __str__ method for object with lowest number for "longitude".
#
# parameter1 an_arrray     An array with objects that has the attribute "longitude".
# return: None
          
def southernPlace(an_array):
    all_places_sorted = sorted(an_array, key=attrgetter('longitude')) 
    print("However, the most southern place is " + str(all_places_sorted[0]))
    

class Place:
    '''Creates a class with attributes; name, description, latitude, longitude, date'''

    def __init__(self, name, description, latitude, longitude, date):
        self.name = name.strip()
        self.description = description.strip()
        self.latitude = latitude.strip()
        self.longitude = longitude.strip()
        self.date = date.strip()


    def getName(self):
        '''Returns the name of the object'''
        return self.name

    def getLongitude(self):
        '''Returns the longitude of the object'''
        return int(self.longitude)
        
        
    def __str__(self):
        '''Returns a string of the name and description of the object'''
        return  str(self.name)+ ", often refferd to as " +str(self.description)

def main():
    all_places = readFile()
    intext = input("Welcome to Locator! \n You can search for a location and get information about it.\n Type in a geografic location: ")
    place_found = findPlace(intext, all_places)[0]
    time_taken = findPlace(intext, all_places)[1]
    while place_found is None:
        intext = input("Welcome to Locator! \n You can search for a location and get information about it.\n Type in a geografic location: ")
        place_found = findPlace(intext, all_places)[0]
        print("Hej manne")
    else:
        print(place_found)
        print(time_taken)
        southernPlace(all_places)

main()
