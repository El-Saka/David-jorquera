from pelicula import agregar_pelicula, mostrar_peliculas, buscar_pelicula_por_categoria, cargar_peliculas

def main():
    peliculas = cargar_peliculas()
    
    while True:
        print("\nMenú de Usuario")
        print("1. Agregar Película")
        print("2. Mostrar todas las películas")
        print("3. Buscar películas por categoría")
        print("4. Salir")
        
        try:
            opcion = int(input("Seleccione una opción: "))
            
            if opcion == 1:
                agregar_pelicula(peliculas)
            elif opcion == 2:
                mostrar_peliculas(peliculas)
            elif opcion == 3:
                buscar_pelicula_por_categoria(peliculas)
            elif opcion == 4:
                print("¡Gracias por usar el sistema de gestión de películas!")
                break
            else:
                print("Opción no válida. Intente de nuevo.")
        
        except ValueError:
            print("Error: Debe ingresar un número.")

if __name__ == "__main__":
    main()
