#D'alba
#calcolatrice client per calcoServer.py versione multithread
import socket
import sys
import random
import os
import time
import threading
import multiprocessing
import json

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22225
NUM_WORKERS=2

def genera_richieste(num,address,port):
    start_time_thread= time.time()
    try:
        s=socket.socket()
        s.connect((address,port))
        print(f"\n{threading.current_thread().name} {num+1}) Connessione al server: {address}:{port}")
    except:
        print(f"{threading.current_thread().name} Qualcosa è andato storto, sto uscendo... \n")
        sys.exit()
    #1. rimpiazzare questa parte con la generazione di operazioni e numeri random, non vogliamo inviare sempre 3+5 
    #primoNumero=3
    #operazione="+"
    #secondoNumero=5
    primoNumero=random.randint(1,100) #genero numeri
    secondoNumero=random.randint(1,100)
    operazione=random.randint(0,4) #genero numeri che equivalgono al simbolo dell'operazione

    operatore=""
    if operazione==0:
        operatore="+"#somma
    elif operatore==1:
        operatore="-"#sottrazione
    elif operazione==2:
        operatore="*"#moltiplicazione
    elif operazione==3: 
        operatore="/"#divisione
    else: 
        operatore="%"#perc

       # print(primoNumero, secondoNumero, operazione)  print di prova
    operazione=operatore
    #2. comporre il messaggio, inviarlo come json e ricevere il risultato
    messaggio={'primoNumero':primoNumero,
    'operazione':operazione,
    'secondoNumero':secondoNumero}
    print(messaggio)
    messaggio=json.dumps(messaggio)#Trasformiamo l'oggetto in una stringa
    s.sendall(messaggio.encode("UTF-8"))
    data=s.recv(1024)
    if not data:
        print(f"{threading.current_thread().name}: Server non risponde. Exit") #output che ci dice che il server non risponde
    else:
        print(f"{threading.current_thread().name}: Risultato: {data.decode()}") # trasforma il vettore di byte in stringa
    s.close()#il metodo close() chiude un file aperto.
    end_time_thread=time.time()#La funzione time() restituisce il numero di secondi trascorsi
    print(f"{threading.current_thread().name} tempo di esecuzione time=", end_time_thread-start_time_thread)

if __name__ == '__main__':
    start_time=time.time()
    # 3 ciclo per chiamare NUM_WORKERS volte la funzione genera richieste alla quale passo i parametri (num,SERVER_ADDRESS, SERVER_PORT)
    for num in range(NUM_WORKERS):
        genera_richieste(num, SERVER_ADDRESS, SERVER_PORT)
    end_time=time.time()
    print("Total SERIAL time=", end_time - start_time)
     
    start_time=time.time()
    threads=[]
    # 4 ciclo per chiamare NUM_WORKERS volte la funzione genera richieste tramite l'avvio di un thread al quale passo i parametri args=(num,SERVER_ADDRESS, SERVER_PORT,)
    for num in range (0, NUM_WORKERS):
    # ad ogni iterazione appendo il thread creato alla lista threads
        threads.append(threading.Thread(target=genera_richieste, args=(num, SERVER_ADDRESS, SERVER_PORT,)))
    # 5 avvio tutti i thread
    for thread in threads:
        thread.start()#start() è un metodo integrato della classe Thread del modulo di threading
    # 6 aspetto la fine di tutti i thread 
    for thread in threads:
        thread.join()#Il join in Python prende tutti gli elementi di un iterabile e li unisce in un'unica stringa.
    end_time=time.time()#fine
    print("Total THREADS time= ", end_time - start_time)

    start_time=time.time()
    process=[]
    # 7 ciclo per chiamare NUM_WORKERS volte la funzione genera richieste tramite l'avvio di un processo al quale passo i parametri args=(num,SERVER_ADDRESS, SERVER_PORT,)
    for num in range(NUM_WORKERS): 
        process.append(multiprocessing.Process(target=genera_richieste, args=(num, SERVER_ADDRESS, SERVER_PORT)))
    # 8 avvio tutti i processi
    for num in range(NUM_WORKERS):
        process[num].start()#avvio
    # 9 aspetto la fine di tutti i processi 
    for num in range(NUM_WORKERS):
        process[num].join()
    end_time=time.time()
    print("Total PROCESS time= ", end_time - start_time)