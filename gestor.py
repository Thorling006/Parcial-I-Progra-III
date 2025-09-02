from aparato import Aparato

class GestorAparatos:
    def __init__(self):
        self.aparatos = []

    def agregar_aparato(self, nombre, potencia, horas, dias):
        aparato = Aparato(nombre, potencia, horas, dias)
        self.aparatos.append(aparato)

    def calcular_costos(self, precio_kwh):
        for aparato in self.aparatos:
            aparato.calcular_costo(precio_kwh)

    def ordenar_por_consumo(self):
        self.aparatos.sort(key=lambda x: x.consumo_kwh, reverse=True)

    def mostrar_resultados(self):
        print("\n📌 CONSUMO DE APARATOS ORDENADO POR MAYOR CONSUMO")
        print("-" * 70)
        print(f"{'Aparato':<20}{'Consumo (kWh)':<20}{'Costo ($)':<20}")
        print("-" * 70)
        for aparato in self.aparatos:
            print(f"{aparato.nombre:<20}{aparato.consumo_kwh:<20.2f}${aparato.costo:<20.2f}")

        consumo_total = sum(a.consumo_kwh for a in self.aparatos)
        gasto_total = sum(a.costo for a in self.aparatos)
        print("-" * 70)
        print(f"{'TOTAL':<20}{consumo_total:<20.2f}${gasto_total:<20.2f}")
        print("-" * 70)
