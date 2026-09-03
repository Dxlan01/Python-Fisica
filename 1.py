while True:
    print("-----------------------")
    print("Ejercicios Propuestos")
    print("-----------------------")
    print("Digite el numero del ejercicio que desea ver(1-7):")
    
    opcion=int(input("Digite la opcion segun el ejercicio que quiere ver: "))
    if opcion == 0:
        print("Saliendo del programa")
        print("Bay")
        break
    elif opcion == 1:
        print("El ejercicio es: Un dron recorre 300 metros en 20 segundos. Calcule su rapidez.")
        print("Datos:\n Distancia=300m.\n Tiempo=20s.")
        rapidez=300/20
        print(f"Respuesta: La rapidez del robot es:{rapidez}m/s")
    elif opcion== 2:
        print("El ejercicio es: Un robot se desplaza a 1,8 m/s durante 50 segundos. Calcule la distancia.")
        print("Datos: \nVelocidad=1.8m/s. \nTiempo=50s")
        distancia=1.8*50
        print(f"Respuesta: La distancia que recorrio el robot fue de: {distancia}m")
    elif opcion== 3:
        print("El ejercicio es: Una banda transportadora recorre 500 metros a 5 m/s. Calcule el tiempo.")
        print("Datos: \nDistancia=500m. \nVelocidad=5m/s")
        tiempo=500/5
        print(f"Respuesta: El tiempo de la banda transportadora es de: {tiempo}s")
    elif opcion == 4:
        print("El ejercicio es: Un vehículo pasa de 10 m/s a 30 m/s en 4 segundos. Calcule la aceleración.")
        print("Datos: \nTiempo= 4s. \nVelocidadI= 10m/s. \nVelocidadF= 30m/s")
        aceleracion= (30-10)/4
        print(f"Respuesta: La aceleracion del vehiculo es de: {aceleracion}m/s")
    elif opcion == 5:
        print("El ejercicio es: Un aprendiz camina 15 metros al norte y después 6 metros al sur. Calcule: \nDistancia. \nDesplazamiento.")
        print("Datos: \nDistancia1= 15m al norte. \nDistancia2= 6m al sur")
        Distancia1= 15+6
        Desplazamiento= 15-6
        print(f"Respuesta: La distancia del  aprendiz es de {Distancia1}m.\nY el desplazamiento del aprendiz es de {Desplazamiento}m al norte.")
    elif opcion == 6:
        print("El ejercicio es: Un servidor movil de un centro de datos recorre 80 metros en 40 segundos. Determine su velocidad promedio.")
        print("Datos: \nDistancia=80m. \nTiempo=40s")
        Velodcidad=80/40
        print(f"Respuesta: La velovidad promedio a la que se mueve el servidor movil es de: {Velodcidad}m/s.")
    elif opcion == 7:
        print("El ejercicio es: Explique la diferencia entre rapidez y velocidad.")
        print("Respuesta: La diferencia es que la rapidez es la que solo indica que tan deprisa se mueve un objeto, mientras que la velocidad indica que tan deprisa se mueve y tambien hacia donde lo hace")
    else:
        print("Opcion no valida")
