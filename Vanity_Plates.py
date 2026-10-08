plate = input("Validate: ").strip()
valid = True
num = False

if len(plate) < 2 or len(plate) > 6:
    valid = False
else:
    for i in range(2):
        if not(plate[i].isalpha()):
            valid = False
            break
    if valid and len(plate) > 2:
        for e in range(2,len(plate)):
            if num:
                 if not plate[e].isdecimal():
                    valid = False
                    break 
            else:    
                if plate[e].isdecimal():
                    if plate[e] == "0":
                        valid = False
                        break
                    else:
                        num = True
                elif not plate[e].isalpha():
                    valid = False
                    break 

if valid:
    print("Valid")
else:
    print("Invalid")