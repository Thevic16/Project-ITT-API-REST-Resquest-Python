# Import picamara from PiCamara module.
from picamera import PiCamera
# Importing time.
import time
# Importing base64 (encoding and decoding functionality).
import base64
# Import requests to make HTTP requests.
import requests
# Import date class from datetime module.
from datetime import date
# Import the entire datetime module.
from datetime import datetime
#Import geocoder module
import geocoder

#PiCamara -----------------------------------------------------------------------------------

camera = PiCamera() #Start PiCamara.
camera.resolution = (460, 340) #setup resolution
time.sleep(2) # Delay to give time to the module to start.
camera.capture("/home/pi/Pictures/fallEvent.jpg") #Capture a image and then save it.

#Base64 encode and decode -------------------------------------------------------------------

image = open('/home/pi/Pictures/fallEvent.jpg', 'rb') #Open the image from the path saved before.
image_read = image.read()
image_64_encode = base64.b64encode(image_read) #Encode the image in bytes in format Base64.
photo = image_64_encode.decode('ascii') #Decode the image from bytes Base64 to text Base64.
print(photo) #check that everything is ok.


#Preparing to obtain hour.
dt = datetime.now()

#Preparing to obtain localization
myloc = geocoder.ip('me') #Get coordinate base on ip address. 


# Make HTTP request to the API-REST aplication of the project. 
response = requests.post('http://10.0.0.251:7000/api/FallEvent', json ={
        "username": "usuariosilla1",
        "photo": "data:image/jpeg;base64,"+photo,
        "latitude": myloc.lat,
        "longitude": myloc.lng,
        "dateTime": str(date.today()),
        "hour": dt.strftime("%H:%M")
    })


print(response.json())
