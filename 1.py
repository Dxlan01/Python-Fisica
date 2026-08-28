while True:
    print("_______________________")
    print("Ejercicios Propuestos")
    print("_______________________")
    print("Digite el numero del ejercicio que desea ver(1-7):")
    
    opcion=(int("Digite la opcion segun el ejercicio que quiere ver: "))
    if opcion == 0:
        print("Saliendo del programa")
        print("Bay")
        break
    elif opcion == 1:
        print("El ejercicio es: Un dron recorre 300 metros en 20 segundos. Calcule su rapidez.")
        print("Datos:\n Distancia=300m.\n Tiempo=20s.")
        rapidez=300/20
        print(f"La rapidez del robot es:{rapidez}")
    elif opcion== 2:
        print("El ejercicio es: Un robot se desplaza a 1,8 m/s durante 50 segundos. Calcule la distancia.")
        print("Datos: \nVelocidad=1.8m/s. \nTiempo=50s")
        distancia=1.8*50
        print(f"La distancia que recorrio el robot fue de: {distancia}")
    elif opcion== 3:
        print("El ejercicio es: Una banda transportadora recorre 500 metros a 5 m/s. Calcule el tiempo.")
        print("Datos: \nDistancia=500m. \nVelocidad=5m/s")
        tiempo=500/5
        print(f"El tiempo de la banda transportadora es de: {tiempo}")
    elif opcion == 4:
        print("El ejercicio es: Un vehículo pasa de 10 m/s a 30 m/s en 4 segundos. Calcule la aceleración.")
        print("Datos: \nTiempo= 4s. \nVelocidadI= 10m/s. \nVelocidadF= 30m/s")
        aceleracion= (30-10)/4
        print(f"La aceleracion del vehiculo es de: {aceleracion}")
    elif opcion == 5:
        print("El ejercicio es: Un aprendiz camina 15 metros al norte y después 6 metros al sur. Calcule: \nDistancia. \nDesplazamiento.")
        print("Datos: \nDistancia1= 15m al norte. \n")
