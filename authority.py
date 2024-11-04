#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import rich 
import pyfiglet
import ipaddress
import subprocess as sb
from rich.console import Console
from pyfiglet import Figlet

console = Console()

def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def banner(): 
    print(pyfiglet.figlet_format("Authority", font="slant"), end='') 
    print("="*47)
    console.print("[blue]A simple reverse shell payload generator and controller[/blue]")
    console.print("[blue]created by: [/blue][red]Jdigitalz[/red][blue] Version:[/blue][yellow] 1.0[/yellow]")
    console.print("[blue]Github: [/blue][green]https://github.com/Jdigitalz[/green]")
    print("="*47)

def main_menu(): 
    print("What mode would you like to use?")
    print("[1]Authority handler generator")
    print("[2]Payload generator")
    print("[99]Exit")
    while True: 
        try: 
            option = input(">>> ").strip().lower()
            if option == "99": 
                exit()
            elif option == "1": 
                auth_menu()
            elif option == "2": 
                pay_menu()
        except KeyboardInterrupt:  
            print("\nexiting...")
            exit()

def Mset_options(handler_name): 
    if not handler_name.endswith(".py"): 
        open(f"{handler_name}.py", "a").close()
        os.chdir("source")
        with open("source-master.py", "r") as handlerf: 
            handler = handlerf.read()
            os.chdir("..")
        with open(f"{handler_name}.py", "w") as _: 
            _.write(handler)
        print("What Ip do you want to host on?")
        while True: 
            setip = input(">>> ").strip()
            if not is_valid_ip(setip): 
                console.print(f"[red]'{setip}', not a valid ip address[/red]")
            else: 
                break
        print("what port do you want to host on?")
        while True: 
            setport = input(">>> ")
            edit_master(f"{handler_name}.py", f"host_ip='{setip.strip()}'", f"host_port={str(setport)}")
            print(f"Created handler file named {handler_name}.py on {setip}:{setport}")
            print(f"{os.getcwd()}/{handler_name}.py")
            break
    else:
        open(f"{handler_name}", "a").close()
        os.chdir("source")
        with open("source-master.py", "r") as handlerf: 
            handler = handlerf.read()
            os.chdir("..")
        with open(f"{handler_name}", "w") as _: 
            _.write(handler)
        print("What Ip do you want to host on?")
        while True: 
            setip = input(">>> ").strip()
            if not is_valid_ip(setip): 
                console.print(f"[red]'{setip}', not a valid ip address[/red]")
            else: 
                break
        print("what port do you want to host on?")
        while True: 
            setport = input(">>> ")
            edit_master(f"{handler_name}", f"host_ip='{setip.strip()}'", f"host_port={str(setport)}")
            print(f"Created handler file named {handler_name} on {setip}:{setport}")
            print(f"{os.getcwd()}/{handler_name}")
            break

def edit_master(file_path, line_15_content, line_16_content):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    lines[14] = line_15_content + '\n'
    lines[15] = line_16_content + '\n'

    with open(file_path, 'w') as file:
        file.writelines(lines)

def Pset_options(payload_name): 
    if not payload_name.endswith(".py"): 
        open(f"{payload_name}.py", "a").close()
        os.chdir("source")
        with open("source-payload.py", "r") as payloadf: 
            payload = payloadf.read()
            os.chdir("..")
        with open(f"{payload_name}.py", "w") as _: 
            _.write(payload)
        print("What Ip do you want to listen for?")
        while True: 
            setip = input(">>> ").strip()
            if not is_valid_ip(setip): 
                console.print(f"[red]'{setip}', not a valid ip address[/red]")
            else: 
                break
        print("what port do you want to listen for?")
        while True: 
            setport = input(">>> ")
            edit_payload(f"{payload_name}.py", f"target_ip='{setip.strip()}'", f"target_port={str(setport)}")
            print(f"Created payload file named {payload_name}.py on {setip}:{setport}")
            print(f"{os.getcwd()}/{payload_name}.py")
            break
    else:
        open(f"{payload_name}", "a").close()
        os.chdir("source")
        with open("source-payload.py", "r") as payloadf: 
            payload = payloadf.read()
            os.chdir("..")
        with open(f"{payload_name}", "w") as _: 
            _.write(payload)
        print("What Ip do you want to listen for?")
        while True: 
            setip = input(">>> ").strip()
            if not is_valid_ip(setip): 
                console.print(f"[red]'{setip}', not a valid ip address[/red]")
            else: 
                break
        print("What port do you want to listen for?")
        while True: 
            setport = input(">>> ")
            edit_payload(f"{payload_name}", f"target_ip='{setip.strip()}'", f"target_port={str(setport)}")
            print(f"Created payload file named {payload_name} on {setip}:{setport}")
            print(f"{os.getcwd()}/{payload_name}")
            break

def edit_payload(file_path, line9, line10):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    lines[8] = line9 + '\n'
    lines[9] = line10 + '\n'

    with open(file_path, 'w') as file:
        file.writelines(lines)

def auth_menu(): 
    sb.run("clear")
    banner()
    print("[1]Create reverse shell handler file")
    print("[2]Start a live reverse shell handler")
    print("[3]Create reverse remote viewer handler")
    print("[99]Main menu")
    console.print("[green]Hint: Ctrl + c lets you go back to the main menu[/green]")
    while True: 
        try: 
            option = input(">>> ")
            if option.strip().lower() == "99": 
                os.chdir(os.path.dirname(os.path.abspath(__file__)))
                sb.run("clear")
                main()
            elif option.strip().lower() == "1":
                sb.run("clear")
                os.chdir(os.path.dirname(os.path.abspath(__file__)))
                os.chdir("handlers")
                banner()
                print("What do want to name this file?")
                while True: 
                    ufile_name = input(">>> ").strip()
                    if not ufile_name.endswith(".py"): 
                        file_name = ufile_name + ".py"
                    else: 
                        file_name = ufile_name
                    if os.path.isfile(file_name):
                        console.print(f"[yellow]Warning: '{file_name}' already exists would you like to overwrite it[/yellow]")
                        console.print("[yellow]y/n[/yellow]") 
                        option = input(">>> ").strip().lower()
                        if option == "y":
                            if option.endswith(".py"): 
                                os.remove(file_name)
                                Mset_options(file_name)
                                exit()
                            else:
                                Mset_options(file_name)
                                exit()
                            pass
                        elif option == "n": 
                            sb.run("clear")
                            banner()
                            print("what do you want to name this file?")
                            continue
                    else:
                        Mset_options(file_name)
                        exit()
            elif option.strip().lower() == "2": 
                if os.path.basename(os.getcwd()) == "handlers":
                    sb.run("clear")
                    os.chdir(os.path.dirname(os.path.abspath(__file__)))
                    os.chdir("handlers")
                    Mset_options("LIVE_HANDLER_FILE.py")
                    try:
                        sb.run("clear")
                        sb.run("python LIVE_HANDLER_FILE.py", shell=True)
                        os.remove("LIVE_HANDLER_FILE.py")
                        exit()
                    except KeyboardInterrupt:
                        os.remove("LIVE_HANDLER_FILE.py")
                        exit()
                else: 
                    os.chdir(os.path.dirname(os.path.abspath(__file__)))
                    os.chdir("handlers")
                    Mset_options("LIVE_HANDLER_FILE.py")
                    try:
                        sb.run("clear")
                        sb.run("python LIVE_HANDLER_FILE.py", shell=True)
                        os.remove("LIVE_HANDLER_FILE.py")
                        exit()
                    except KeyboardInterrupt:
                        exit()
            elif option.strip().lower() == "3": 
                console.print("[yellow]Sorry this option is work in progress")
            else: 
                console.print(f"[red]Invalid option '{option}'[/red]")
        except KeyboardInterrupt:              
            if os.path.exists("LIVE_HANDLER_FILE.py"): 
                os.remove("LIVE_HANDLER_FILE.py")
            os.chdir(os.path.dirname(os.path.abspath(__file__)))
            sb.run("clear")
            banner()
            main_menu()

def pay_menu():
    sb.run("clear")
    banner()
    print("[1]Create reverse shell payload")
    print("[2]Create remote viewer payload")
    print("[99]Main menu")
    console.print("[green]Hint: Ctrl + c lets you go back to the main menu[/green]")
    while True: 
        try: 
            option = input(">>> ")
            if option.strip().lower() == "99": 
                sb.run("clear")
                os.chdir(os.path.dirname(os.path.abspath(__file__)))
                main()
            elif option.strip().lower() == "1":
                sb.run("clear")
                print(os.getcwd())
                os.chdir(os.path.dirname(os.path.abspath(__file__)))
                os.chdir("payloads")
                banner()
                print("What do want to name this file?")
                while True: 
                    ufile_name = input(">>> ").strip()
                    if not ufile_name.endswith(".py"): 
                        file_name = ufile_name + ".py"
                    else: 
                        file_name = ufile_name
                    if os.path.isfile(file_name): 
                        console.print(f"[yellow]Warning: '{file_name}' already exists would you like to overwrite it[/yellow]")
                        console.print("[yellow]y/n[/yellow]") 
                        option = input(">>> ").strip().lower()
                        if option == "y":
                            if option.endswith(".py"): 
                                os.remove(file_name)
                                Pset_options(file_name)
                                exit()
                            else:
                                Pset_options(file_name)
                                exit()
                            pass
                        elif option == "n": 
                            sb.run("clear")
                            banner()
                            print("what do you want to name this file?")
                            continue
                    else:
                        Pset_options(file_name)
                        exit()
            elif option.strip().lower() == "2": 
                console.print("[yellow]Sorry this option is work in progress[/yellow]")
            else: 
                console.print(f"[red]Invalid option '{option}'[/red]")
        except KeyboardInterrupt:              
            os.chdir(os.path.dirname(os.path.abspath(__file__)))
            sb.run("clear")
            banner()
            main_menu()

def main():
    sb.run("clear")
    banner()
    main_menu() 

if __name__ == "__main__": 
    main()
