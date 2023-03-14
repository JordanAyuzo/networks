import numpy as np
import matplotlib.pyplot as plt
def main():
    """
    funcion principal main()
    >Parámetros de entrada:
        sin parametros de entrada
    >variables internas:
        - nombre(string) :  Nombre y Titulo de la grafica 
        - numeroCiclos(entero): Numero de ciclos que se mostraran.
        - presicion(enetero):Veces que se itera la suma
        - opcion(entero): Define el tipo de onda.

    >llamadas a funcion:
        a) ondas(x,presicion,opcion):
            Donde:
            - x (tipo : arreglo): es el valor en el cual se evaluara f(x) 
            - presicion (tipo : entero): limite de la sumatoria de Fourier 
            - opcion(tipo : entero): solo toma 3 valores distintos:
                1) onda cuadrada
                2) onda triangular. 
                3) onda dientes de sierra
        
        b) grafica(x,y,nombre)
            Donde:
            - x(tipo: arreglo de flotantes):valores en los cuales se avalua f(x)
            - y(tipo: arreglo de flotantes):resultados de la evaluacion f(x)
            - nombre (tipo: string): nombre de la grafica

    >valores de retorno:
        sin valores de retorno
    """
    nombre = ""
    numeroCiclos = 1
    presicion  = 10
    opcion = -1
    #TODO OPTIONAL: los if de hasta abajo son opcionales, por si presionan otra tecla que no es valida 
    while opcion != 4:
        print('\033[31m' + '****Graficas de las Formulas de Fourier****' + '\033[0m')
        print('\033[31m' + '    =============================' + '\033[0m')
        print('\033[32m' + '        1) Onda Cuadrada' + '\033[0m')
        print('\033[33m' + '        2) Onda Triangular' + '\033[0m')
        print('\033[36m' + '        3) Onda dientes de Sierra' + '\033[0m')
        print('\033[35m' + '        4) Salir' + '\033[0m')
        print('\033[31m' + '    =============================' + '\033[0m')
        opcion = int(input("     Elije una opcion: "))
        if opcion == 1 : nombre = "Onda Cuadrada"
        if opcion == 2 : nombre = "Onda Triangular"
        if opcion == 3 : nombre = "Onda Dientes de Sierra"
        if nombre == "" and opcion!= 4:
            print("Elegiste una opción incorrecta")
        elif(nombre != ""):
            numeroCiclos = int (input("Rango de angulos en la grafica: "))
            presicion = int (input("Numero de terminos para la serie de Fourier: "))
            x = np.linspace(0, 2*numeroCiclos*np.pi, 500)
            y = ondas(x,presicion,opcion)
            grafica(x,y,nombre)
            nombre = ""     
def ondas(x,n,tipo):
    """
    Funcion que regresa la serie segun su tipo
    >Parámetros de entrada:

        - x(array de flotantes): variable que contiene los valores del eje x para f(x)
        - n(int): numero de iteraciones para la suma 
        - tipo(int): variable bandera que identifica el tipo de funcion
            1) Cuadrada.
            2) De pico
            3) Dientes de sierra.

     >variables internas:

        - suma:(array de floats)  guarda la sumatoria para despues multiplicarla
        - signo:(int)  alterna el signo + - para la sumatoria de la onda dientes de sierra
    >llamadas a funcion:

        no tiene llamadas a funcion.

    >valores de retorno:

        Retorna el resultado de la serie de furier(array)
    """
    suma  = 0
    signo = 1
    if tipo == 1:  # onda cuadrada
        for i in range(1, n+1):
            suma += (1/(2*i-1))*np.sin((2*i-1)*x)
        return ((4)/np.pi)*suma
    elif tipo == 2:  # onda triangular
        for i in range(1, n+1,2):
            if signo % 2 == 0:
                suma -= 1/(i**2)*np.sin(i*x)
            else:
                suma += 1/(i**2)*np.sin(i*x)
            signo+=1
        return ((8/np.pi**2)*suma)
    elif tipo == 3:  # onda dientes de sierra 
        for i in range(1, n+1):
            suma += (1/i)*np.sin(i*x)
        return -((2)/np.pi)*suma
    else:
        return 0
def grafica(x, y, titulo):
    """
    Funcion la cual grafica usando la libreria matplotlib
    >Parámetros de entrada:
        - x(array  float) : valores en x, estan dados en n*pi.
        - y (array float) : valores evaluados en x f(x). 
        - titulo(string)  : Titulo que desea poner en la grafica.
    >variables internas :
        - abscisa (CONSTANTE):es el eje x que siempre es 0
    >llamadas a funcion:
        funciones(metodos) propias de la libreria matplotlib
    >valores de retorno :
        Esta funcion no retorna un valor. 
    """ 
    ABSCISA = np.zeros_like(x)               # valores para dibujar eje x
    plt.title(titulo)                        # Agrega titulo
    plt.plot(x, y)                           # Grafica de x y y
    plt.plot(x, ABSCISA,color='black')       # Grafica la abscisa
    plt.grid(True)                           # Agrega Cuadricula al grafico   
    plt.xlabel('x')                          # Agrega etiqueta x
    plt.ylabel('y')                          # Agrega etiqueta y
    plt.show()                               # Mostrar el gráfico

main()
