import inputFunctions # archivo que solamente contiene funciones de input sin clase
import random

class TableManager:
    def __init__(self):
        self.tables = inputFunctions.getTables()
        self.timeRange = inputFunctions.getTimeRange()
        self.smallTable = 0
        self.mediumTable = 0
        self.bigTable = 0
        self.tableList = [] # lista de objetos Table
        self.clientWaitingList = []
        self.generateTableSizes() # genera diferentes tamaños de mesas y los objetos Table mediante generateTables()
        self.late = False
        self.totalTimeInTable = 0

    def generateTableSizes(self): # usa una varible temporal para calcular la cantidad de mesas de diferentes tamaños
        tables = self.tables
        self.smallTable = tables // 3
        self.generateTables(self.smallTable, "small") # le pasa cantidad de mesas del tipo y tipo de mesa
        tables -= self.smallTable
        self.bigTable = tables // 3
        self.generateTables(self.bigTable, "big")
        tables -= self.bigTable
        self.mediumTable = tables
        self.generateTables(self.mediumTable, "medium")
        print(f"Total: {self.tables}, Small: {self.smallTable}, Medium: {self.mediumTable}, Big: {self.bigTable}")

    def generateTables(self, totalTables, size): # genera objetos Table en la lista segun el tamaño que se le pasa
        # argumento size sirve tanto para asignar valor a la propiedad size como para el id, que se combina con el indice de mesa
        for i in range(0, totalTables):
            newTable = Table(size, size.capitalize() + " Table " + str(i + 1))
            self.tableList.append(newTable)

    def sitClient(self, clientGroupSize):
        if clientGroupSize in [1, 2]: # priorizar mesa pequeña
            table = self.getTable("small")
            if table == False: # si no obtiene pequeña busca mediana
                table = self.getTable("medium")
                if table == False: # si no obtiene mediana busca grande
                    table = self.getTable("big")
        elif clientGroupSize in [3, 4]:
            table = self.getTable("medium")
            if table == False: # si no obtiene mediana busca grande
                table = self.getTable("big")
        else: # grupo de 5 o 6
            table = self.getTable("big") # la unica opcion es una mesa grande
        if table:
            table.aviable = False
            if self.late == False:
                table.clientTime = random.randint(self.timeRange[0], self.timeRange[1])
            else:
                # asegura que los clientes que entran tarde no se queden tiempo excesivo
                table.clientTime = random.randint(self.timeRange[0], 45 if 45 <= self.timeRange[1] else 30)
            self.totalTimeInTable += table.clientTime  
            table.clientsInTable = clientGroupSize
            print(f"{table.clientsInTable} clients sit on {table.id} for {table.clientTime} minutes")
        else:
            # asegurarse de que la lista de espera sea igual o menor a la mitad del total de mesas
            if len(self.clientWaitingList) <= self.tables / 2: 
                self.clientWaitingList.append(clientGroupSize) # añade cliente a la lista de espera
                print(f"{clientGroupSize} clients go to the waiting line")
            else:
                print(f"{clientGroupSize} clients leave because waiting line is too long!")
                return False
        return True
            
                
    def getTable(self, size): 
        for i in range(0, self.tables):
            # busca mesa que coincida con tamaño buscado y esté disponible
            if self.tableList[i].size == size and self.tableList[i].aviable == True:
                return self.tableList[i]
        return False

    def checkTableTimers(self): # esta funcion se llama una vez por minuto
        # permite rastrear el uso de las mesas y liberarlas cuando su contador de minutos de ocupacion llega a 0
        for i in range(0, self.tables):
            self.tableList[i].clientTime -= 1
            if self.tableList[i].clientTime == 0:
                print(f"{self.tableList[i].clientsInTable} clients leave {self.tableList[i].id}")
                self.tableList[i].clientsInTable = 0
                self.tableList[i].aviable = True
                if len(self.clientWaitingList) > 0: # si hay clientes en fila
                    self.getClientFromLine(self.tableList[i].size)
            
    def getClientFromLine(self, TableSize):
        index = False
        if TableSize == "small":
            index = self.getValidIndexForPop([1, 2])
        elif TableSize == "medium":
            index = self.getValidIndexForPop([1, 2, 3, 4])
        else: # big
            index = self.getValidIndexForPop([1, 2, 3, 4, 5, 6])
        if index != False:
            clientGroupSize = self.clientWaitingList.pop(index)
            self.sitClient(clientGroupSize)

    def getValidIndexForPop(self, valid): # obtiene un indice valido para hacer el pop
        listSize = len(self.clientWaitingList)
        for i in range(0, listSize):
            if self.clientWaitingList[i] in valid:
                return i
        return False
            
    def checkEmpty(self): # verifica que el local esta vacio para poder cerrarlo
        for i in range(0, self.tables):
            if self.tableList[i].aviable == False: # si encuentra una mesa ocupada devuelve False
                return False
        return True # devuelve True si todas las mesas estan libres
         
class Table:
    def __init__(self, size, id):
        self.size = size
        self.aviable = True
        self.clientTime = 0 # al asignarse un cliente, se le asigna un valor en minutos que se resta en cada iteracion del reloj
        self.id = id
        self.clientsInTable = 0
        # logrando de esta forma, tener un registro del tiempo que pasa un cliente en la mesa

tableManager = TableManager()

    
    
    
