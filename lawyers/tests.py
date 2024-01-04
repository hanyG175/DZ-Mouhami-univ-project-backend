from django.test import TestCase
import requests ,os
# Create your tests here.
response = requests.get("https://avocatalgerien.com/wp-content/uploads/2015/01/avocat001-230x230.jpg")
with open('C:/Users/LENOVO/Code/GLPROJECT/backend/media/photos/temp_image.jpg', 'ab') as f:
    f.write(response.content)
    os.startfile("temp_image.jpg")
