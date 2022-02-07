import socket
import json

HOST="127.0.0.1"
PORT=65432
students = {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7.5,4),("Storia",7.5,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9.5,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7.5,2),("Italiano",6,2),("Inglese",4,3),("Storia",8.5,2),("Geografia",8,2)]}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    i=1 #contatore
    s.bind((HOST,PORT))
    s.listen()
    print("[*] In ascolto su %s:%d"%(HOST,PORT))
    clientsocket, address = s.accept()
    with clientsocket as c:
        print("Connessione da ", address)
        while True:
            request=c.recv(1024)
            if not request:
                break
            request=request.decode()
            request=json.loads(request)
            stringa=request['stringa']

            if (stringa.find('#list') != -1):
                serialized_dict = json.dumps(students)#codifica prima di inviare
                c.sendall(serialized_dict.encode())

            elif (stringa.find('#set') != -1):#Il comando set deve verificare che lo studente non esista già
                serieStr=stringa.split('/')
                nomStud = serieStr[1]
                if(nomStud in students):
                    c.sendall("Studente già presente".encode())
                else:
                    students[nomStud] = []
                    c.sendall("Studente inserito correttamente".encode())
            
            elif (stringa.find('#put') != -1): # Il comando put deve verificare che lo studente esista e che la materia non esista
                presente = False
                serieStr=stringa.split('/')
                nomStud = serieStr[1]
                materia = serieStr[2]
                if(nomStud in students):
                    for studente, materPag in students.items():
                        if(studente == nomStud):
                            for i in materPag:
                                print(materPag)
                                if(materia == i[0]):
                                    print(i[0])
                                    presente=True
                    if(presente == False):
                        voto = int(serieStr[3])
                        ore = int(serieStr[4])
                        newMater = [materia, voto, ore]
                        students[nomStud].append(newMater)
                        c.sendall("Voto inserito correttamente".encode())
                    else:
                        c.sendall("Materia già presente".encode())
                else:
                    c.sendall("Lo studente non è presente".encode())


            elif (stringa.find('#get') != -1):#l comando get deve verificare che lo studente esista
                strVot = ""
                serieStr=stringa.split('/')
                nomStud = serieStr[1]
                if(nomStud in students):
                    serialized_dict = json.dumps(students[nomStud])
                    c.sendall(serialized_dict.encode())
                else:
                    listString = ["Lo studente non è presente"]
                    serialized_dict = json.dumps(listString)
                    c.sendall(serialized_dict.encode())
            else:
                c.sendall("Comando errato".encode())