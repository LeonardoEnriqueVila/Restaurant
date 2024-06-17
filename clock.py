import time
import threading
import clientGeneration
import table

class Clock: # clase que gestiona el paso del tiempo y actualiza el reloj
    def __init__(self):
        self.stopTime = threading.Event()
        self.hours = 8 # settea de forma inicial las 8AM que es el horario de apertura
        # mediante el valor de horas manejo las frecuencias
        self.minutes = 0
        self.seconds = 0
        self.days = 1 # indica el primer día como "dia 1" por una cuestion visual
        print(f"Day {self.days} - {self.hours}:{self.minutes}:{self.seconds}")
        clientGeneration.clientGenerator.matchHour(self.hours) # hace la primer llamada al generador de clientes, al inicializar

    def time(self): # gestiona bucle de tiempo y contador de segundos. Llama al reloj para modificar valores
        while not self.stopTime.is_set():
            time.sleep(0.0005)
            self.seconds += 1
            self.clock()
    
    def clock(self): # gestiona el reloj
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
            if self.hours == 24 or self.hours == 0:
                close = table.tableManager.checkEmpty()
                if close:
                    self.printDayStats()
                    self.stopTime.set()
            table.tableManager.checkTableTimers() # checkea timers y sienta a clientes de la lista de espera en caso de haberlos
            clientGeneration.clientGenerator.matchHour(self.hours)
        if self.minutes == 60:
            self.minutes = 0
            self.hours += 1
            print(f"Day {self.days} - {self.hours}:{self.minutes}:{self.seconds}")
            if self.hours == 23:
                table.tableManager.late = True # asegura que los clientes que llegan a partir de las 23 se queden menos tiempo
        if self.hours == 24:
            self.hours = 0
            self.days += 1

    def printDayStats(self):
        print(f"Restaurant just closed at {self.hours}:{self.minutes}:{self.seconds}")
        print(f"A total of {clientGeneration.clientGenerator.groupCounter} groups of clients ate in the restaurant") 
        print(f"A total of {clientGeneration.clientGenerator.clientCounter} individuals ate in the restaurant") 
        print(f"A total of {clientGeneration.clientGenerator.leaverGroupCounter} groups of clients leave and didnt eat in the restaurant")
        print(f"A total of {clientGeneration.clientGenerator.leaverClientCounter} individuals leave and didnt eat in the restaurant")
        print(f"Average time spent in tables: {table.tableManager.totalTimeInTable / clientGeneration.clientGenerator.groupCounter}")
        
clock = Clock()
clock.time() # inicia el bucle de tiempo


