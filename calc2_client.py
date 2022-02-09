import json
import socket

SERVER_ADDRESS='127.0.0.1'
SERVER_PORT=22224

def invia_comandi(sock_service):
    while True:
        primoNum=input("Digita numero, se invece vuoi uscire digita exit() ")
        if primoNum=="exit()":
            break
        primoNum=float(primoNum)
        operazione=input("Inserisci l'operazione desiderata (+,-,*,/,%)")
        secondoNum=float(input("Digita il secondo numero "))
        messaggio={'primoNum':primoNum, 'operazione':operazione, 'secondoNum':secondoNum}
        messaggio=json.dumps(messaggio)# La funzione dumps() converte un oggetto Python in una stringa 
        sock_service.sendall(messaggio.encode("UTF-8"))#specifica che ogni carattere è rappresentato da una sequenza specifica di uno o più byte.
        data=sock_service.recv(1024)#la funzione recv() del modulo socket di Python può essere utilizzata per ricevere dati da entrambi i socket TCP e UDP.
        print("Risultato: ",data.decode())#Questo metodo viene utilizzato per convertire da uno schema di codifica, in cui la stringa dell'argomento è codificata nello schema di codifica desiderato

def  connessione_server(address, port):
    sock_service=socket.socket()
    sock_service.connect((SERVER_ADDRESS, SERVER_PORT))
    print("Connesso a " + str((SERVER_ADDRESS, SERVER_PORT)))
    invia_comandi(sock_service)

if __name__=='__main__':
    connessione_server(SERVER_ADDRESS, SERVER_PORT)