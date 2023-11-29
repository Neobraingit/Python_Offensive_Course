#!/usr/bin/env python3

class Libro:
    def __init__(self, id_libro, autor, titulo):
        self.id_libro = id_libro
        self.autor = autor
        self.titulo = titulo
        self.prestado = False
        
    def __str__(self):
         return 'Libro {} {} {}'.format(self.id_libro, self.autor, self.titulo)
     
    def __repr__(self) :
        return self.__str__()
         

class Biblioteca:
    def __init__(self):
        self.libros = {}
        
    def agregar_libro(self, libro):
        if libro.id_libro not in self.libros:
            self.libros[libro.id_libro] = libro
        else:
            print ('[¡] No es posible agregar el libro con ID {}'.format(libro.id_libro))
            
    def prestar_libro(self, id_libro):
        if id_libro in self.libros and not self.libros[id_libro].prestado:
            self.libros[id_libro].prestado = True
        else:
            print (f'[¡] No es posible prestar el libro con ID {id_libro}')
            
            
            
    @property
    def mostrar_libros(self):
        return [str(libro )for libro in self.libros.values() if not libro.prestado]
        
    @property
    def mostrar_libros_prestados(self):
        return [str(libro for libro in self.libros.values() if libro.prestado )]
    
class BibliotecaInfantil(Biblioteca):
    def __init__(self):
        super().__init__()
        self.libros_para_ninos = {}
        
    def agregar_libro(self, libro):
        super().agregar_libro(libro)
        self.libros_para_ninos[libro.id_libro] = self.libros.para_ninos
        
    def prestar_libro(self, id_libro):
        if id_libro in self.libros and self.libros_para_niños and  not self.libros[id_libro].prestado:
            self.libros[id_libro].prestado = True
        else:
            print (f'[¡] No es posible prestar el libro con ID {id_libro}')
        
        
if __name__ == '__main__': 
        
    biblioteca = BibliotecaInfantil()
    
    libro1 = Libro(1, 'J.R.R Tolkien', 'El señor de los anillos')
    libro2 = Libro(2, 'Brandon Sanderson', 'Arcanum Ilimitado')
    biblioteca.agregar_libro(libro1, para_ninos = False)
    biblioteca.agregar_libro(libro2, para_ninos = True)
    
    print (f'[+] Libros en la biblioteca: {biblioteca.mostrar_libros}')
    print (f'[+] Libros prestados: {biblioteca.mostrar_libros_prestados}')
    
    
    biblioteca.prestar_libro(1, es_nino = False)
    
    


   