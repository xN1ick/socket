import socket 
import json


HOST="127.0.0.1"
PORT=65435

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    while True:
        print("inserire KO per uscire ")
        
        messaggio=input("Digita una frase ")
        if messaggio=="KO":
            break
        s.sendall(messaggio.encode("UTF-8"))
        data=s.recv(1024)
        print("Risultato: ",data.decode()) #traforma il vettore  in una stringa