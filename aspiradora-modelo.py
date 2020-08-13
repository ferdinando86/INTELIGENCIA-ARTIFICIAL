import random

# Estado de las baldosas

limpio = ' '
sucio = 'x'
poco = '+'
permanente = '#'
pared = '?'
piso = [pared, limpio, sucio, poco, permanente, limpio, limpio, pared]


class Aspiradora:
    posicion = random.randrange(1, len(piso)-1)
    direccion = 'derecha'
    movimientos = 0
    condicion_piso = [0] * len(piso)

    def set_condicion_piso(self):
        for i in range(0, len(piso)):
            self.condicion_piso[i] = 0

    def update_condicion_piso(self):
        self.condicion_piso[self.posicion] = self.condicion_piso[self.posicion] + 1

    def avanzar(self):
        self.movimientos += 1
        if self.direccion == 'izquierda':
            self.posicion -= 1
        elif self.direccion == 'derecha':
            self.posicion += 1
        print('Avance \n')

    def girar_izquierda(self):
        self.movimientos += 1
        self.direccion = 'izquierda'
        print('Gire a la izquierda \n')

    def girar_derecha(self):
        self.movimientos += 1
        self.direccion = 'derecha'
        print('Gire a la derecha \n')

    def limpiar(self):
        self.movimientos += 1
        '''self.update_condicion_piso()'''

        if piso[aspiradora.posicion] == poco:
            piso[aspiradora.posicion] = limpio
        elif piso[aspiradora.posicion] == sucio:
            piso[aspiradora.posicion] = poco


        print('Limpie \n')

    def revisar_suciedad(self):
        self.movimientos += 1
        print('Limpie \n')

    def mostrar_aspiradora(self):
        cadena=''
        for i in range(0,len(piso)):
            if i == self.posicion:
                cadena = cadena + '|A|'
            else:
                cadena = cadena + '| |'
        print(cadena)

def mostrar_piso():
    cadena = ''
    for i in range(0, len(piso)):
        cadena = cadena + '|' + piso[i] + '|'
    print(cadena)



if __name__ == '__main__':
    clean = False
    aspiradora = Aspiradora()
    aspiradora.set_condicion_piso()
    for i in range(0, 100):
        if aspiradora.condicion_piso[aspiradora.posicion] == 0:
            if piso[aspiradora.posicion] == pared:
                if aspiradora.direccion == 'derecha':
                    aspiradora.girar_izquierda()
                    aspiradora.avanzar()
                elif aspiradora.direccion == 'izquierda':
                    aspiradora.girar_derecha()
                    aspiradora.avanzar()
            aspiradora.update_condicion_piso()
            for i in range(0, 2):
                if piso[aspiradora.posicion] != limpio:
                    aspiradora.limpiar()
        else:
            print('por aca pase')
            aspiradora.avanzar()
        mostrar_piso()
        aspiradora.mostrar_aspiradora()
        aspiradora.avanzar()






        '''if condicion_piso[i] == 1:
        aspiradora.limpiar()
        if piso[aspiradora.posicion] == poco:
            aspiradora.limpiar()
            if condicion_piso[i] != 

            piso[aspiradora.posicion] = limpio
        elif piso[aspiradora.posicion] == sucio:
            aspiradora.limpiar()
            aspiradora.limpiar()
            piso[aspiradora.posicion] = poco
        elif piso[aspiradora.posicion] == permanente:
            aspiradora.limpiar()
            aspiradora.limpiar()'''