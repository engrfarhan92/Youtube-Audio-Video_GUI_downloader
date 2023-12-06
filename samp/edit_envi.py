import os

# print all environment variables as a dictionary
#print(os.environ)

# get LANG variable without KeyError
#pathi = os.environ.get("Path")
x = 'C:\\ffmpeg\\bin'
pathi = os.environ.get('Path') +  x
os.environ['Path'] = pathi
print(os.environ.get('Path'))




#print(os.environ.get('Path'))