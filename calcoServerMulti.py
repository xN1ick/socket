import socket
import json
from threading import Thread

SERVER_ADDRESS='127.0.0.1'
SERVER_PORT=22225

def ricevi_comandi(sock_service, addr_client):
    print("avviato")
    while True:
            data=sock_service.recv(1024)
            if not data:
                break
            data=data.decode()
            data=json.loads(data)#Il metodo loads() può essere utilizzato per analizzare una stringa JSON valida e convertirla in un dizionario Python
            primoNum=data['primoNumero']
            operazione=data['operazione']
            secondoNum=data['secondoNumero']
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

def ricevi_connessioni(sock_listen):
    while True:
        sock_service, addr_client=sock_listen.accept()
        print("\nConnessione ricevuta da "+str(addr_client))
        print("\nCreo un thread per servire le richieste ")
        try:
            Thread(target=ricevi_comandi, args=(sock_service, addr_client)).start()
        except:
            print("il thread non si avvia ")
            sock_listen.close()

def avvia_server(indirizzo, porta):
    sock_listen=socket.socket()
    sock_listen.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock_listen.bind((SERVER_ADDRESS, SERVER_PORT))
    sock_listen.listen(5)
    print("Server in ascolto su %s." % str((SERVER_ADDRESS, SERVER_PORT)))
    ricevi_connessioni(sock_listen)

if __name__=='__main__':
    avvia_server(SERVER_ADDRESS, SERVER_PORT)
