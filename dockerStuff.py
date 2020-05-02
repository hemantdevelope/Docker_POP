import os
import pyfiglet as pf
import subprocess
import dockerimages
def dockerStuff():

	bannerDockerStuff = pf.figlet_format("BASIC DOCKER:")
	print(bannerDockerStuff)
	while True:
		os.system("tput setaf 3")
		print("""
		\t\t\t[ 1 ]: Install Docker
		\t\t\t[ 2 ]: Install Docker-compose
		\t\t\t[ 3 ]: Download Different Useful images
		\t\t\t[ 4 ]: Back
		\t\t\t[ 0 ]: Exit 
		""")
		os.system("tput setaf 7")

		option = int(input("Please Enter Your choice: "))

		if option == 1:
			string1 = subprocess.getoutput("rpm -q docker-ce | cut -c 1-9")
			if string1 == "docker-ce":
			    print("Docker Requirement is Already Fullfilled")
			else:
				os.system("echo -e '[docker]\nbaseurl=https://download.docker.com/linux/centos/7/x86_64/stable/\ngpgcheck=0' > /etc/yum.repos.d/docker.repo && dnf install docker-ce -y")
		elif option == 2:
			os.system("pip install docker-compose")
		elif option == 3:
			dockerimages.dockerimages()
		elif option == 4:
			break
		elif option == 0:
			exit()
			

if __name__ == "__main__":
	dockerStuff()