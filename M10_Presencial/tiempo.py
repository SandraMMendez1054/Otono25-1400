#TODO1:Definición de la clase Time

class Tiempo:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
        self._normalize()

       
def __str__(self):
        return f"{self.hour:02}:{self.minute:02}:{self.second:02}"

def _normalize(self):
        self.minutos += self.segundos // 60
        self.segundos %= 60
        self.horas += self.minutos // 60
        self.minutos %= 60
        self.horas %= 24

        # Ahora ajusta el tiempo si excede
def incrementar_tiempo(self, horas, minutos, segundos):
        self.segundos += segundos
        self.minutos += minutos
        self.horas += horas
        self._normalize()
        return self


#TODO2: Convirtiendo tiempo original en segundos
# convertir el total de segundos aun objeto tiempo

def tiempo_a_int(tiempo):
    return tiempo.horas * 3600 + tiempo.minutos * 60 + tiempo.segundos

def int_a_tiempo(segundos):
      minutos, segundos = divmod(segundos, 60)
      horas, minutos = divmod(minutos, 60)
      return Tiempo(horas, minutos, segundos)


def sumar_tiempo(tiempo, horas, segundos, minutos):
    total_segundos = tiempo_a_int(tiempo) + horas * 3600 + minutos * 60 + segundos
    return tiempo_a_int(total_segundos)

mi_hora = Tiempo(14,30,15)
print("Hora inicial:", mi_hora)

nueva_hora = sumar_tiempo(mi_hora, 2, 45, 30)
print("Nueva hora:", nueva_hora)

mi_hora.incrementar_tiempo(1, 45, 30)
print("Hora incrementada:", mi_hora)

mi_hora.incrementar_tiempo(3, 0, 0)
print("Hora incrementada nuevamente:", mi_hora)

tiempo_desbordado = sumar_tiempo(mi_hora, 0, 120, 3600)
print("hora despues del overflow:", tiempo_desbordado)







    














