import json
import socket
from threading import Thread
SERVER_ADDRESS='127.0.0.1'
SERVER_PORT=22224
class Client():

    def invia_comandi(self, sock_service):
        while True:
            try:
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
                dati=f"{operazione}; {primoNum};{secondoNum}"
                print("Risultato: ",data.decode())#Questo metodo viene utilizzato per convertire da uno schema di codifica, in cui la stringa dell'argomento è codificata nello schema di codifica desiderato

            except EOFError:
                print("\nOkay. Exit")
                break

            if not dati:
                print("Non puoi inviare una stringa vuota!")
                continue
            if dati == '0':
                    print("Chiudo la connessione con il server!")
                    sock_service.close()
                    break
                
            # dati = dati.encode()
            # sock_service.sendall(dati)
            # dati = sock_service.recv(2048)
            # if not dati:
            #     print("Server non risponde. Exit")
            #     break
            # dati = dati.decode()
            # print("Ricevuto dal server:")
            # print(dati + '\n')

        
    def connessione_server(self, address, port):
        sock_service=socket.socket()
        sock_service.connect((SERVER_ADDRESS, SERVER_PORT))
        print("Connesso a " + str((SERVER_ADDRESS, SERVER_PORT)))
        self.invia_comandi(sock_service)


        

c1=Client()
sock_serv=c1.connessione_server(SERVER_ADDRESS, SERVER_PORT)
# c1.invia_comandi(sock_serv)