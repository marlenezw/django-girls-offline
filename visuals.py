#!/usr/bin/env python3
import sys
import os

# ANSI color codes - Django Girls orange
ORANGE = '\033[38;5;214m'  # Django Girls orange color
ORANGE_BG = '\033[48;5;214m'
BOLD = '\033[1m'
RESET = '\033[0m'
WHITE = '\033[97m'
BLACK = '\033[30m'

def print_welcome_message():
    """Print an orange block-style welcome message for Django Girls"""
    
    # Block-style banner using Unicode block characters
    banner = f"""{ORANGE}
██████╗      ██╗ █████╗ ███╗   ██╗ ██████╗  ██████╗      ██████╗ ██╗██████╗ ██╗     ███████╗
██╔══██╗     ██║██╔══██╗████╗  ██║██╔════╝ ██╔═══██╗    ██╔════╝ ██║██╔══██╗██║     ██╔════╝
██║  ██║     ██║███████║██╔██╗ ██║██║  ███╗██║   ██║    ██║  ███╗██║██████╔╝██║     ███████╗
██║  ██║██   ██║██╔══██║██║╚██╗██║██║   ██║██║   ██║    ██║   ██║██║██╔══██╗██║     ╚════██║
██████╔╝╚█████╔╝██║  ██║██║ ╚████║╚██████╔╝╚██████╔╝    ╚██████╔╝██║██║  ██║███████╗███████║
╚═════╝  ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝      ╚═════╝ ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝
{RESET}"""
    
    # Box drawing for frame
    frame_top = f"{ORANGE}┌{'─' * 65}┐{RESET}"
    frame_bottom = f"{ORANGE}└{'─' * 65}┘{RESET}"
    
    # Welcome text with box
    print()
    print(banner)
    print()
    print(frame_top)
    print(f"{ORANGE}│{RESET} {BOLD}Welcome to Django Girls Offline!{RESET}                                        {ORANGE}│{RESET}")
    print(f"{ORANGE}│{RESET}                                                                 {ORANGE}│{RESET}")
    print(f"{ORANGE}│{RESET} Start your web development journey with Django!                 {ORANGE}│{RESET}")
    print(f"{ORANGE}│{RESET} Type 'hello' to get started with your Django Girls Assistant.   {ORANGE}│{RESET}")
    print(frame_bottom)
    
    # System info bar
    # sys_info = f"Python {sys.version.split()[0]} | Django Ready | {os.name.upper()} System"
    # print(f"\n{ORANGE}{'═' * 65}{RESET}")
    # print(f"{ORANGE}  {sys_info}{RESET}")
    # print(f"{ORANGE}{'═' * 65}{RESET}\n")

def print_compact_version():
    """Print a more compact block version"""
    print(f"""
{ORANGE_BG}{BLACK} DJANGO GIRLS {RESET}
    
{ORANGE}████████████████████████████████████████████████████████████████
██╔══██╗     ██╗ █████╗ ███╗   ██╗ ██████╗  ██████╗ 
██║  ██║     ██║██╔══██╗████╗  ██║██╔════╝ ██╔═══██╗
██║  ██║     ██║███████║██╔██╗ ██║██║  ███╗██║   ██║
██║  ██║██   ██║██╔══██║██║╚██╗██║██║   ██║██║   ██║
██████╔╝╚█████╔╝██║  ██║██║ ╚████║╚██████╔╝╚██████╔╝
╚═════╝  ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ 

 ██████╗ ██╗██████╗ ██╗     ███████╗
██╔════╝ ██║██╔══██╗██║     ██╔════╝
██║  ███╗██║██████╔╝██║     ███████╗
██║   ██║██║██╔══██╗██║     ╚════██║
╚██████╔╝██║██║  ██║███████╗███████║
 ╚═════╝ ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝
████████████████████████████████████████████████████████████████{RESET}

{ORANGE}Welcome to Django Girls Tutorial{RESET}
Build amazing things with Django!

{ORANGE}♥{RESET} Start with {ORANGE}python manage.py runserver{RESET}
{ORANGE}♥{RESET} Visit {ORANGE}http://127.0.0.1:8000/{RESET}
""")

if __name__ == "__main__":
    print_welcome_message()  # Detailed version
    # print_compact_version()  # Compact version