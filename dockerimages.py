import pyfiglet as pf
import os

def dockerimages():
    while True:


        dockerimagesbanner = pf.figlet_format("Docker Images")
        print(dockerimagesbanner)

        print("""
        \t\t\t[ 1 ]: Download wordpress:latest
        \t\t\t[ 2 ]: Download mariadb:latest
        \t\t\t[ 3 ]: Download webthings-gateway IOT
        \t\t\t[ 4 ]: Download heroku
        \t\t\t[ 5 ]: Download nextcloud
        \t\t\t[ 6 ]: Back
        \t\t\t[ 0 ]: Exit
        """)
        os.system("systemctl start docker")
        option = int(input("PLEASE ENTER YOUR CHOICE: "))

        if option == 1:
            os.system("docker pull wordpress")
        elif option == 2:
            os.system("docker pull mariadb")
        elif option == 3:
            os.system("docker pull mozillaiot/gateway")
        elif option == 4:
            os.system("docker pull heroku/heroku")
        elif option == 5:
            os.system("docker pull nextcloud")
        elif option == 6:
            break
        elif option == 0:
            exit()
        else:
            print("PLEASE ENTER CORRECT OPTION")
    
if __name__ == "__main__":
    dockerimages()
    