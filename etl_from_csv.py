import csv



def extrac_csv():
# Printa cada fila del archivo csv
    with open("basket_players.csv", 'r') as csvfile:
        print("Archivo abierto exitosamente.")
        filereader = csv.reader(csvfile, delimiter=',')
        num_rows = 0
        for row in filereader:
            print(row)
            num_rows += 1
        print('Numero total de files:',num_rows)

'''
1-
'''
player_position ={
    "Point Guard": "Base",
    "Shooting Guard": "Escolta",
    "Small Forward": "Aler",
    "Power Forward":"Ala-pivot",
    "Center": "Pivot"

}
#Name,Team,Position,Heigth,Weigth,Age
def age_change():
    #Redondear la sexta posicion de la edad 


def transform_csv():
    

def load_csv():
    file_writer = csv.writer(cs, delimeter='^')

def _init_():
    extrac_csv()
    transform_csv()

    
