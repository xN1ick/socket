import socket 
import json 

HOST="127.0.0.1"
PORT=65435

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    contatore=1
    s.bind((HOST,PORT))
    s.listen()
    print("[*] In ascolto su %s: %d "%(HOST,PORT)) 
    clientsocket, address=s.accept() #restituzione della variabile che gestisce il socket e l'address 
    with clientsocket as cs:
        print("Conessione da ",address)
        while True:
            data=cs.recv(1024)
            if not data:  
                print("break")
                break
            data=data.decode()
            stringa=data
            print("stringa ottenuta "+ stringa)
            if stringa!="KO":
                ris=stringa+" "+str(contatore)
                contatore+=1
            ris=str(ris)
            cs.sendall(ris.encode("UTF-8")) #manda il vettore in risposta al client