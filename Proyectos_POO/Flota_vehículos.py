#!/usr/bin/env python3

class Vehiculo:
    def __init__(self, matricula, modelo):
        self.matricula = matricula
        self.modelo = modelo
        self.disponible = True
        
    def alquilar(self):
        if self.disponible:
            self.disponible = False
        else:
            print (f' El vehículo con matrícula {self.matricula} no se puede alquilar')
            
            
    def __str__(self):
        return f'Vehiculo(matricula = {self.matricula}, modelo = {self.modelo}, disponible = {self.disponible})'
class Flota:
    def __init__(self):
        self.vehiculos = []
        
    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)
        
    def alquilar_vehiculo(self, matricula):
        for vehiculo in self.vehiculos:
            if vehiculo.matricula == matricula:
                vehiculo.alquilar()
                
        
    def __str__(self):
        return '\n'.join(str(vehiculo for vehiculo in self.vehiculos))


if __name__ == '__main__':
    
    flota = Flota()
    flota.agregar_vehiculo(Vehiculo('5898MJZ', 'Toyota Corolla'))
    flota.agregar_vehiculo(Vehiculo('1234MJZ', 'Honda Civic'))
    
print ('[+] Flota inicial\n')
print (flota)

print ('\nMostrando la flota después de haber alquilado el Toyota:\n')
print (flota)


print (flota)