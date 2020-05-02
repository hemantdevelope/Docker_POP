import pyfiglet as pf
import dockerStuff
import infrastrutures
banner1 = pf.figlet_format("DOCKER : POP")
print(banner1)
banner2 = pf.figlet_format("Project of Projects")
print(banner2)


while True:

    print("""
    \t\t[ 1 ]: Basic Docker Stuff
    \t\t[ 2 ]: Setup Different Infrastructure
    \t\t[ 0 ]: Exit 
    """)

    option = int(input("Please Enter Your choice: "))
    import os
    if option == 1:
        dockerStuff.dockerStuff()
    elif option == 2:
        infrastrutures.infrastructures()
    elif option == 0:
        exit()
        
        
    else:
        os.system("clear")
        print("\t\t\t....PLEASE ENTER THE NUMBER FORM MENU....")

os.system("reset")
