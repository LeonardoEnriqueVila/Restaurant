def getTables(): # obtiene mediante input la cantidad de mesas disponibles
    while True:
        try:
            tables = int(input("Enter Number of Tables: "))
            if tables < 1 or tables > 500:
                print("Enter number between 1 and 500")
            else:
                return tables
        except ValueError:
            print("Enter number between 1 and 500")

def getTimeRange(): # obtiene mediante input el rango de tiempo de estadía en mesas
    timeRange = [] # [0] minimo [1] maximo
    while True:
        try:
            flag = False
            while flag == False:
                min = int(input("Enter MIN time on tables: "))
                if min < 15 or min > 60: # tiempo minimo permitido entre 15m y 1h
                    print("Min time allowed between 15 and 60 minutes")
                    flag = False
                else:
                    flag = True
            flag = False
            while flag == False:
                max = int(input("Enter MAX time on tables: "))
                if max < 30 or max > 180 or max < min: # tiempo maximo permitido entre 30m y 3hs. Asegura que sea mayor que MIN
                    flag = False
                    print(f"Max time allowed between 30 and 180 minutes. Max must be greater than {min}")
                else:
                    flag = True
            if flag:
                timeRange.extend([min, max])
                return timeRange
        except ValueError:
            print("Enter valid input.")