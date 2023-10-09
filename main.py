import csv
import json

# retorna cada fila del archivo csv
def extract_csv():
    with open('basket_players.csv', 'r', newline='', encoding='ascii') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=';')
        next(csv_reader)  # Saltar la primera línea que contiene los encabezados
        data = [row for row in csv_reader]
        return data


#Factor de conversió
def calculate_metrics(player_data,metric):
    return round(player_data*metric,2)

#Retorna l'edat redondejada com a int
def round_age(age:str) -> int:
    player_age = round(float(age))
    return player_age

#Depenent del input envia un dict o un altre.
def create_dict(num:int) -> dict:
    dict_column_name = {"Name:Nom","Team:Equip","Position:Posicio","Heigth:Altura","Weigth:Pes","Age:Edat"}
    dict_player_positions = {"Point Guard":"Base","Shooting Guard":"Escorta","Small Forward":"Aler","Power Forward":"Ala-pivot","Center":"Pivot"}
    if(num == 0):
        return dict_column_name
    else:
        return dict_player_positions



def modify_csv():
    datos_csv = extract_csv()
    dict_player_positions = create_dict(1)
    count = 1
    modified_data = []

    #Itera per a cada linea i canvia la posició d'angles a catala
    for line in datos_csv:
        name = line[0]
        team = line[1]
        #Aagafa la posició de la posocio referent a Position per a iterar per cada linea del csv.
        player_position = line[2]
        paraula_cat = dict_player_positions[player_position]

        #Cambia els valors de height i weight de basket_players a sistema metric europeu.
        player_height = float(line[3])
        player_weight = float(line[4])
        metric_height = 2.54 # Factor de conversio a CM's
        metric_weight = 0.45 # Factor de conversio a KG
        player_height_eurometric = calculate_metrics(player_height,metric_height)
        player_weight_eurometric = calculate_metrics(player_weight,metric_weight)

        #Cambia el valor age de decimal a int
        rounded_age = round_age(line[5])

        print(name,team,paraula_cat,player_height_eurometric,player_weight_eurometric,rounded_age)
        count = count+1
        print(count)
        # Agregar los datos modificados a la lista
        modified_data.append([name, team, paraula_cat, player_height_eurometric, player_weight_eurometric, rounded_age])
        write_csv(modified_data)

def write_csv(data):
    nueva_cabecera = ["Nom", "Equip", "Posicio", "Altura", "Pes", "Edat"]

    with open('new_file.csv', 'w', newline='', encoding='ascii') as salida_csvfile:
        csv_writer = csv.writer(salida_csvfile, delimiter='^')

        # Escribir la nueva cabecera
        csv_writer.writerow(nueva_cabecera)

        # Escribir los datos transformados
        csv_writer.writerows(data)
        print("Los datos han sido escritos con exito.")

#Carregar data del fitxer modificat
def load_data():
    data = []
    with open("new_file.csv", 'r', encoding='ascii') as csvfile:
        csvreader = csv.reader(csvfile, delimiter='^')
        header = next(csvreader)  # Saltar la cabecera
        for row in csvreader:
            data.append(row)
    return data

#Calcular jugador amb pes mes alt
def player_highest_weight():
    data = load_data()
    max_weight = 0
    player = ""
    for row in data:
        weight = float(row[4])
        if weight > max_weight:
            max_weight = weight
            player = row[0]
    return print("a) Jugador con el peso más alto:", player)

#Calcular jugador amb height mes baixa.
def player_smallest():
    data = load_data()
    min_altura = float('inf')
    player = ""
    for row in data:
        height = float(row[3])
        if height < min_altura:
            min_altura = height
            player = row[0]
            
    return print("b) Jugador con la altura más baja:", player)

#Calcular la mitjana de pes per equip
def average_weight_height_per_team():
    data = load_data()
    teams = {}
    for row in data:
        team = row[1]
        weight = float(row[4])
        height = float(row[3])
        if team in teams:
            teams[team]['weight_total'] += weight
            teams[team]['altura_total'] += height
            teams[team]['count'] += 1
        else:
            teams[team] = {'weight_total': weight, 'altura_total': height, 'count': 1}
    for team, stats in teams.items():
        stats['media_weight'] = stats['weight_total'] / stats['count']
        stats['media_altura'] = stats['altura_total'] / stats['count']
    #return print("c) Equipo: ",{teams} "Media de peso:", {stats['media_weight']:.2f}" kg, Media de altura: "{stats['media_altura']:.2} "cm")

#Contar jugadors per posicio
def count_players_by_position():
    data = load_data()
    posiciones = {}
    for row in data:
        posicion = row[2]
        if posicion in posiciones:
            posiciones[posicion] += 1
        else:
            posiciones[posicion] = 1
    return posiciones

#calcular jugadors per edat
def distribution_players_by_age():
    data = load_data()
    edades = {}
    for row in data:
        edad = int(float(row[5]))
        if edad in edades:
            edades[edad] += 1
        else:
            edades[edad] = 1
    return edades

#llegeix el fitxer csv i el transforma a json.
def to_json():
    data = load_data()
    with open("json_file.json", "w") as json_file:
        json.dump(data,json_file,indent=4)


def __main__():
    print("Selecciona una Exercici:")
    print("1. Exercici 1")
    print("2. Exercici 2")
    print("3. Exercici 3")
    
    choice = input("Ingresa el número de la Exercici deseada: ")
    
    match choice:
        case "1":
            print("Has seleccionado ETL from csv.")
            modify_csv()
        case "2":
            print("Has seleccionado Estadístiques.")
            player_highest_weight()
            player_smallest()
        case "3":
            print("Has seleccionado Canvia el format de dades.")
            to_json()
        case _:
            print("Exercici no válida. Por favor, selecciona una Exercici válida.")

__main__()