serie = "N-02"

if serie == "N-01":
    print("Samsung")
elif serie == "N-02":
    print("Nokia")
elif serie == "N-03":
    print("Motorola")
else:
    print("Do not exist this product")

#We can use match

match serie:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Motorola")
    case _:
        print("Do not exist this product")

client = {"nombre": "Federico",
          "edad": 45,
          "ocupacion": "Instructor"}
pelicula = {"titulo": "Matrix",
            "ficha_tecnica": {
                "protagonista": "Keanu Reeves",
                "director": "Lana y Lilly Wachowski"
            }
            }
elementos = [pelicula, client, 'libro']
for e in elementos:
    match e:
        case {'nombre': nombre,
              'edad': edad,
              'ocupacion': ocupacion}:
            print("Es un cliente")
            print(nombre, edad, ocupacion)
        case {'titulo': titulo,
              'ficha_tecnica' : {
                  'protagonista': protagonista,
                  'director': director
              }}:
            print("Es una pelicula")
            print(protagonista, director)
        case _:
            print("No se que es esto")


