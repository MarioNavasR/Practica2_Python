import csv



def extrac_csv():
# retorna cada fila del archivo csv
    with open("basket_players.csv", 'r') as csvfile:
        print("Archivo abierto exitosamente.")
        filereader = csv.reader(csvfile, delimiter=';')
        return list(filereader)

def write_csv(name,team,paraula_cat,player_height_eurometric,player_weight_eurometric,rounded_age):
    #Escriu cada linea d'un csv a un altre
    with open("new_file.csv","w", ) as newfile:
        #Escriu cada fila
        filewriter = csv.writer(newfile, delimiter='^')
        #Crida a la funcio extract csv per a llegir el fitxer
        datos_csv = extrac_csv()
        for fila in datos_csv:
            filewriter.writerow(fila)

def create_dict(num:int) -> dict:
    dict_column_name = {"Name:Nom","Team:Equip","Position:Posicio","Heigth:Altura","Weigth:Pes","Age:Edat"}
    dict_player_positions = {"Point Guard":"Base","Shooting Guard":"Escorta","Small Forward":"Aler","Power Forward":"Ala-pivot","Center":"Pivot"}
    if(num == 0):
        return dict_column_name
    else:
        return dict_player_positions

def modify_csv():
    datos_csv = extrac_csv()
    dict_player_positions = create_dict(1)
    line_number = 0
    count = 0
    #Itera per a cada linea i canvia la posició d'angles a catala
    for line in datos_csv:
        line_number = line_number + 1
        if line_number == 1:
            line = create_dict(0)
        if line_number > 1:
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

def calculate_metrics(player_data,metric):
    return round(player_data*metric,2)

def round_age(age:str) -> int:
    player_age = round(float(age))
    return player_age


def statistics_highest_smallest_weight():
    highest = 0
    smaller = 0
    #Agafa la posicio del pes i del nom de cada fila
    #weight = dict({"Nom":"linea","Pes":"lineax" ,})
    #Recorre cada fila amb el nom i el pes
    for i in weight:
        #compara el pes mes gran
        if(i > highest):
            i = highest
        if(i< highest):
            i = smaller

def __main__():
    print("Selecciona una Exercici:")
    print("1. Exercici 1")
    print("2. Exercici 2")
    print("3. Exercici 3")
    
    choice = input("Ingresa el número de la Exercici deseada: ")
    
    match choice:
        case "1":
            print("Has seleccionado ETL from csv.")
            # Coloca aquí el código para la Exercici 1
            modify_csv()
        case "2":
            print("Has seleccionado Estadístiques.")
            # Coloca aquí el código para la Exercici 2
        case "3":
            print("Has seleccionado Canvia el format de dades.")
            # Coloca aquí el código para la Exercici 3
        case _:
            print("Exercici no válida. Por favor, selecciona una Exercici válida.")

modify_csv()