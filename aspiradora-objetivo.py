import random
from random import randint

limpio = ' '
sucio = 'x'
poco = '+'
permanente = '#'
pared = '?'
baldosas = [limpio, sucio, poco, permanente]
piso = [pared]
contador_pared = 0

class Aspiradora:
    posicion = 0
    direccion = 'derecha'
    movimientos_totales = 0
    movimientos_direccion = 0
    movimientos_avanzar = 0
    movimientos_limpiar = 0
    condicion_piso = [0] * len(piso)

    def set_condicion_piso(self):
        for i in range(len(piso)):
            self.condicion_piso.append(0)

    def update_condicion_piso(self):
        self.condicion_piso[self.posicion] = self.condicion_piso[self.posicion] + 1

    def avanzar(self):
        self.movimientos_totales += 1
        self.movimientos_avanzar += 1
        if self.direccion == 'izquierda':
            self.posicion -= 1
        elif self.direccion == 'derecha':
            self.posicion += 1
        print('Avance')

    def girar_izquierda(self):
        self.movimientos_totales += 1
        self.movimientos_direccion += 1
        self.direccion = 'izquierda'
        print('Gire a la izquierda')

    def girar_derecha(self):
        self.movimientos_totales += 1
        self.movimientos_direccion += 1
        self.direccion = 'derecha'
        print('Gire a la derecha')

    def limpiar(self):
        self.movimientos_totales += 1
        self.movimientos_limpiar += 1
        if piso[aspiradora.posicion] == poco:
            piso[aspiradora.posicion] = limpio
        elif piso[aspiradora.posicion] == sucio:
            piso[aspiradora.posicion] = poco
        print('Limpie')

    def definir_piso(self):
        for i in range(randint(0,20)):   # cantidad de baldosas aleatorias, el piso puede estar definido por un numero aleatorio entre 0 y 20 baldosas
            piso.append(random.choice(baldosas))   # la configuracion del piso es aleatoria, se genera el array piso con los tipos de manchas aleatoriamente gracias a la funcion choice
        piso.append(pared)

    def mostrar_aspiradora(self):
        cadena ='|'
        for i in range(0,len(piso)):
            if i == self.posicion:
                cadena = cadena + 'A|'
            elif i != self.posicion and i != len(piso):
                cadena = cadena + ' |'
        print(cadena)

def mostrar_piso():
    cadena = '|'
    for i in range(0, len(piso)):
        cadena = cadena  + piso[i] + '|'
    print(cadena)


if __name__ == '__main__':
    aspiradora = Aspiradora()
    aspiradora.definir_piso()
    aspiradora.set_condicion_piso()
    aspiradora.posicion = random.randrange(1, len(piso) - 1)  # posicion de la aspiradora inicial es aleatoria
    for i in range(0, 50):
        if aspiradora.condicion_piso[aspiradora.posicion] == 0:
            if piso[aspiradora.posicion] == pared:
                contador_pared = contador_pared + 1
                if contador_pared == 2:
                    break
                if aspiradora.direccion == 'derecha':
                    aspiradora.girar_izquierda()
                    aspiradora.avanzar()
                elif aspiradora.direccion == 'izquierda':
                    aspiradora.girar_derecha()
                    aspiradora.avanzar()
                aspiradora.update_condicion_piso()
            else:
                for i in range(0, 2):
                    if piso[aspiradora.posicion] != limpio:
                        aspiradora.limpiar()
                aspiradora.update_condicion_piso()
        else:
            print('por aca pase')
            aspiradora.avanzar()
        mostrar_piso()
        aspiradora.mostrar_aspiradora()
        aspiradora.avanzar()
        print('')

    print('Movimientos totales: ' + str(aspiradora.movimientos_totales))
    print('Movimientos direccion: ' + str(aspiradora.movimientos_direccion))
    print('Movimientos avanzar: ' + str(aspiradora.movimientos_avanzar))
    print('Movimientos limpiar: ' + str(aspiradora.movimientos_limpiar))