from gestor import GestorAparatos

def main():
    print("⚡ SISTEMA DE CONTROL DE GASTO ELÉCTRICO ⚡")
    gestor = GestorAparatos()

    precio_kwh = float(input("Ingrese el precio de 1 kWh en dólares: "))

    while True:
        print("\n=== REGISTRO DE APARATOS ===")
        nombre = input("Nombre del aparato: ")
        potencia = float(input("Potencia en watts: "))
        horas = float(input("Horas de uso diario: "))
        dias = int(input("Días de uso al mes: "))

        gestor.agregar_aparato(nombre, potencia, horas, dias)

        otro = input("¿Desea registrar otro aparato? (s/n): ").lower()
        if otro != 's':
            break

    # Calcular costos y mostrar resultados
    gestor.calcular_costos(precio_kwh)
    gestor.ordenar_por_consumo()
    gestor.mostrar_resultados()

if __name__ == "__main__":
    main()
