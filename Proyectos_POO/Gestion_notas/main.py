
#!/usr/bin/env python3
import os

def main():
    while True:
        print (f'\n----------------\nMENÚ\n----------------')
        print ('1. Agregar una nota')
        print ('2. Leer todas las notas')
        print ('3. Buscar por una nota')
        print ('4. Eliminar una nota')
        print ('5. Salir')
        
        opcion = input('\nEscoge una opción: ')
        if opcion == '1':
            contenido = input('\n[+] Contenido de la nota: ')
        elif opcion == '5':
            break
        else:
            print ('\n[!] La opción indicada es incorrecta\n')
            
        input (f'\n[+]Presiona <Enter> para continuar...')
        os.system ('cls' if os.name == 'nt' else 'clear')
        

if __name__ == '__main__':
    main()