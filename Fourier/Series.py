import numpy as np
import matplotlib.pyplot as plt
def main():
    """
    funcion principal main()
    >Parámetros de entrada:
        sin parametros de entrada
    >variables internas:
        numeroCiclos
    >llamadas a funcion:
        a) ondas(x,presicion,opcion):
            Donde:
            > x (tipo : arreglo): es el valor en el cual se evaluara f(x) 
            > presicion (tipo : entero): limite de la sumatoria de Fourier 
            >opcion(tipo : entero): solo toma 3 valores distintos:
                1) onda cuadrada
                2) onda triangular. 
                3) onda de sierra
        
        b) grafica(x,y,nombre)
            Donde:
            > x(tipo: arreglo de flotantes):valores en los cuales se avalua f(x)
            > y(tipo: arreglo de flotantes):resultados de la evaluacion f(x)
            > nombre (tipo: string): nombre de la grafica

    >valores de retorno:
        sin valores de retorno
    """
    numeroCiclos = 1
    presicion  = 10
    opcion = -1
    
    print('\033[31m' + '****Graficas de las Formulas de Fourier****' + '\033[0m')
    numeroCiclos = int (input("Ciclos que se mostraran en la grafica: "))
    presicion = int (input("Presicion del valor de la serie de Fourier: "))
    print('\033[31m' + '    =============================' + '\033[0m')
    print('\033[32m' + '        1) Onda Cuadrada' + '\033[0m')
    print('\033[33m' + '        2) Onda Triangular' + '\033[0m')
    print('\033[36m' + '        3) Onda de Sierra' + '\033[0m')
    print('\033[31m' + '    =============================' + '\033[0m')
    opcion = int(input("     Elije una opcion: "))
    x = np.linspace(0, 2*numeroCiclos*np.pi, 500)
    y = ondas(x,presicion,opcion)
    if opcion == 1 : nombre = "Onda Cuadrada"
    if opcion == 2 : nombre = "Onda Triangular"
    if opcion == 3 : nombre = "Onda De sierra"
    grafica(x,y,nombre)     


def ondas(x,n,tipo):
    """
    Funcion que regresa la serie segun su tipo
    >Parámetros de entrada:
        tipo(int): variable bandera que identifica el tipo de funcion
            1) Cuadrada.
            2) De pico
            3) De sierra.
    >llamadas a funcion:
        no tiene llamadas a funcion
    >valores de retorno:
        Retorna el resultado de la serie de furier(array)
    """
    suma = 0
    if tipo == 1:  # onda cuadrada
        for i in range(1, n+1):
            suma += (1/(2*i-1))*np.sin((2*i-1)*x)
        return ((4)/np.pi)*suma
    elif tipo == 2:  # onda triangular
        suma = 0
        for i in range(1, n+1):
            if i % 2 == 0:
                suma -= 1/(i**2)*np.sin(i*x)
            else:
                suma += 1/(i**2)*np.sin(i*x)
        return ((8/np.pi**2)*suma)
    elif tipo == 3:  # onda de sierra
        suma = 0
        for i in range(1, n+1):
            suma += (1/i)*np.sin(i*x)
        return -((2)/np.pi)*suma
    else:
        return 0
def grafica(x, y, titulo):
    """
    Funcion la cual grafica usando la libreria matplotlib
    >Parámetros de entrada:
        x(array  float) : valores en x, estan dados en n*pi.
        y (array float) : valores evaluados en x f(x). 
        titulo(string)  : Titulo que desea poner en la grafica.
    >llamadas a funcion:
        funciones(metodos) propias de la libreria matplotlib
    >valores de retorno :
        Esta funcion no retorna un valor. 
    """ 
    plt.title(titulo)                        # Agrega titulo
    plt.plot(x, y)                           # Grafica de x y y
    plt.grid(True)                           # Agrega Cuadricula al grafico   
    plt.xlabel('x')                          # Agrega etiqueta x
    plt.ylabel('y')                          # Agrega etiqueta y
    plt.show()                               # Mostrar el gráfico

main()
