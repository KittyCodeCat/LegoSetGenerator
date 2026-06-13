from collections import Counter

def parse_file(file):
    with file as file:
        steps = [] 
        for line in file:
            line = line.strip()
            if line.startswith("1") and line.endswith(".DAT"):
                # Creates a tuple of (partID, color, position, rotation)
                # in format (part ID, color, (x,y,z), [[a,b,c],[d,e,f],[g,h,i]])
                parts = line.split()
                parts.pop(0) # remove 1
                color = parts[0] # color
                x,y,z = float(parts[1]), float(parts[2]), float(parts[3]) # x, y, z coordinates
                rotation = [[parts[4], parts[5], parts[6]], 
                            [parts[7], parts[8], parts[9]], 
                            [parts[10], parts[11], parts[12]]] # rotation matrix
                partID = parts[13] # part ID

                brick = {"partID": partID,
                        "color": color,
                        "coordinates": (x, y, z),
                        "rotation": rotation}
                steps.append(brick)

    return steps

def process_description():
    with open("C:/Users/aberg/Documents/VS_codes/Home/parts.txt", encoding="utf-8") as file:
        descriptions = {} # partID : description
        for line in file:
            line = line.strip()
            if line:
                partID, description = line.split(" ", 1)
                partID = partID[:-4] # remove .dat
                description = description.strip() 
                descriptions[partID] = description
        return descriptions

def get_description(partID, descriptions):
    return descriptions.get(partID, "Description not found")

def print_counter(steps):
    head = 5
    counts = Counter(b["partID"] for b in steps)
    sort = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    descriptions = process_description()
    print(f"Total bricks: {len(steps)}  | Unique parts: {len(counts)}\n")
    for i in range(head):
        id = (sort[i][0])[:-4]
        print(f"{get_description(id, descriptions)} ({id}.dat): {sort[i][1]}")

def main():
    with open("C:/Users/aberg/Documents/VS_codes/Home/10022-1_Sleeping-Ca.txt") as file:
        steps = parse_file(file)
        print_counter(steps)

main()
