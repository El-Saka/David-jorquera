import random
import math

def agregar_pelicula(peliculas):
    try:
        codigo = input("Ingrese el código de la película: ")
        nombre = input("Ingrese el nombre de la película: ")
        año = int(input("Ingrese el año de la película: "))
        categoria = input("Ingrese la categoría de la película: ")
        actores = input("Ingrese los actores de la película (separados por comas): ").split(',')
        director = input("Ingrese el director de la película: ")
        
        pelicula = {
            'codigo': codigo,
            'nombre': nombre,
            'año': año,
            'categoria': categoria,
            'actores': actores,
            'director': director
        }
        
        peliculas.append(pelicula)
        print("Película agregada con éxito.")
        
        with open('peliculas.txt', 'a') as file:
            file.write(f"{codigo},{nombre},{año},{categoria},{'|'.join(actores)},{director}\n")
        
    except ValueError:
        print("Error: El año debe ser un número.")

def mostrar_peliculas(peliculas):
    if not peliculas:
        print("No hay películas para mostrar.")
        return
    
    for pelicula in peliculas:
        print(f"Código: {pelicula['codigo']}, Nombre: {pelicula['nombre']}, Año: {pelicula['año']}, Categoría: {pelicula['categoria']}, Actores: {', '.join(pelicula['actores'])}, Director: {pelicula['director']}")

def buscar_pelicula_por_categoria(peliculas):
    categoria = input("Ingrese la categoría de la película a buscar: ")
    encontradas = [p for p in peliculas if p['categoria'].lower() == categoria.lower()]
    
    if encontradas:
        for pelicula in encontradas:
            print(f"Código: {pelicula['codigo']}, Nombre: {pelicula['nombre']}, Año: {pelicula['año']}, Categoría: {pelicula['categoria']}, Actores: {', '.join(pelicula['actores'])}, Director: {pelicula['director']}")
    else:
        print("No se encontraron películas en esa categoría.")

def cargar_peliculas():
    peliculas = []
    try:
        with open('peliculas.txt', 'r') as file:
            for linea in file:
                codigo, nombre, año, categoria, actores, director = linea.strip().split(',')
                actores = actores.split('|')
                pelicula = {
                    'codigo': codigo,
                    'nombre': nombre,
                    'año': int(año),
                    'categoria': categoria,
                    'actores': actores,
                    'director': director
                }
                peliculas.append(pelicula)
    except FileNotFoundError:
        print("Archivo de películas no encontrado, se creará uno nuevo.")
    except Exception as e:
        print(f"Error al cargar películas: {e}")
    
    return peliculas
