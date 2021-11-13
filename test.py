import requests

# This python file is to test the API and to query the data provided

# Base URL, the location of the API
BASE = "http://127.0.0.1:5000/"

# Test with ATN Provider
response = requests.get(BASE + "shows/ATN")
print(response.json())
print('\n')

# Test with ATN Provider page 1
response = requests.get(BASE + "shows/ATN/1")
print(response.json())
print('\n')

# Test with ATN Provider page 2
response = requests.get(BASE + "shows/ATN/2")
print(response.json())
print('\n')

# Test with ATN Provider page 3
response = requests.get(BASE + "shows/ATN/3")
print(response.json())
print('\n')

# -----------------------------------------------------------------------

# Test with SH Provider
response = requests.get(BASE + "shows/SH")
print(response.json())
print('\n')

# Test with SH Provider page 1
response = requests.get(BASE + "shows/SH/1")
print(response.json())
print('\n')

# Test with SH Provider page 2
response = requests.get(BASE + "shows/SH/2")
print(response.json())
print('\n')

# Test with SH Provider page 3
response = requests.get(BASE + "shows/SH/3")
print(response.json())
print('\n')

# -----------------------------------------------------------------------

# Test with CVOD Provider
response = requests.get(BASE + "shows/CVOD")
print(response.json())
print('\n')

# Test with CVOD Provider page 1
response = requests.get(BASE + "shows/CVOD/1")
print(response.json())
print('\n')

# Test with CVOD Provider page 2
response = requests.get(BASE + "shows/CVOD/2")
print(response.json())
print('\n')

# Test with CVOD Provider page 3
response = requests.get(BASE + "shows/CVOD/3")
print(response.json())
print('\n')

