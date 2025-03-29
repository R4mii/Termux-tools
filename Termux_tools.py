#!/usr/bin/env python3
import os
import sys
import subprocess
from time import sleep
import platform
import random
from datetime import datetime

def print_banner():
    """Print a colorful banner for the tool."""
    os.system('clear')
    
    # Random color selection for banner
    colors = ['\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;34m', '\033[1;35m', '\033[1;36m']
    color = random.choice(colors)
    
    print("=" * 70)
    print(f"{color}                                                                                      ")
    print(f"████████╗███████╗██████╗ ███╗   ███╗██╗   ██╗██╗  ██╗    ██████╗ ██████╗  ██████╗          ")
    print(f"╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║   ██║╚██╗██╔╝    ██╔══██╗██╔══██╗██╔═══██╗         ")
    print(f"   ██║   █████╗  ██████╔╝██╔████╔██║██║   ██║ ╚███╔╝     ██████╔╝██████╔╝██║   ██║         ")
    print(f"   ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║   ██║ ██╔██╗     ██╔═══╝ ██╔══██╗██║   ██║         ")
    print(f"   ██║   ███████╗██║  ██║██║ ╚═╝ ██║╚██████╔╝██╔╝ ██╗    ██║     ██║  ██║╚██████╔╝         ")
    print(f"   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝    ╚═╝     ╚═╝  ╚═╝ ╚═════╝          ")
    print(f"                                                                                      \033[0m")
    print("=" * 70)
    print(f"\033[1;36m{'Termux Advanced Tools Installer v2.0':^70}\033[0m")
    print(f"\033[1;33m{'Created by R4mii':^70}\033[0m")
    print("=" * 70)
    
    # Add fancy timestamp
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\033[1;37m{'Execution time: ' + current_time:^70}\033[0m")
    print("=" * 70)

def print_category(category_name):
    """Print a styled category header."""
    print(f"\n\033[1;35m[+] {category_name}\033[0m")
    print("─" * 70)

def print_success_banner():
    """Print success banner after completion."""
    os.system('clear')
    print("""\033[1;92m
  ██████╗ ██████╗ ███╗   ███╗██████╗ ██╗     ███████╗████████╗███████╗██████╗ ██╗
 ██╔════╝██╔═══██╗████╗ ████║██╔══██╗██║     ██╔════╝╚══██╔══╝██╔════╝██╔══██╗██║
 ██║     ██║   ██║██╔████╔██║██████╔╝██║     █████╗     ██║   █████╗  ██║  ██║██║
 ██║     ██║   ██║██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝     ██║   ██╔══╝  ██║  ██║╚═╝
 ╚██████╗╚██████╔╝██║ ╚═╝ ██║██║     ███████╗███████╗   ██║   ███████╗██████╔╝██╗
  ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝   ╚═╝   ╚══════╝╚═════╝ ╚═╝
\033[0m""")
    
    # Get installed packages count
    try:
        result = subprocess.run("dpkg --get-selections | wc -l", shell=True, capture_output=True, text=True)
        pkg_count = result.stdout.strip()
    except:
        pkg_count = "many"
    
    print("\n" + "=" * 70)
    print(f"\033[1;32m{'✓ Installation completed successfully!':^70}\033[0m")
    print(f"\033[1;32m{f'✓ You now have {pkg_count} packages installed':^70}\033[0m")
    print(f"\033[1;32m{'✓ Your Termux is now equipped with advanced tools':^70}\033[0m")
    print("=" * 70)

def run_command(command, description, silent=False):
    """Execute a command with progress indication and error handling."""
    if not silent:
        print(f"\n\033[1;33m[*] {description}...\033[0m")
    
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            if not silent:
                print(f"\033[1;32m[✓] Successfully completed: {description}\033[0m")
            return True
        else:
            if not silent:
                print(f"\033[1;31m[✗] Failed: {description}\033[0m")
                print(f"\033[1;31m    Error: {result.stderr}\033[0m")
            return False
    except Exception as e:
        if not silent:
            print(f"\033[1;31m[✗] Error executing: {description}\033[0m")
            print(f"\033[1;31m    {str(e)}\033[0m")
        return False

def check_termux():
    """Check if running in Termux environment."""
    return os.path.exists("/data/data/com.termux") or "termux" in platform.release().lower()

def setup_directories():
    """Create necessary directories for tools."""
    directories = [
        os.path.expanduser("~/tools"),
        os.path.expanduser("~/wordlists"),
        os.path.expanduser("~/payloads"),
        os.path.expanduser("~/projects")
    ]
    
    print_category("Setting up directories")
    for directory in directories:
        if not os.path.exists(directory):
            try:
                os.makedirs(directory)
                print(f"\033[1;32m[✓] Created directory: {directory}\033[0m")
            except Exception as e:
                print(f"\033[1;31m[✗] Failed to create directory {directory}: {str(e)}\033[0m")

def update_system():
    """Update system repositories and packages."""
    print_category("Updating System")
    update_commands = [
        "apt update -y",
        "apt upgrade -y",
        "pkg update -y",
        "pkg upgrade -y"
    ]
    
    for cmd in update_commands:
        run_command(cmd, f"Running {cmd}")

def install_base_packages():
    """Install essential base packages."""
    print_category("Installing Base Packages")
    
    base_packages = [
        "python", "python2", "python-dev", "python2-dev",
        "git", "wget", "curl", "zip", "unzip", "tar",
        "nano", "vim", "openssh", "termux-api", "proot",
        "termux-tools", "build-essential", "clang", "make",
        "pkg-config", "openssl", "libffi-dev", "libsodium-dev"
    ]
    
    for pkg in base_packages:
        run_command(f"pkg install {pkg} -y", f"Installing {pkg}")

def install_programming_languages():
    """Install various programming languages."""
    print_category("Installing Programming Languages")
    
    languages = [
        "php", "perl", "ruby", "golang", "rust", "nodejs",
        "lua", "swift", "dart", "kotlin", "openjdk-17"
    ]
    
    for lang in languages:
        run_command(f"pkg install {lang} -y", f"Installing {lang}")

def install_network_tools():
    """Install networking tools."""
    print_category("Installing Network Tools")
    
    network_tools = [
        "nmap", "netcat", "tcpdump", "whois", "net-tools",
        "macchanger", "mtr", "iproute2", "iputils", "tracepath",
        "dnsutils", "iptables", "sshpass", "openssh"
    ]
    
    for tool in network_tools:
        run_command(f"pkg install {tool} -y", f"Installing {tool}")

def install_security_tools():
    """Install security and penetration testing tools."""
    print_category("Installing Security Tools")
    
    # Basic security tools available through pkg
    security_tools = [
        "hydra", "sqlmap", "hashcat", "crunch", "john",
        "aircrack-ng", "nikto", "ettercap", "wireshark-gtk",
        "stunnel", "exploitdb", "metasploit", "searchsploit"
    ]
    
    # First try to install unstable repo which contains some of these tools
    run_command("pkg install unstable-repo -y", "Adding unstable repository")
    run_command("pkg install root-repo -y", "Adding root repository")
    
    # Install security tools through pkg
    for tool in security_tools:
        run_command(f"pkg install {tool} -y", f"Installing {tool}")
    
    # Install additional GitHub security tools
    github_tools = [
        {
            "name": "Nmap-Scripts",
            "repo": "https://github.com/vulnersCom/nmap-vulners.git",
            "dir": "tools/nmap-vulners",
            "install": "cp nmap-vulners.nse /data/data/com.termux/files/usr/share/nmap/scripts/ 2>/dev/null || echo 'Manual setup required'"
        },
        {
            "name": "Sherlock",
            "repo": "https://github.com/sherlock-project/sherlock.git",
            "dir": "tools/sherlock",
            "install": "pip install -r requirements.txt"
        },
        {
            "name": "XSStrike",
            "repo": "https://github.com/s0md3v/XSStrike.git",
            "dir": "tools/XSStrike",
            "install": "pip install -r requirements.txt"
        },
        {
            "name": "RouterSploit",
            "repo": "https://github.com/threat9/routersploit.git",
            "dir": "tools/routersploit",
            "install": "pip install -r requirements.txt"
        }
    ]
    
    # Clone and setup GitHub tools
    for tool in github_tools:
        tool_path = os.path.expanduser(f"~/{tool['dir']}")
        run_command(f"git clone {tool['repo']} {tool_path}", f"Cloning {tool['name']}")
        if os.path.exists(tool_path):
            run_command(f"cd {tool_path} && {tool['install']}", f"Setting up {tool['name']}")

def install_utility_tools():
    """Install utility tools to enhance Termux experience."""
    print_category("Installing Utility Tools")
    
    utility_tools = [
        "coreutils", "findutils", "htop", "bmon", "screenfetch", "neofetch",
        "figlet", "toilet", "cowsay", "cmatrix", "sl", "tree",
        "fortune", "ranger", "mc", "ncdu", "tmux", "screen",
        "ffmpeg", "imagemagick", "jq", "yq", "ack-grep", "pv",
        "strace", "ltrace", "parallel", "bat", "exa", "fzf"
    ]
    
    for tool in utility_tools:
        run_command(f"pkg install {tool} -y", f"Installing {tool}")

def install_python_packages():
    """Install useful Python packages and libraries."""
    print_category("Installing Python Packages")
    
    python_packages = [
        "requests", "bs4", "colorama", "numpy", "pandas",
        "pillow", "cryptography", "pygments", "ipython",
        "scapy", "paramiko", "pycryptodome", "pyftpdlib",
        "django", "flask", "scrapy", "selenium", "matplotlib",
        "rich", "tqdm", "psutil", "pyinstaller", "impacket"
    ]
    
    # Ensure pip is up to date
    run_command("pip install --upgrade pip", "Updating pip")
    run_command("pip2 install --upgrade pip", "Updating pip2")
    
    # Install Python packages
    for package in python_packages:
        run_command(f"pip install {package}", f"Installing {package} (Python3)")
        # Some packages might still be needed for Python2
        if package in ["requests", "colorama", "bs4", "cryptography", "scapy"]:
            run_command(f"pip2 install {package}", f"Installing {package} (Python2)", True)

def install_dev_tools():
    """Install development tools and frameworks."""
    print_category("Installing Development Tools")
    
    dev_tools = [
        "nodejs", "npm", "yarn", "ruby-dev", "rust", "golang",
        "apache2", "mariadb", "postgresql", "sqlite", "nginx",
        "composer", "gradle", "cmake", "autoconf", "automake",
        "libtool", "bison", "flex", "valgrind", "gdb"
    ]
    
    for tool in dev_tools:
        run_command(f"pkg install {tool} -y", f"Installing {tool}")
    
    # Setup common dev frameworks
    run_command("npm install -g express-generator react-native-cli @angular/cli", "Installing Node.js frameworks")
    run_command("gem install bundler jekyll sinatra rails", "Installing Ruby frameworks")
    run_command("pip install virtualenv pipenv django flask fastapi", "Installing Python frameworks")

def setup_aliases():
    """Setup useful aliases in .bashrc file."""
    print_category("Setting up Aliases")
    
    aliases = [
        "alias ll='ls -la'",
        "alias la='ls -A'",
        "alias l='ls -CF'",
        "alias cls='clear'",
        "alias py='python'",
        "alias py2='python2'",
        "alias update='pkg update && pkg upgrade'",
        "alias install='pkg install'",
        "alias search='pkg search'",
        "alias myip='curl ifconfig.me'",
        "alias ports='netstat -tulanp'",
        "alias networks='ip -c a'",
        "alias tools='cd ~/tools'",
        "alias projects='cd ~/projects'"
    ]
    
    bashrc_path = os.path.expanduser("~/.bashrc")
    
    # Check if file exists, if not create it
    if not os.path.exists(bashrc_path):
        with open(bashrc_path, 'w') as f:
            f.write("# .bashrc generated by Termux-Tools-Installer\n\n")
    
    # Add aliases to .bashrc if not already there
    with open(bashrc_path, 'r') as f:
        existing_content = f.read()
    
    with open(bashrc_path, 'a') as f:
        f.write("\n# Aliases added by Termux-Tools-Installer\n")
        for alias in aliases:
            if alias not in existing_content:
                f.write(f"{alias}\n")
                print(f"\033[1;32m[✓] Added alias: {alias}\033[0m")
    
    print(f"\033[1;32m[✓] Aliases configured in {bashrc_path}\033[0m")
    print(f"\033[1;33m[!] Run 'source ~/.bashrc' to apply changes to current session\033[0m")

def setup_termux_appearance():
    """Setup Termux appearance and configuration."""
    print_category("Setting up Termux Appearance")
    
    # Create termux properties directory if it doesn't exist
    termux_dir = os.path.expanduser("~/.termux")
    if not os.path.exists(termux_dir):
        os.makedirs(termux_dir)
    
    # Create termux.properties file with better settings
    with open(os.path.join(termux_dir, "termux.properties"), "w") as f:
        f.write("""# Termux properties file
# Generated by Termux-Tools-Installer

# Extra keyboard keys
extra-keys = [[ESC,TAB,CTRL,ALT,{key: '-', popup: '|'},DOWN,UP]]

# Bell character behavior
bell-character=vibrate

# Terminal cursor blink rate (off if 0)
terminal-cursor-blink-rate=600

# Use ctrl space key
use-black-ui=true
""")
    
    # Create colors.properties file with a cool color scheme
    with open(os.path.join(termux_dir, "colors.properties"), "w") as f:
        f.write("""# Termux color scheme
# Generated by Termux-Tools-Installer

# Hacker theme
background=#000000
foreground=#00FF00
cursor=#00FF00

color0=#000000
color1=#FF0000
color2=#00FF00
color3=#FFFF00
color4=#0000FF
color5=#FF00FF
color6=#00FFFF
color7=#FFFFFF
color8=#555555
color9=#FF5555
color10=#55FF55
color11=#FFFF55
color12=#5555FF
color13=#FF55FF
color14=#55FFFF
color15=#FFFFFF
""")
    
    print(f"\033[1;32m[✓] Termux appearance configured\033[0m")
    print(f"\033[1;33m[!] Restart Termux session to apply appearance changes\033[0m")

def download_wordlists():
    """Download common wordlists for security testing."""
    print_category("Downloading Wordlists")
    
    wordlists_dir = os.path.expanduser("~/wordlists")
    if not os.path.exists(wordlists_dir):
        os.makedirs(wordlists_dir)
    
    wordlists = [
        {
            "name": "rockyou.txt",
            "url": "https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt",
            "description": "Common password list"
        },
        {
            "name": "directory-list-2.3-medium.txt",
            "url": "https://raw.githubusercontent.com/daviddias/node-dirbuster/master/lists/directory-list-2.3-medium.txt",
            "description": "Directory brute forcing list"
        },
        {
            "name": "common.txt",
            "url": "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/Web-Content/common.txt",
            "description": "Common web files and directories"
        },
        {
            "name": "subdomains-top1million-5000.txt",
            "url": "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/DNS/subdomains-top1million-5000.txt",
            "description": "Common subdomains for DNS enumeration"
        }
    ]
    
    for wordlist in wordlists:
        output_path = os.path.join(wordlists_dir, wordlist["name"])
        run_command(f"wget -O {output_path} {wordlist['url']}", f"Downloading {wordlist['name']} ({wordlist['description']})")

def create_startup_script():
    """Create a custom startup script for Termux."""
    print_category("Creating Startup Script")
    
    motd_path = os.path.expanduser("~/.motd")
    with open(motd_path, "w") as f:
        f.write("""\033[1;36m
  ______                               
 /_  __/___  _________ ___  __  ___  __
  / / / __ \\/ ___/ __ `__ \\/ / / / |/_/
 / / / /_/ / /  / / / / / / /_/ />  <  
/_/  \\____/_/  /_/ /_/ /_/\\__,_/_/|_|  
                                        
    Advanced Tools by R4mii
\033[0m

Welcome to Termux! Type \033[1;32mhelp\033[0m for a list of commands.
Type \033[1;32mtools\033[0m to navigate to your tools directory.
Type \033[1;32mprojects\033[0m to navigate to your projects directory.

\033[1;33mHappy Hacking!\033[0m
""")
    
    # Add sourcing of motd to .bashrc
    bashrc_path = os.path.expanduser("~/.bashrc")
    with open(bashrc_path, "a") as f:
        f.write("\n# Display custom MOTD\n")
        f.write("if [ -f ~/.motd ]; then\n")
        f.write("    cat ~/.motd\n")
        f.write("fi\n")
    
    print(f"\033[1;32m[✓] Custom startup script created\033[0m")
    print(f"\033[1;33m[!] The custom welcome message will appear on next Termux startup\033[0m")

def main():
    """Main function to run the script."""
    # Check if running in Termux
    if not check_termux():
        print("\033[1;31m[!] This script is designed to run in Termux environment only!\033[0m")
        print("\033[1;31m[!] If you are running in Termux and seeing this error, please report it.\033[0m")
        sys.exit(1)
    
    # Print welcome banner
    print_banner()
    
    print("\033[1;33m[!] This script will install a comprehensive suite of tools in Termux.\033[0m")
    print("\033[1;33m[!] It includes security tools, programming languages, and utilities.\033[0m")
    print("\033[1;33m[!] Installation may take a significant amount of time and bandwidth.\033[0m")
    print("\033[1;33m[!] Some tools might not be available in all repositories.\033[0m")
    
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
    
    # Create necessary directories
    setup_directories()
    
    # Update system repositories and packages
    update_system()
    
    # Install packages in order of dependency
    install_base_packages()
    install_programming_languages()
    install_utility_tools()
    install_network_tools()
    install_security_tools()
    install_python_packages()
    install_dev_tools()
    
    # Additional setups
    setup_aliases()
    setup_termux_appearance()
    download_wordlists()
    create_startup_script()
    
    # Final update to ensure everything is in place
    update_system()
    
    # Print success message
    print_success_banner()
    print("\n\033[1;32m[✓] Installation completed!\033[0m")
    print("\033[1;33m[!] Some packages might not have been installed if they're not available in your repositories.\033[0m")
    print("\033[1;33m[!] Check the output above for any errors.\033[0m")
    print("\n\033[1;36m[*] To apply all changes, please restart Termux or run:\033[0m")
    print("\033[1;37m    source ~/.bashrc\033[0m")
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
