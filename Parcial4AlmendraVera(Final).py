
entradas={}
def nombre_comprador(nombre):
    return nombre not in entradas

def tipo_entrada (tipo):
    return tipo.upper() in ['G','V']

def cod_verificación (codigo):
    if len(codigo) < 6:
        return False
    if not any(c.isdigit() for c in codigo):
        return False
    if not any(c.isupper() for c in codigo):
        return False
    if " " in codigo:
        return False
    return True

def opcion_1 ():
    while True:
        nombre=input("\nIngrese un nombre de usuario: ")
        if nombre_comprador(nombre):
            break
        print("Nombre invalido o repetido, ingrese un nombre diferente")
          
    while True:
        tipo=input("\nIngrese el tipo de entrada (V:Vip / G:General): ")
        if tipo_entrada(tipo):
            tipo_nuevo="VIP" if tipo.upper()=="V" else "General"
            break
        print("Tipo de entrada invalido")
    
    while True:
        codigo=input("\nIngrese codigo de confirmación (Debe tener mínimo 6 caracteres, al menos una letra mayúscula, un número y sin espacios.): ")
        if cod_verificación(codigo):
            break
        print("Codigo de verificación invalido")

    entradas[nombre]={
        "Nombre":nombre,
        "Tipo": tipo_nuevo, 
        "Codigo": codigo
    }
    print("\n******Compra registrada exitosamente******\n")

def opcion_2():
    nombre=input("Ingrese el nombre del comprador a consltar: ")
    if nombre in entradas:
        datos=entradas[nombre]
        print(f"\nNombre: {datos['Nombre']}")
        print(f"\nTipo de entrada: {datos['Tipo']}")
        print(f"\nCodigo de confirmación: {datos['Codigo']}\n")
    else:
        print("El comprador no se encuentra")

def opcion_3():
    nombre=input("Ingrese el nombre del comprador a cancelar: ")
    if nombre in entradas:
        del entradas[nombre]
        print ("Compra cancelada")
    else:
        print("No se pudo cancelar la compra")


print("****Conejo simpatico****\n")
while True:
    print("***MENU PRINCIPAL****")
    print("1.- Comprar entrada")
    print("2.- Consultar comprador")
    print("3.- Cancelar compra")
    print("4.- Salir")
    try:
        opcion=int(input("\nSeleccione una opción: "))
    except ValueError:
        print("Opción invalida. Ingrese un número")
        continue

    if opcion==1:
        opcion_1()
    elif opcion==2:
        opcion_2()
    elif opcion==3:
        opcion_3()
    elif opcion==4:
        print("Programa terminado...")
        break
    else:
        print("Opción invalida, intente nuevamente")