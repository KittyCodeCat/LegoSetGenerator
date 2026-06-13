file = open("LegoFile.txt")
steps = [] 

for line in file:
    if line.startswith("1") and line.endswith(".DAT"):
        # Creates a tuple of (partID, position, rotation, color)
        # in format (partID, color, (x,y,z), [[a,b,c],[d,e,f],[g,h,i]], color)
        parts = line.split()
        parts.pop(0) # remove 1
        color = parts[0] # color
        coordinates = (parts[1], parts[2], parts[3]) # x, y, z coordinates
        rotation = [[parts[4], parts[5], parts[6]], 
                    [parts[7], parts[8], parts[9]], 
                    [parts[10], parts[11], parts[12]]] # rotation matrix
        partID = parts[13] # part ID
        brick = (partID, color, coordinates, rotation)
        steps.append(brick)

file.close()
print(steps)