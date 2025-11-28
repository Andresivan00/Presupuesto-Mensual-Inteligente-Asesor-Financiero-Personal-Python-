"""
 ------------------------------
 Función para pedir números enteros al usuario
 ------------------------------
"""
def pedir_numero(mensaje: str) -> int: 
    """
    Pide al usuario un número entero, validando la entrada.
    - 'mensaje' es el texto que se le mostrará al usuario.
    - Si el usuario escribe algo que no es un número, vuelve a preguntar.
    """
    while True:  # bucle infinito hasta que se ingrese un número válido
        try:
            return int(input(mensaje))  # intentamos convertir la entrada a número entero
        except ValueError:
            print("Error: ingrese un número válido.")  # mensaje de error si no es un número

"""
  ------------------------------
  Función para pedir el tipo de vivienda
  ------------------------------
"""

def pedir_tipo_vivienda() -> str:
    """
    Solicita y valida el tipo de vivienda del usuario.
    - Solo acepta 'propia' o 'arrendada'.
    - Si se escribe otra cosa, vuelve a preguntar.
    """
    while True:  # se repite hasta que el usuario escriba una opción correcta
        tipo = input("Escriba si tiene vivienda 'propia' o 'arrendada': ").lower()
        if tipo in ["propia", "arrendada"]:  # comprobamos si la opción es válida
            return tipo
        print("Opción inválida. Intente nuevamente, solo escriba('propia' o 'arrendada').")  # mensaje de error

"""
 ------------------------------
 Función que calcula presupuesto mensual
 ------------------------------
"""
def calcular_presupuesto(salario: int, vivienda: str, arriendo: int, facturas: int, otros: int, ahorro_deseado: int):
    """
    Calcula los egresos (dinero que se gasta) y los ahorros (dinero que sobra).
    - egresos = arriendo + facturas + otros
    - ahorros = salario - egresos
    Retorna ambos valores.
    """
    egresos = arriendo + facturas + otros
    ahorros = salario - egresos
    return egresos, ahorros  # devolvemos una tupla (dos valores)

"""
  ------------------------------
  Función que muestra resultados al usuario
  ------------------------------
"""
def mostrar_resultados(egresos: int, ahorros: int, ahorro_deseado: int, otros: int, facturas: int):
    """
    Muestra en pantalla el resumen del presupuesto y da recomendaciones.
    - Imprime los egresos y los ahorros.
    - Da consejos dependiendo de los gastos y el ahorro deseado.
    """
    print(f"\nSus egresos mensuales son: {egresos}")
    print(f"Sus ahorros mensuales son: {ahorros}")

    # Si los gastos en ocio y comida son mayores o iguales que las facturas, se da una alerta.
    if otros >= facturas:
        print("⚠ sus gastos en otros servicios son muy elevados, deberia intentar ir menos al cine😛")
    
    # Si el ahorro deseado es mayor que el real, se recomienda ajustar los gastos.
    if ahorro_deseado > ahorros:
        print("⚠ Debe tomar medidas para llegar al ahorro deseado, puede comenzar quitando los gastos hormiga.")
    else:
        print("✅ bien hecho, tus deseos se han hecho realidad🤩")


"""
  ------------------------------
  Función principal (punto de entrada del programa)
  ------------------------------

"""
def main():
    """
    Orquesta el programa:
    1. Pide al usuario su salario y gastos.
    2. Calcula presupuesto.
    3. Muestra resultados y recomendaciones.
    """
    print(" Algoritmo financiero para presupuesto mensual ")

    salario = pedir_numero("Ingrese su salario mensual: ")
    vivienda = pedir_tipo_vivienda()
    # Si la vivienda es arrendada, se pregunta el arriendo, si no, el valor es 0.
    arriendo = pedir_numero("Ingrese el gasto de arriendo: ") if vivienda == "arrendada" else 0
    facturas = pedir_numero("Ingrese el promedio de gastos en servicios: ")
    otros = pedir_numero("Ingrese el promedio en otros servicios (comida, entretenimiento): ")
    ahorro_deseado = pedir_numero("Ingrese cuánto desea ahorrar al mes: ")

    # Se calculan los egresos y ahorros usando la función
    egresos, ahorros = calcular_presupuesto(salario, vivienda, arriendo, facturas, otros, ahorro_deseado)
    
    # Se muestran los resultados
    mostrar_resultados(egresos, ahorros, ahorro_deseado, otros, facturas)


"""
  ------------------------------
  Esto asegura que el programa se ejecute solo si se corre directamente
  y no cuando se importa como módulo en otro programa.
  ------------------------------

"""
if __name__ == "__main__":
    main()
