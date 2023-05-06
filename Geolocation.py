# this is for fun only...
import opencage.geocoder
import tkinter as tk
from tkinter import simpledialog
from geopy.distance import geodesic

# Enter your OpenCage Geocoder API key here
key = ''

# Create a Tkinter dialog to prompt the user for the starting and destination cities, and countries, as well as the speed
root = tk.Tk()
root.withdraw()

# Prompt the user for the starting location
starting_country = simpledialog.askstring('Enter Starting Country', 'Enter the starting country:')
starting_city = simpledialog.askstring('Enter Starting City', 'Enter the starting city:')
starting_address = f"{starting_city}, {starting_country}"

# Prompt the user for the destination location
destination_country = simpledialog.askstring('Enter Destination Country', 'Enter the destination country:')
destination_city = simpledialog.askstring('Enter Destination City', 'Enter the destination city:')
destination_address = f"{destination_city}, {destination_country}"

speed = simpledialog.askinteger('Enter Speed', 'Enter the speed in km/h:', minvalue=1)

# Geocode the starting address to get the latitude and longitude
geocoder = opencage.geocoder.OpenCageGeocode(key)
result = geocoder.geocode(starting_address)
start_lat = result[0]['geometry']['lat']
start_lng = result[0]['geometry']['lng']

# Reverse geocode the starting coordinates to get the location information
result = geocoder.reverse_geocode(start_lat, start_lng)

# Extract the relevant location information from the result
start_formatted_address = result[0]['formatted']
start_city = result[0]['components']['city']
start_country = result[0]['components']['country']

# Print the starting location information
print('Starting Address:', start_formatted_address)
print('City:', start_city)
print('Country:', start_country)

# Geocode the destination address to get the latitude and longitude
result = geocoder.geocode(destination_address)
dest_lat = result[0]['geometry']['lat']
dest_lng = result[0]['geometry']['lng']

# Reverse geocode the destination coordinates to get the location information
result = geocoder.reverse_geocode(dest_lat, dest_lng)

# Extract the relevant location information from the result
dest_formatted_address = result[0]['formatted']
dest_city = result[0]['components']['city']
dest_country = result[0]['components']['country']

# Print the destination location information
print('Destination Address:', dest_formatted_address)
print('City:', dest_city)
print('Country:', dest_country)

# Calculate the distance between the starting and destination coordinates
distance = geodesic((start_lat, start_lng), (dest_lat, dest_lng)).km
print('Distance from', start_formatted_address, 'to', dest_formatted_address, ':', distance, 'km')

# Calculate the time taken to travel the distance at the given speed from the starting location
time = distance / speed
print('Time taken to travel', distance, 'km at', speed, 'km/h from', start_formatted_address, 'to', dest_formatted_address, ':', time, 'hours')
