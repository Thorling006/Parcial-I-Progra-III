class Aparato:
    def __init__(self, nombre, potencia_watts, horas_diarias, dias_mes):
        self.nombre = nombre
        self.potencia_watts = potencia_watts
        self.horas_diarias = horas_diarias
        self.dias_mes = dias_mes
        self.consumo_kwh = self.calcular_consumo()
        self.costo = 0.0

    def calcular_consumo(self):
        # Consumo en kWh = (Potencia en watts * horas diarias * días) / 1000
        return (self.potencia_watts * self.horas_diarias * self.dias_mes) / 1000

    def calcular_costo(self, precio_kwh):
        self.costo = self.consumo_kwh * precio_kwh
