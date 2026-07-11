#Programa para tienda de mascotas PetMarket

#Definimos nuestras funciones.

def leer_opcion():
    print(" ========== MENÚ PRINCIPAL ========== ")
    print("1. Unidades por categoría")
    print("2. Busqueda de productos por rando de precio")
    print("3. Actualizar precio del producto")
    print("4. Agregar producto")
    print("5. Eliminar producto")
    print("6. Salir")
    print("=====================================")

    try:
        opcion = int(input("Ingrese opción: "))
        if opcion >= 1 and opcion <= 6:
            return opcion
        else:
            print("Error: Debe seleccionar una opción válida (de ser un número entre 1 y 6)")
            return False
    except ValueError:
        print("Error: Debe ingresar un número entero.")
        return False
    

def unidades_categoria(categoria, dicc_productos, dicc_stock):
    categoria_buscar = categoria.strip().lower()
    total_disponible = 0
    encontrado = False
    
    for codigo, datos in dicc_productos.items(): 
        if datos[1].lower() == categoria_buscar:
            encontrado = True
            if codigo in dicc_stock:
                total_disponible += dicc_stock[codigo][1]
                
    if encontrado:
        print(f"El total de unidades disponibles es: {total_disponible}")
    else:
        print(f"No se encontraron productos para la categoría: {categoria}")

def busqueda_precio(p_min, p_max, dicc_stock, dicc_productos):
    resultados = []
    
    for codigo, datos_stock in dicc_stock.items():
        precio = datos_stock[0]
        unidades = datos_stock[1]
        
        if precio >= p_min and precio <= p_max and unidades > 0:
            if codigo in dicc_stock:
                nombre_producto = dicc_productos[codigo][0]
                resultados.append(f"{nombre_producto}--{codigo}")
                
    if resultados:
        resultados.sort()  
        print(f"Los productos encontrados son: {resultados}")
    else:
        print("No hay productos en ese rango de precios.")


def buscar_codigo(codigo, dicc_stock):
    if codigo in dicc_stock:
        return True
    else:
        return False



def actualizar_precio(codigo, nuevo_precio, dicc_stock):
    codigo_limpio = codigo.strip().upper()
    
    if buscar_codigo(codigo_limpio, dicc_stock):
        dicc_stock[codigo_limpio][0] = nuevo_precio
        return True
    else:
        return False


def agregar_producto(codigo, nombre, categoria, marca, peso_kg, es_importado, es_para_cachorro, precio, unidades, dicc_productos, dicc_stock):
    codigo_limpio = codigo.strip().upper()
    
    if buscar_codigo(codigo_limpio, dicc_stock):
        return False
    
    dicc_productos[codigo_limpio] = [nombre.strip(), categoria.strip(), marca.strip(), float(peso_kg), es_importado, es_para_cachorro]
    dicc_stock[codigo_limpio] = [int(precio), int(unidades)]
    return True



def validar_codigo(codigo, dicc_productos):
    codigo_limpio = codigo.strip().upper()
    if not codigo_limpio:
        return False
    elif codigo_limpio in dicc_productos:
        return False
    else:
        return True


def validar_nombre(nombre):
    if not nombre.strip():
        return False
    return True

def validar_categoria(categoria):
    if not categoria.strip():
        return False
    return True 

def validar_marca(marca):
    if not marca.strip():
        return False
    return True

def validar_peso(peso):
    try:
        peso = float(peso)
        if peso > 0:
            return True
        else:
            return False
    except ValueError:
        return False

def validar_importado(respuesta):
    respuesta = respuesta.strip().lower()
    if respuesta == 's' or respuesta == 'n':
        return True
    else:
        return False 

def validar_para_cachorro(respuesta):
    respuesta = respuesta.strip().lower()
    if respuesta == 's' or respuesta == 'n':
        return True
    else:
        return False



def validar_precio(precio_str):
    try:
        precio = int(precio_str)
        if precio > 0:
            return True
        else:
            return False
    except ValueError:
        return False

def validar_unidades(unidades):
    try:
        unidades = int(unidades)
        if unidades >= 0:
            return True
        else:
            return False
    except ValueError:
        return False


def eliminar_producto(codigo, dicc_productos, dicc_stock):
    codigo_limpio = codigo.strip().upper()
    
    if buscar_codigo(codigo_limpio, dicc_stock):
        dicc_productos.pop(codigo_limpio)
        dicc_stock.pop(codigo_limpio)
        return True
    return False


def main():

    productos = {
        'M001': ['Alimento Premium', 'comida', 'DogPlus', 10, True, False],
        'M002': ['Arena Aglomerante', 'higiene', 'CatClean', 8, False, False],
        'M003': ['Snack Dental', 'snack', 'BiteJoy', 1, True, True],
        'M004': ['Shampoo Suave', 'higiene', 'PetCare', 0.5, False, True],
        'M005': ['Correa Nylon', 'accesorio', 'WalkPro', 0.3, True, False],
        'M006': ['Cama Mediana', 'accesorio', 'CozyPet', 2, False, False]
        }

    stock = {
        'M001': [32990, 12],
        'M002': [9990, 0],
        'M003': [5490, 25],
        'M004': [7990, 5],
        'M005': [11990, 7],
        'M006': [24990, 3]
        }


    while True:
        opcion = leer_opcion()
        
        if opcion == 1:
            categoria_input = input("Ingrese categoría a consultar: ")
            unidades_categoria(categoria_input, dicc_productos=productos, dicc_stock=stock)
            
        elif opcion == 2:
            validador = True
            while validador:
                try:
                    precio_min = int(input("Ingrese precio mínimo: "))
                    precio_max = int(input("Ingrese precio máximo: "))
                    
                    if precio_min >= 0 and precio_max >= 0 and precio_min <= precio_max:
                        busqueda_precio(precio_min, precio_max, dicc_stock=stock, dicc_productos=productos)
                        validador = False
                        break
                    else:

                        print("Error: Rango de precios inconsistente (El mínimo debe ser menor o igual al máximo y ambos mayores o iguales a cero).")
                except ValueError:
                    print("Debe ingresar valores enteros")

                
        elif opcion == 3:
            while True:
                cod_input = input("Ingrese código del producto: ")
                nuevo_precio_input = input("Ingrese nuevo precio: ")
                
                if validar_precio(nuevo_precio_input):
                    nuevo_precio = int(nuevo_precio_input)
                    if actualizar_precio(cod_input, nuevo_precio, dicc_stock=stock):
                        print("Precio actualizado")
                    else:
                        print("El código no existe")
                else:
                    print("Error: El precio debe ser un número entero positivo.")
                    
                respuesta = input("¿Desea actualizar otro precio (s/n)?: ").strip().lower()
                if respuesta != 's':
                    break
                    
        elif opcion == 4:
            codigo_producto = input("Ingrese código del producto: ")
            if not validar_codigo(codigo_producto, dicc_productos=productos):
                print("Error: Código inválido o ya registrado.")
                continue
                
            nombre_producto = input("Ingrese nombre: ")
            if not validar_nombre(nombre_producto):
                print("Error: El nombre no puede estar vacío.")
                continue
                
            categoria_producto = input("Ingrese categoría: ")
            if not validar_categoria(categoria_producto):
                print("Error: La categoría no puede estar vacía.")
                continue
                
            marca_producto = input("Ingrese marca: ")
            if not validar_marca(marca_producto):
                print("Error: La marca no puede estar vacía.")
                continue
                
            peso_producto = input("Ingrese peso (kg): ")
            if not validar_peso(peso_producto):
                print("Error: El peso debe ser un número decimal mayor a cero.")
                continue
                
            importacion_producto = input("¿Es importado? (s/n): ")
            if not validar_importado(importacion_producto):
                print("Error: Debe responder con 's' o 'n'.")
                continue
            bool_importado = importacion_producto.strip().lower() == 's'
                
            apto_cachorro = input("¿Es para cachorro? (s/n): ")
            if not validar_para_cachorro(apto_cachorro):
                print("Error: Debe responder con 's' o 'n'.")
                continue
            bool_cachorro = apto_cachorro.strip().lower() == 's'


            precio_producto = input("Ingrese precio: ")
            if not validar_precio(precio_producto):
                print("Error: El precio debe ser un número entero mayor a cero.")
                continue
                
            unidades_producto = input("Ingrese unidades: ")
            if not validar_unidades(unidades_producto):
                print("Error: Las unidades deben ser un número entero mayor o igual a cero.")
                continue
            
            if agregar_producto(codigo_producto, nombre_producto, categoria_producto, marca_producto, peso_producto, bool_importado, bool_cachorro, precio_producto, unidades_producto, dicc_productos=productos, dicc_stock=stock):
                print("Producto agregado")
            else:
                print("Error: El código ingresado ya existe")
                
        elif opcion == 5:
            cod_eliminar = input("Ingrese el código del producto que desea eliminar: ")
            if eliminar_producto(cod_eliminar, dicc_productos=productos, dicc_stock=stock ):
                print("Producto eliminado")
            else:
                print("Error: El código ingresado no existe")
                
        elif opcion == 6:
            print("Programa finalizado.")
            break




main()


