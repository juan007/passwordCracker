import random
import time

def generatePassword(glyphs):
    # generate the password to crack (3 glyphs long)
    passwordToCrack = ""
    for n in range(3):
        # add a glyph to the password
        passwordToCrack = passwordToCrack + glyphs[random.randint(0, len(glyphs))]

    print("PASSWORD TO CRACK:", passwordToCrack)
    time.sleep(2)
    return passwordToCrack

def crack(glyphs,passwordToCrack):
    
    # to print attempt 
    counter=1

    for n in range(0,len(glyphs)):
        for o in range(0,len(glyphs)):
            for p in range(0,len(glyphs)):
                # create attempt
                attempt = glyphs[n]+glyphs[o]+glyphs[p]
                print("Crack Attempt #"+str(counter)+":"+attempt)
                counter +=1
                # if found print and exit 
                if(attempt == passwordToCrack):
                    print("Password Cracked("+attempt+")!")
                    
                    return

def main():
    # list of possible glyphs that make up the password
    glyphs = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]
    
    passwordToCrack = generatePassword(glyphs)

    # write the code to crack the password here!
    # ...
    crack(glyphs,passwordToCrack)

main()