import os
import pyfiglet as pf
import dockerStuff
def infrastructures():

    infraBanner = pf.figlet_format("Infrasture as CODE")
    print(infraBanner)
    while True:
        os.system("tput setaf 3")
        print("""
    \t\t\t[ 1 ]: setup WORDPRESS + MARIADB
    \t\t\t[ 2 ]: setup WEBTHINGS GATEWAY IOT
    \t\t\t[ 3 ]: setup NEXTCLOUD + MARIADB
    \t\t\t[ 4 ]: setup HEROKU CLOUD PLATFORM
    \t\t\t[ 5 ]: Back
    \t\t\t[ 0 ]: Exit
    """)
        os.system("tput setaf 7")

        option = int(input("PLEASE ENTER YOUR CHOICE:  "))

        if option ==1:
            print("""
	    \t\t\t[ 1 ]: IF you have Images pulled already
        \t\t\t[ 2 ]: To Download or Pull the Images
        """)
            optionImage1 = int(input("ENTER YOUR CHOICE: "))
            if optionImage1 ==1:
                os.system("systemctl start docker")
                os.system("docker-compose down")
                os.system("docker-compose -f wordpress.yml up")
            elif optionImage1 ==2:
                dockerStuff.dockerStuff()
            else:
                print("Wrong Input")

        
        elif option ==2:
            print("""
	    \t\t\t[ 1 ]: IF you the Images pulled already
        \t\t\t[ 2 ]: To Download or Pull the Images
        """)
            optionImage1 = int(input("ENTER YOUR CHOICE: "))
            if optionImage1 ==1:
                os.system("systemctl start docker")
                os.system("docker run \
                -d \
                -e TZ=Asia/Kolkata \
                -v /path/to/shared/data:/home/node/.mozilla-iot \
                --log-opt max-size=1m \
                --log-opt max-file=10 \
                --name webthings-gateway \
                mozillaiot/gateway:latest")
            
            elif optionImage1 ==2:
                dockerStuff.dockerStuff()
            else:
                print("Wrong Input")
        
        elif option ==3:
            print("""
	    \t\t\t[ 1 ]: IF you the Images pulled already
        \t\t\t[ 2 ]: To Download or Pull the Images
        """)
            optionImage1 = int(input("ENTER YOUR CHOICE: "))
            if optionImage1 ==1:
                os.system("systemctl start docker")
                os.system("docker-compose down")
                os.system("docker-compose -f nextCloud.yml up")
            elif optionImage1 ==2:
                dockerStuff.dockerStuff()
            else:
                print("Wrong Input")
        
        elif option ==4:
            print("""
	    \t\t\t[ 1 ]: IF you the Images pulled already
        \t\t\t[ 2 ]: To Download or Pull the Images
        """)
            optionImage1 = int(input("ENTER YOUR CHOICE: "))
            if optionImage1 ==1:
                os.system("systemctl start docker")
                os.system("systemctl start docker")
                os.system("docker-compose down")
                os.system("docker-compose -f heroku.yml up --build")
            elif optionImage1 ==2:
                dockerStuff.dockerStuff()
            else:
                print("Wrong Input")

        
        elif option ==5:
            break
        elif option ==0:
            exit()
        else:
            print("\t\t\t....PLEASE ENTER CORRECT OPTION FROM MENU....")
            
        

if __name__ == "__main__":
	infrastructures()