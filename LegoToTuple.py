file = open("C:/Users/aberg/Documents/VS_codes/Home/10022-1_Sleeping-Ca.txt")

with open("C:/Users/aberg/Documents/VS_codes/Home/10022-1_Sleeping-Ca.txt") as file:
    steps = [] 
    for line in file:
        line = line.strip()
        if line.startswith("1") and line.endswith(".DAT"):
            # Creates a tuple of (partID, color, position, rotation)
            # in format (part ID, color, (x,y,z), [[a,b,c],[d,e,f],[g,h,i]])
            parts = line.split()
            parts.pop(0) # remove 1
            color = parts[0] # color
            coordinates = (parts[1], parts[2], parts[3]) # x, y, z coordinates
            rotation = [[parts[4], parts[5], parts[6]], 
                        [parts[7], parts[8], parts[9]], 
                        [parts[10], parts[11], parts[12]]] # rotation matrix
            partID = parts[13] # part ID

            brick = {"partID": partID,
                     "color": color,
                     "coordinates": coordinates,
                     "rotation": rotation}
            steps.append(brick)

if steps:
    print(steps[0])
else:
    print("Inga rader matchade kriterierna.")
