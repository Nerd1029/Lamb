import socket; import sys; import os; import platform; import subprocess

try:
    import colorama
except ModuleNotFoundError:
    subprocess.run(["pip", "install", "colorama"])

#locations:
#sys/
    #sys/info
    #sys/version
#account/
    #account/user
    #account/info

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
sysos = platform.system()

user = f"{ip}"
version = "v0.0.1"
sysinfo = f"version={version}\nuser={user}\nos={sysos}"

while True:
    cmd = input(f"lamb/os:{sysos}/user:{ip}> ").lower()

    lamb = f"Welcome to Lamb!\nThe version that you are using is {version}!\nThe user (called by their IP) is: {ip}"

    if cmd == "help":
        print("As of this version there is no proper help log :(")
    
    elif cmd == "lamb --sys/version" or cmd == "lamb -s/v":
        print(version)
    
    elif cmd == "lamb --account/user" or cmd == "lamb -a/user":
        print(user)

    elif cmd == "lamb":
        print(lamb)
    
    elif cmd == "lamb --sys/info" or cmd == "lamb -s/info":
        print(f"sys info:\n{sysinfo}")

    elif cmd == "lamb --list text/colors" or cmd == "lamb -l t/c":
        print(f"{colorama.Fore.RED}RED\n{colorama.Fore.BLUE}BLUE\n{colorama.Fore.YELLOW}YELLOW\n{colorama.Fore.GREEN}GREEN\n{colorama.Fore.BLACK}BLACK\n{colorama.Fore.CYAN}CYAN\n{colorama.Fore.MAGENTA}MAGENTA\n{colorama.Fore.RESET}RESET\nEnter your choice here: ")
    
    elif cmd == "lamb --config text/color" or cmd == "lamb -c t/c":
        color = input(f"Choose a color from these:\n{colorama.Fore.RED}RED\n{colorama.Fore.BLUE}BLUE\n{colorama.Fore.YELLOW}YELLOW\n{colorama.Fore.GREEN}GREEN\n{colorama.Fore.BLACK}BLACK\n{colorama.Fore.CYAN}CYAN\n{colorama.Fore.MAGENTA}MAGENTA\n{colorama.Fore.RESET}RESET\nEnter your choice here: ").lower()
        
        if color == "red":
            print(f"{colorama.Fore.RED}The new terminal color is red!")
        elif color == "blue":
            print(f"{colorama.Fore.BLUE}The new terminal color is blue!")
        elif color == "yellow":
            print(f"{colorama.Fore.YELLOW}The new terminal color is yellow!")
        elif color == "green":
            print(f"{colorama.Fore.GREEN}The new terminal color is green!")
        elif color == "black":
            print(f"{colorama.Fore.BLACK}The new terminal color is black!")
        elif color == "cyan":
            print(f"{colorama.Fore.CYAN}The new terminal color is cyan!")
        elif color == "magenta":
            print(f"{colorama.Fore.MAGENTA}The new terminal color is magenta!")
        elif color == "reset":
            print(f"{colorama.Fore.RESET}The terminal color cas been reset!")

    elif cmd == "quit":
        sys.exit("Session killed.")

    elif cmd == "clear":
        os.system('clear')

    else:
        print("That command is invalid :(")