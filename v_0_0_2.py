import re
import json

# Validación de email y teléfono
def validar_email(email):
    patron = r"[^@]+@[^@]+\.[^@]+"
    if re.match(patron, email):
        return True
    else:
        print("Formato de email inválido. Intente nuevamente.")
        return False

def validar_telefono(telefono):
    patron = r"^\d{9}$"  # Acepta solo números de 9 dígitos
    if re.match(patron, telefono):
        return True
    else:
        print("Formato de teléfono inválido. Debe contener solo 9 dígitos.")
        return False

# Guardar y cargar contactos desde archivo
def guardar_contactos(agenda, archivo="agenda_contactos.json"):
    with open(archivo, 'w') as f:
        json.dump(agenda, f)
    print("Contactos guardados exitosamente.")

def cargar_contactos(archivo="agenda_contactos.json"):
    try:
        with open(archivo, 'r') as f:
            agenda = json.load(f)
        print("Contactos cargados exitosamente.")
    except FileNotFoundError:
        print("Archivo de contactos no encontrado, creando uno nuevo.")
        agenda = {}
    return agenda

# Funciones principales del programa
def mostrar_menu():
    print("\nAgenda de contactos:")
    print("1. Agregar nuevo contacto")
    print("2. Eliminar contacto existente")
    print("3. Buscar contacto")
    print("4. Lista de contactos")
    print("5. Editar contacto")
    print("6. Guardar y salir")
    print("\n")

def agregar_contacto(agenda):
    nombre = input("Por favor introduzca el nombre completo del contacto: ")
    telefono = input("Por favor, introduzca el teléfono del contacto: ")
    email = input("Por favor introduzca el email del contacto: ")

    if validar_telefono(telefono) and validar_email(email):
        agenda[nombre] = {"telefono": telefono, "email": email}
        print(f"¡Se ha agregado el contacto {nombre} exitosamente!")

def eliminar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto que desea eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print(f"El contacto de {nombre} ha sido eliminado correctamente")
    else:
        print(f"No se ha encontrado un contacto con el nombre {nombre}")

def buscar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto que está buscando: ")
    if nombre in agenda:
        print(f"Nombre: {nombre}")
        print(f"Teléfono: {agenda[nombre]['telefono']}")
        print(f"Email: {agenda[nombre]['email']}")
    else:
        print(f"El contacto {nombre} no ha sido encontrado en la agenda")

def listar_contactos(agenda):
    if agenda:
        print("\nLista de contactos: ")
        for nombre, info in agenda.items():
            print(f"Nombre: {nombre}")
            print(f"Teléfono: {info['telefono']}")
            print(f"Email: {info['email']}")
            print("-" * 20)
    else:
        print("La agenda aún está vacía")

def editar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto que desea editar: ")
    if nombre in agenda:
        print(f"Editando contacto {nombre}:")
        nuevo_telefono = input(f"Nuevo teléfono (actual: {agenda[nombre]['telefono']}): ")
        nuevo_email = input(f"Nuevo email (actual: {agenda[nombre]['email']}): ")

        if nuevo_telefono and validar_telefono(nuevo_telefono):
            agenda[nombre]['telefono'] = nuevo_telefono
        if nuevo_email and validar_email(nuevo_email):
            agenda[nombre]['email'] = nuevo_email

        print(f"El contacto {nombre} ha sido actualizado exitosamente.")
    else:
        print(f"El contacto {nombre} no existe.")

# Bucle principal del programa
def agenda_contactos():
    agenda = cargar_contactos()  # Cargamos los contactos desde el archivo

    while True:
        mostrar_menu()
        opcion = input("Por favor elija una opción: ")
        print("\n")

        if opcion == "1":
            agregar_contacto(agenda)
        elif opcion == "2":
            eliminar_contacto(agenda)
        elif opcion == "3":
            buscar_contacto(agenda)
        elif opcion == "4":
            listar_contactos(agenda)
        elif opcion == "5":
            editar_contacto(agenda)
        elif opcion == "6":
            guardar_contactos(agenda)
            print("Saliendo de la agenda de contactos ¡Hasta luego!")
            break
        else:
            print("Por favor seleccione una opción válida (del 1 al 6)")

agenda_contactos()