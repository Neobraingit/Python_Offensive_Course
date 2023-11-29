#!/usr/bin/env python3

class Vehiculo:
    def __init__(self, matricula, modelo):
        self.matricula = matricula
        self.modelo = modelo
        self.disponible = True

class Flota:
    def __init__(self):
        self.vehiculos = []
        
    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)
        
    def __str__(self):
        return '\n'.join(str(vehiculo for vehiculo in self.vehiculos))


if __name__ == '__main__':
    
    flota = Flota()
    flota.agregar_vehiculo(Vehiculo('5898MJZ', 'Toyota Corolla'))
    flota.agregar_vehiculo(Vehiculo('1234MJZ', 'Honda Civic'))
    
print (f'[+] Flota inicial {flota}')