#!/usr/bin/env python3

class Libro:
    def __init__(self, id_libro, autor, titulo):
        self.id_libro = id_libro
        self.autor = autor
        self.titulo = titulo
        self.prestado = False
        
    def __str__(self):
         return 'Libro {} {} {}'.format(self.id_libro, self.autor, self.titulo)
        


if __name__ == '__main__':
    
        libro1 = Libro(1, 'J.R.R Tolkien', 'El señor de los anillos')
        libro2 = Libro(2, 'Brandon Sanderson', 'Arcanum Ilimitado')
    
print (libro1)

    