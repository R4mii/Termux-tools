#!/usr/bin/env python3
import os
import sys
import subprocess
from time import sleep

def print_banner():
    """Print a colorful banner for the tool."""
    os.system('clear')
    
    print("=" * 70)
    print("""\033[1;91m
    ████████╗███████╗██████╗ ███╗   ███╗██╗   ██╗██╗  ██╗
    ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║   ██║╚██╗██╔╝
       ██║   █████╗  ██████╔╝██╔████╔██║██║   ██║ ╚███╔╝ 
       ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║   ██║ ██╔██╗ 
       ██║   ███████╗██║  ██║██║ ╚═╝ ██║╚██████╔╝██╔╝ ██╗
       ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝
                                                         
           ████████╗ ██████╗  ██████╗ ██╗     ███████╗
           ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
              ██║   ██║   ██║██║   ██║██║     ███████╗
              ██║   ██║   ██║██║   ██║██║     ╚════██║
              ██║   ╚██████╔╝╚██████╔╝███████╗███████║
              ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝                                                
    \033[0m""")
    print("=" * 70)
    print("\033[1;36m" + "Termux Tools Installer - Enhanced Version" + "\033[0m")
    print("=" * 70)

def print_success_banner():
    """Print success banner after completion."""
    print("""\033[1;92m
    ██╗███╗   ██╗███████╗████████╗ █████╗ ██╗     ██╗      █████╗ ████████╗██╗ ██████╗ ███╗   ██╗
    ██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║     ██║     ██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
    ██║██╔██╗ ██║███████╗   ██║   ███████║██║     ██║     ███████║   ██║   ██║██║   ██║██╔██╗ ██║
    ██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║     ██║     ██╔══██║   ██║   ██║██║   ██║██║╚██╗██║
    ██║██║ ╚████║███████║   ██║   ██║  ██║███████╗███████╗██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║
    ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                                                                                             
         ██████╗ ██████╗ ███╗   ███╗██████╗ ██╗     ███████╗████████╗███████╗██████╗          
        ██╔════╝██╔═══██╗████╗ ████║██╔══██╗██║     ██╔════╝╚══██╔══╝██╔════╝██╔══██╗         
        ██║     ██║   ██║██╔████╔██║██████╔╝██║     █████╗     ██║   █████╗  ██║  ██║         
        ██║     ██║   ██║██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝     ██║   ██╔══╝  ██║  ██║         
        ╚██████╗╚██████╔╝██║ ╚═╝ ██║██║     ███████╗███████╗   ██║   ███████╗██████╔╝         
         ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝   ╚═╝   ╚══════╝╚═════╝          
    \033[0m""")

def run_command(command, description):
    """Execute a command with progress indication and error handling."""
    print(f"\n\033[1;33m[*] {description}...\033[0m")
    
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"\033[1;32m[✓] Successfully completed: {description}\033[0m")
            return True
        else:
            print(f"\033[1;31m[✗] Failed: {description}\033[0m")
            print(f"\033[1;31m    Error: {result.stderr}\033[0m")
            return False
    except Exception as e:
        print(f"\033[1;31m[✗] Error executing: {description}\033[0m")
        print(f"\033[1;31m    {str(e)}\033[0m")
        return False

def install_packages():
    """Install all required packages with error handling and progress indication."""
    # Update repositories first
    update_commands = [
        "apt update",
        "apt upgrade -y"
    ]
    
    # List of packages to install
    packages = [
        "php", "python", "python2", "git", "golang", "host", "nano",
        "hydra", "cmatrix", "figlet", "wget", "python2-dev",
        "cowsay", "toilet", "ruby", "curl", "unzip", "openssh",
        "tor", "net-tools", "unrar", "clang", "w3m", "proot"
    ]
    
    # Optional packages that might not be available in all repositories
    optional_packages = [
        "wireshark", "havij", "metasploit"
    ]
    
    # Python packages to install via pip
    pip_packages = [
        "requests"
    ]
    
    # Ruby gems to install
    gems = [
        "lolcat"
    ]
    
    # Run update commands
    print("\n\033[1;34m[+] Updating system repositories...\033[0m")
    for cmd in update_commands:
        run_command(cmd, f"Running {cmd}")
    
    # Install regular packages
    print("\n\033[1;34m[+] Installing main packages...\033[0m")
    for pkg in packages:
        run_command(f"pkg install {pkg} -y", f"Installing {pkg}")
    
    # Try installing optional packages
    print("\n\033[1;34m[+] Attempting to install optional packages...\033[0m")
    for pkg in optional_packages:
        run_command(f"apt install {pkg} -y", f"Installing {pkg}")
    
    # Install Python packages
    print("\n\033[1;34m[+] Installing Python packages...\033[0m")
    for pkg in pip_packages:
        run_command(f"pip install {pkg} && pip2 install {pkg}", f"Installing pip package {pkg}")
    
    # Install Ruby gems
    print("\n\033[1;34m[+] Installing Ruby gems...\033[0m")
    for gem in gems:
        run_command(f"gem install {gem}", f"Installing Ruby gem {gem}")
    
    # Try installing Metasploit Framework
    print("\n\033[1;34m[+] Installing Metasploit Framework...\033[0m")
    run_command("apt install unstable-repo -y", "Adding unstable repository")
    run_command("pkg install metasploit -y", "Installing Metasploit Framework")

def main():
    """Main function to run the script."""
    # Check if running as root (though not typically needed for Termux)
    if os.geteuid() == 0 and not os.path.exists("/data/data/com.termux"):
        print("\033[1;33m[!] Running as root. This is not typically needed in Termux.\033[0m")
    
    # Print welcome banner
    print_banner()
    
    print("\033[1;33m[!] This script will install various penetration testing tools in Termux.\033[0m")
    print("\033[1;33m[!] Some tools might not be available in all repositories.\033[0m")
    print("\033[1;33m[!] Installation may take a while depending on your internet connection.\033[0m")
    
    # Confirm installation
    while True:
        choice = input("\n\033[1;36m[?] Do you want to continue? (y/n): \033[0m").lower()
        if choice == 'y':
            break
        elif choice == 'n':
            print("\033[1;31m[!] Installation cancelled by user.\033[0m")
            sys.exit(0)
        else:
            print("\033[1;31m[!] Invalid choice. Please enter 'y' or 'n'.\033[0m")
    
    # Install packages
    print("\n\033[1;34m[+] Starting installation...\033[0m")
    install_packages()
    
    # Print success message
    print_success_banner()
    print("\n\033[1;32m[✓] Installation completed!\033[0m")
    print("\033[1;33m[!] Some packages might not have been installed if they're not available in your repositories.\033[0m")
    print("\033[1;33m[!] Check the output above for any errors.\033[0m")
    print("\n\033[1;36m[*] Enjoy your new tools!\033[0m")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\033[1;31m[!] Installation cancelled by user (Ctrl+C).\033[0m")
        sys.exit(1)
    except Exception as e:
        print(f"\n\033[1;31m[!] An unexpected error occurred: {str(e)}\033[0m")
        sys.exit(1)
