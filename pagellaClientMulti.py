#nome del file : pagellaClientMulti.py
import socket
import sys
import random
import os
import time
import threading
import multiprocessing
import json
import pprint

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22225
NUM_WORKERS=4

#Versione 1 
def genera_richieste1(num,address,port):
    start_time_thread= time.time()
    try:
        s=socket.socket()
        s.connect((address,port))
        print(f"\n{threading.current_thread().name} {num+1}) Connessione al server: {address}:{port}")
    except:
        print(f"{threading.current_thread().name} Qualcosa è andato storto, sto uscendo... \n")
        sys.exit()

    #1. Generazione casuale:
    #   di uno studente (valori ammessi: 5 cognomi a caso tra cui il tuo cognome)
     
    studenti=random.randint(0,4) #genero numeri che equivalgono al simbolo dell'studenti

    
    if studenti==0:
        studente="D'alba"
    elif studenti==1:
        studente="Falcone"
    elif studenti==2:
        studente="Ghidoli"
    elif studenti==3: 
        studente="Rincon"
    else: 
        studente="Rescaldina"

       # print(voto, secondoNumero, studenti)  print di prova
    
    #   di una materia (valori ammessi: Matematica, Italiano, inglese, Storia e Geografia)
    materie=random.randint(0,4) #genero numeri che equivalgono al simbolo dell'studenti

    
    if materie==0:
        materia="Matematica"
    elif materie==1:
        materia="Italiano"
    elif materie==2:
        materia="inglese"
    elif materie==3: 
        materia="Storia"
    else: 
        materia="Geografia"
    #   di un voto (valori ammessi 1 ..10)
    voto=random.randint(1,10)
    #   delle assenze (valori ammessi 1..5) 
    assenze=random.randint(1,5)
    #2. comporre il messaggio, inviarlo come json
    messaggio={'Studente':studente,
    'Materia':materia,
    'Voto':voto,
    'Assenze':assenze}
    print(messaggio)
    print (f"Dati inviati dal server {messaggio}")
    messaggio=json.dumps(messaggio)#Trasformiamo l'oggetto in una stringa
    s.sendall(messaggio.encode("UTF-8"))
    data=s.recv(1024)
    data=data.decode()
    data=json.loads(data)
    print(f"Dati ricevuti dal server {data}")
    

    #   esempio: {'studente': 'Studente4', 'materia': 'Italiano', 'voto': 2, 'assenze': 3}
    #3. ricevere il risultato come json: {'studente':'Studente4','materia':'italiano','valutazione':'Gravemente insufficiente'}

    if not data:
        print(f"{threading.current_thread().name}: Server non risponde. Exit")#output che ci dice che il server non risponde
    else:
        #4 stampare la valutazione ricevuta esempio: La valutazione di Studente4 in italiano è Gravemente insufficiente
         print(f"{threading.current_thread().name}: Risultato: {data.decode()}") # trasforma il vettore di byte in stringa
        
    s.close()
    end_time_thread=time.time()#La funzione time() restituisce il numero di secondi trascorsi
    print(f"{threading.current_thread().name} tempo di esecuzione time=", end_time_thread-start_time_thread)

#Versione 2 
def genera_richieste2(num,address,port):
    try:
        s=socket.socket()
        s.connect((address,port))
        print(f"\n{threading.current_thread().name} {num+1}) Connessione al server: {address}:{port}")
    except:
        print(f"{threading.current_thread().name} Qualcosa è andato storto, sto uscendo... \n")
        sys.exit()
  #   1. Generazione casuale di uno studente(valori ammessi: 5 cognomi a caso scelti da una lista)
  #   Per ognuna delle materie ammesse: Matematica, Italiano, inglese, Storia e Geografia)
  #   generazione di un voto (valori ammessi 1 ..10)
  #   e delle assenze (valori ammessi 1..5) 
  #   esempio: pagella={"Cognome1":[("Matematica",8,1), ("Italiano",6,1), ("Inglese",9.5,3), ("Storia",8,2), ("Geografia",8,1)]}
    #genero numeri che equivalgono al simbolo dell'studenti

        
        if studenti==0:
            studente="D'alba"
        elif studenti==1:
            studente="Falcone"
        elif studenti==2:
            studente="Ghidoli"
        elif studenti==3: 
            studente="Rincon"
        else: 
            studente="Rescaldina"
    

    
    if materie==0:
        materia="Matematica"
    elif materie==1:
        materia="Italiano"
    elif materie==2:
        materia="inglese"
    elif materie==3: 
        materia="Storia"
    else: 
        materia="Geografia"

    studenti=random.randint(0,4)
    pagella=[]
    for m in materie: 
        voto=random.randint(1,10) 
        assenze=random.randint(1,5)
        materie=random.randint(0,4) #genero numeri che equivalgono al simbolo dell'studenti
  #2. comporre il messaggio, inviarlo come json
    messaggio={'Studente':studente,
    'Materia':materia,
    'Voto':voto,
    'Assenze':assenze}
    print(messaggio)
    messaggio=json.dumps(messaggio)#Trasformiamo l'oggetto in una stringa
    s.sendall(messaggio.encode("UTF-8"))
    data=s.recv(1024)
    data=data.decode()
    data=json.loads(data)
    print(f"Dati ricevuti dal server {data}")

#Versione 3
def genera_richieste3(num,address,port):
    try:
        s=socket.socket()
        s.connect((address,port))
        print(f"\n{threading.current_thread().name} {num+1}) Connessione al server: {address}:{port}")
    except:
        print(f"{threading.current_thread().name} Qualcosa è andato storto, sto uscendo... \n")
        sys.exit()
  #   1. Generazione casuale di uno studente(valori ammessi: 5 cognomi a caso scelti da una lista)
  #   Per ognuna delle materie ammesse: Matematica, Italiano, inglese, Storia e Geografia)
  #   generazione di un voto (valori ammessi 1 ..10)
  #   e delle assenze (valori ammessi 1..5) 
  #   esempio: pagella={"Cognome1":[("Matematica",8,1), ("Italiano",6,1), ("Inglese",9.5,3), ("Storia",8,2), ("Geografia",8,1)]}
    #genero numeri che equivalgono al simbolo dell'studenti

        
        if studenti==0:
            studente="D'alba"
        elif studenti==1:
            studente="Falcone"
        elif studenti==2:
            studente="Ghidoli"
        elif studenti==3: 
            studente="Rincon"
        else: 
            studente="Rescaldina"
    

    
    if materie==0:
        materia="Matematica"
    elif materie==1:
        materia="Italiano"
    elif materie==2:
        materia="inglese"
    elif materie==3: 
        materia="Storia"
    else: 
        materia="Geografia"

    studenti=random.randint(0,4)
    for stud in studenti:
        pagella=[]
        for m in materie: 
            voto=random.randint(1,10) 
            assenze=random.randint(1,5)
            materie=random.randint(0,4) #genero numeri che equivalgono al simbolo dell'studenti
            pagella.append((m,voto,assenze))
        tabellone[stud]=pagella
  #2. comporre il messaggio, inviarlo come json
    messaggio={'Studente':studente,
    'Materia':materia,
    'Voto':voto,
    'Assenze':assenze}
    print(messaggio)
    pp=pprint.PrettyPrinter(indent=4)
    pp.pprint(tabellone)
    tabellone=json.dumps(tabellone)#Trasformiamo l'oggetto in una stringa
    s.sendall(messaggio.encode("UTF-8"))
    data=s.recv(1024)
    data=data.decode()
    data=json.loads(data)
    print(f"Dati ricevuti dal server {data}")

if __name__ == '__main__':
    start_time=time.time()
    # PUNTO A) ciclo per chiamare NUM_WORKERS volte la funzione genera richieste (1,2,3)
    # alla quale passo i parametri (num,SERVER_ADDRESS, SERVER_PORT)
    for num in range(NUM_WORKERS):
        genera_richieste1(num, SERVER_ADDRESS, SERVER_PORT)
    end_time=time.time()
    print("Total SERIAL time=", end_time - start_time)
     
    start_time=time.time()
    threads=[]
    # PUNTO B) ciclo per chiamare NUM_WORKERS volte la funzione genera richieste (1,2,3)  
    # tramite l'avvio di un thread al quale passo i parametri args=(num,SERVER_ADDRESS, SERVER_PORT,)
    # avviare tutti i thread e attenderne la fine
    #ciclo per chiamare NUM_WORKERS volte la funzione genera richieste tramite l'avvio di un thread al quale passo i parametri args=(num,SERVER_ADDRESS, SERVER_PORT,)
    for num in range (NUM_WORKERS):
    # ad ogni iterazione appendo il thread creato alla lista threads
        threads.append(threading.Thread(target=genera_richieste1, args=(num, SERVER_ADDRESS, SERVER_PORT,)))
        
    #avvio tutti i thread
    for thread in threads:
        thread.start()#start() è un metodo integrato della classe Thread del modulo di threading
    #aspetto la fine di tutti i thread 
    for thread in threads:
        thread.join()
    end_time=time.time()
    print("Total THREADS time= ", end_time - start_time)

    start_time=time.time()
    process=[]
    # PUNTO C) ciclo per chiamare NUM_WORKERS volte la funzione genera richieste (1,2,3) 
    # tramite l'avvio di un processo al quale passo i parametri args=(num,SERVER_ADDRESS, SERVER_PORT,)
    # avviare tutti i processi e attenderne la fine
    #  ciclo per chiamare NUM_WORKERS volte la funzione genera richieste tramite l'avvio di un processo al quale passo i parametri args=(num,SERVER_ADDRESS, SERVER_PORT,)
    for num in range(NUM_WORKERS): 
        process.append(multiprocessing.Process(target=genera_richieste1, args=(num, SERVER_ADDRESS, SERVER_PORT)))
    #  avvio tutti i processi
    for num in range(NUM_WORKERS):
        process[num].start()#avvio
    # aspetto la fine di tutti i processi 
    for num in range(NUM_WORKERS):
        process[num].join()
    end_time=time.time()
    print("Total PROCESS time= ", end_time - start_time)