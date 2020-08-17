import random
from random import randint

limpio = ' '
sucio = 'x'
poco = '+'
permanente = '#'
pared = '?'
baldosas = [limpio, sucio, poco, permanente]
piso = [pared]

class Aspiradora:
    posicion = 0
    direccion = 'derecha'
    movimientos_totales = 0
    movimientos_direccion = 0
    movimientos_avanzar = 0
    movimientos_limpiar = 0


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
    aspiradora.posicion = random.randrange(1, len(piso) - 1)  # posicion de la aspiradora inicial es aleatoria
    for i in range(0, 30):
        if piso[aspiradora.posicion] == pared:
            if aspiradora.direccion == 'derecha':
                aspiradora.girar_izquierda()
                aspiradora.avanzar()
            elif aspiradora.direccion == 'izquierda':
                aspiradora.girar_derecha()
                aspiradora.avanzar()
        if piso[aspiradora.posicion] == poco:
            aspiradora.limpiar()
            piso[aspiradora.posicion] = limpio
        elif piso[aspiradora.posicion] == sucio:
            aspiradora.limpiar()
            piso[aspiradora.posicion] = poco
        elif piso[aspiradora.posicion] == permanente:
            aspiradora.limpiar()
        mostrar_piso()
        aspiradora.mostrar_aspiradora()
        aspiradora.avanzar()
        print('')
        
    print('Movimientos totales: ' + str(aspiradora.movimientos_totales))
    print('Movimientos direccion: ' + str(aspiradora.movimientos_direccion))
    print('Movimientos avanzar: ' + str(aspiradora.movimientos_avanzar))
    print('Movimientos limpiar: ' + str(aspiradora.movimientos_limpiar))


