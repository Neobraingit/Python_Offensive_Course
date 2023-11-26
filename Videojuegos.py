#!/usr/bin/env python3

juegos = ['Super Mario Bros', 'Zelda', 'Ciberpunk', 'Final Fantasy VII']
tope = 500

# Géneros

generos = {
    'Super Mario Bros' : 'Aventura',
    'Zelda': 'Aventura',
    'Ciberpunk' : 'Rol',
    'Final Fantasy VII' : 'Rol'
}

# Venta y stock

ventas_stock = {
    'Super Mario Bros' : (400, 200),
    'Zelda' : (600, 20),
    'Ciberpunk' : (60, 120),
    'Final Fantasy VII' : (924, 3)
}
# Clientes

clientes = {
    'Super Mario Bros' : {'Marcos', 'David', 'Eva', 'Marta'},
    'Zelda' : {'Marcos', 'David'},
    'Ciberpunk' : { 'Marta'},
    'Final Fantasy VII' : {'Eva', 'Marcos'}
}

def sumario(juego):

# Sumario

    print ('[i] Resumen del juego {}\n'.format(juego))
    print ('\t[+] Género del juego: {}'.format(generos[juego]))
    print ('\t[+] Total de ventas para este juego {}'.format(ventas_stock[juego][0]))
    print ('\t[+] Total de stock para este juego {} unidades'.format(ventas_stock[juego][1]))
    print (f'\t[+] Clientes que han adquirido el juego: {", " .join(clientes[juego])}')



for i in juegos:
    if ventas_stock[i][0] > 500:
        sumario(i)
        
    
ventas_totales = lambda: sum(ventas for juego, (ventas, _ )in ventas_stock.items()if ventas_stock[juego][0] > tope)
print (f'\n[+] El total de ventas ha sido {ventas_totales()}')