picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

image = str() #creating a string variable

for items in picture:
    for item in items:
        if(item is 1):
            image += '*'
        else:
            image += ' '
    #concat the string with new line for each items in the string
    image = image + '\n'

#print the output
print(image)
