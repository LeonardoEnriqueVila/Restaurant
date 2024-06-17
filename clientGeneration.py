import random
import table

class ClientGenerator:
    def __init__(self):
        self.veryLowChance = [1]
        self.otherVeryLowChance = [2]
        self.lowChance = [2, 3]
        self.otherLowChance = [4, 5]
        self.mediumChance = [6, 7, 8, 9]
        self.highChance = [10, 11, 12, 13, 14]

        self.clientCounter = 0
        self.groupCounter = 0
        self.leaverGroupCounter = 0
        self.leaverClientCounter = 0

    def generateDayClient(self): # generación teorica de clientes durante el dia
        # esto determinaría el tamaño del grupo que entra
        randomNum = random.randint(1, 14)
        if randomNum in self.veryLowChance:
            print("6 clients enter")
            if table.tableManager.sitClient(6):
                self.clientCounter += 6
                self.groupCounter += 1
            else:
                self.leaverGroupCounter += 1
                self.leaverClientCounter += 6
        elif randomNum in self.otherVeryLowChance:
            print("5 clients enter")
            if table.tableManager.sitClient(5):
                self.clientCounter += 5
                self.groupCounter += 1
            else:
                self.leaverGroupCounter += 1
                self.leaverClientCounter += 5
        elif randomNum in self.lowChance:
            print("4 clients enter")
            if table.tableManager.sitClient(4):
                self.clientCounter += 4
                self.groupCounter += 1
            else:
                self.leaverGroupCounter += 1
                self.leaverClientCounter += 4
        elif randomNum in self.otherLowChance:
            print("3 clients enter")
            if table.tableManager.sitClient(3):
                self.clientCounter += 3
                self.groupCounter += 1
            else:
                self.leaverGroupCounter += 1
                self.leaverClientCounter += 3
        elif randomNum in self.highChance:
            print("2 clients enter")
            if table.tableManager.sitClient(2):
                self.clientCounter += 2
                self.groupCounter += 1
            else:
                self.leaverGroupCounter += 1
                self.leaverClientCounter += 2
        elif randomNum in self.mediumChance:
            print("1 client enters")
            if table.tableManager.sitClient(1):
                self.clientCounter += 1
                self.groupCounter += 1
            else:
                self.leaverGroupCounter += 1
                self.leaverClientCounter += 1

    def generateNightClient(self): # generación teorica de clientes durante la noche
        randomNum = random.randint(1, 14)
        if randomNum in self.lowChance:
            print("6 clients enter")
            if table.tableManager.sitClient(6):
                self.clientCounter += 6
                self.groupCounter += 1
            else:
                self.leaverGroupCounter += 1
                self.leaverClientCounter += 6
        elif randomNum in self.otherLowChance:
            print("5 clients enter")
            if table.tableManager.sitClient(5):
                self.clientCounter += 5
                self.groupCounter += 1
            else:
                self.leaverGroupCounter += 1
                self.leaverClientCounter += 5
        elif randomNum in self.highChance:
            print("4 clients enter")
            if table.tableManager.sitClient(4):
                self.clientCounter += 4
                self.groupCounter += 1
            else:
                self.leaverGroupCounter += 1
                self.leaverClientCounter += 4
        elif randomNum in self.veryLowChance:
            print("3 clients enter")
            if table.tableManager.sitClient(3):
                self.clientCounter += 3
                self.groupCounter += 1
            else:
                self.leaverGroupCounter += 1
                self.leaverClientCounter += 3
        elif randomNum in self.mediumChance:
            print("2 clients enter")
            if table.tableManager.sitClient(2):
                self.clientCounter += 2
                self.groupCounter += 1
            else:
                self.leaverGroupCounter += 1
                self.leaverClientCounter += 2
        elif randomNum in self.otherVeryLowChance:
            print("1 client enters")
            if table.tableManager.sitClient(1):
                self.clientCounter += 1
                self.groupCounter += 1
            else:
                self.leaverGroupCounter += 1
                self.leaverClientCounter += 1
    def matchHour(self, hour): # genera clientes segun horario con diferente frecuencia
        # esta funcion es llamada una vez por minuto, y segun el horario, habra diferente probabilidad de que se llame al cliente
        randomNum = random.randint(1, 14)
        if hour == 8: # 8 a 9
            if randomNum in self.veryLowChance:
                self.generateDayClient()
        elif hour in [9, 10]: # 9 a 11
            if randomNum in self.lowChance:
                self.generateDayClient()
        elif hour == 11: # 11 a 12
            if randomNum in self.veryLowChance:
                self.generateDayClient()
        elif hour in [12, 13]: # 12 a 14
            if randomNum in self.mediumChance:
                self.generateDayClient()
        elif hour in [14, 15]: # 14 a 16
            if randomNum in self.veryLowChance:
                self.generateDayClient()
        elif hour in [16, 17]: # 16 a 18
            if randomNum in self.mediumChance:
                self.generateDayClient()
        elif hour in [18, 19]: # 18 a 20
            if randomNum in self.veryLowChance:
                self.generateDayClient()
        elif hour in [20, 21]: # 20 a 22
            if randomNum in self.highChance:
                self.generateNightClient()
        elif hour == 22: # 22 a 23
            if randomNum in self.mediumChance:
                self.generateNightClient()
        elif hour == 23: # 23 a 24
            if randomNum in self.veryLowChance:
                self.generateNightClient()

clientGenerator = ClientGenerator()