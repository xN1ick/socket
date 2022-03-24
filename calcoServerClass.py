import socket
import json
from threading import Thread

SERVER_ADDRESS='127.0.0.1'
SERVER_PORT=22224

class Server():

    def __init__(self, address, port):
        self.address=address
        self.port=port

    def ricevi_comandi(self, sock_service, addr_client):
        print("avviato")
        while True:
                data=sock_service.recv(1024)
                if not data:
                    break
                data=data.decode()
                print(data)
                data=json.loads(data)#Il metodo loads() può essere utilizzato per analizzare una stringa JSON valida e convertirla in un dizionario Python
                primoNum=data['primoNum']
                operazione=data['operazione']
                secondoNum=data['secondoNum']
                ris=""
                if operazione=="+":
                    ris=primoNum+secondoNum
                elif operazione=="-":
                    ris=primoNum-secondoNum
                elif operazione=="*":
                    ris=primoNum*secondoNum
                elif operazione=="/":
                    if secondoNum==0:
                        ris="Impossibile dividere per 0"
                    else:
                        ris=primoNum/secondoNum
                elif operazione=="%":
                    ris=primoNum%secondoNum
                else:
                    ris="Operazione non andata a buon fine"
                ris=str(ris)
                sock_service.sendall(ris.encode("UTF-8"))

        sock_service.close()

    def ricevi_connessioni(self, sock_listen):
        while True:
            sock_service, addr_client=sock_listen.accept()
            print("\nConnessione ricevuta da "+str(addr_client))
            print("\nCreo un thread per servire le richieste ")
            try:
                Thread(target=self.ricevi_comandi, args=(sock_service, addr_client)).start()
            except Exception as e:
                print(e)
                print("il thread non si avvia ")
                sock_listen.close()

    def avvia_server(self):
        sock_listen=socket.socket()
        sock_listen.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock_listen.bind((SERVER_ADDRESS, SERVER_PORT))
        sock_listen.listen(5)
        print("Server in ascolto su %s." % str((SERVER_ADDRESS, SERVER_PORT)))
        self.ricevi_connessioni(sock_listen)

s1=Server(SERVER_ADDRESS, SERVER_PORT)
sock_listen=s1.avvia_server()
s1.ricevi_connessioni(sock_listen)