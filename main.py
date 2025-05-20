import os
import platform
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modelos.base import Base
from modelos.paciente import Paciente
from modelos.servicio import Servicio
from modelos.documento_transaccion import DocumentoTransaccion
from modelos.linea_doc_transaccion import LineaDocTransaccion
from datetime import datetime

# Inicializar conexión a base de datos
engine = create_engine('sqlite:///hospital.db')
Session = sessionmaker(bind=engine)
session = Session()

# Limpiar la consola
def limpiar_consola():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# Precargar servicios base
def precargar_servicios():
    servicios_base = [
        ("Atención médica", 50.0),
        ("Exámenes de laboratorio", 30.0),
        ("Imágenes de rayos X", 80.0),
        ("Suministro de medicamentos", 20.0),
        ("Procedimientos médicos", 100.0)
    ]
    for desc, precio in servicios_base:
        existe = session.query(Servicio).filter_by(descripcion=desc, precio=precio).first()
        if not existe:
            nuevo = Servicio(descripcion=desc, precio=precio, origen='base')

            session.add(nuevo)
    session.commit()

def mostrar_pacientes():
    pacientes = session.query(Paciente).all()
    print("\nLista de Pacientes:")
    for p in pacientes:
        print(f"{p.id}. {p.nombre}")

def mostrar_servicios():
    servicios = session.query(Servicio).filter_by(origen='base').all()
    print("\nServicios Disponibles:")
    for s in servicios:
        print(f"{s.id}. {s.descripcion} - ${s.precio}")


def registrar_paciente():
    nombre = input("Ingrese el nombre del paciente: ")
    paciente = session.query(Paciente).filter_by(nombre=nombre).first()
    if paciente:
        print(f"El paciente ya existe con ID {paciente.id}")
    else:
        paciente = Paciente(nombre=nombre)
        session.add(paciente)
        session.commit()
        print(f"Paciente registrado con ID {paciente.id}")

def crear_descargo():
    mostrar_pacientes()
    paciente_id = int(input("Ingrese el ID del paciente: "))
    descargo_existente = session.query(DocumentoTransaccion).filter_by(paciente_id=paciente_id).first()
    if descargo_existente:
        print("El paciente ya tiene un descargo activo.")
    else:
        nro = f"D-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        descargo = DocumentoTransaccion(nro=nro, paciente_id=paciente_id)
        session.add(descargo)
        session.commit()
        print(f"Descargo creado con ID {descargo.id}")

def agregar_servicio_a_descargo():
    mostrar_pacientes()
    paciente_id = int(input("Ingrese el ID del paciente: "))
    descargo = session.query(DocumentoTransaccion).filter_by(paciente_id=paciente_id).first()
    if not descargo:
        print("No se encontró un descargo activo para este paciente.")
        return

    mostrar_servicios()
    servicio_id = int(input("Ingrese el ID del servicio a agregar: "))
    servicio = session.get(Servicio, servicio_id)
    if not servicio:
        print("Servicio no encontrado.")
        return

    linea = LineaDocTransaccion(documento_id=descargo.id, servicio_id=servicio.id)
    session.add(linea)
    session.commit()
    print(f"Servicio '{servicio.descripcion}' agregado al descargo.")

def registrar_servicio_personalizado_para_paciente():
    mostrar_pacientes()
    paciente_id = int(input("Ingrese el ID del paciente: "))
    descargo = session.query(DocumentoTransaccion).filter_by(paciente_id=paciente_id).first()
    if not descargo:
        print("Este paciente no tiene un descargo activo.")
        return

    descripcion = input("Describa el servicio o producto personalizado: ")
    precio = float(input("Ingrese el precio del servicio: "))
    servicio = Servicio(descripcion=descripcion, precio=precio, origen='personalizado')

    session.add(servicio)
    session.commit()

    linea = LineaDocTransaccion(documento_id=descargo.id, servicio_id=servicio.id)
    session.add(linea)
    session.commit()
    print(f"Servicio personalizado '{descripcion}' agregado al descargo del paciente.")

def generar_factura():
    mostrar_pacientes()
    paciente_id = int(input("Ingrese el ID del paciente a dar de alta: "))
    descargo = session.query(DocumentoTransaccion).filter_by(paciente_id=paciente_id).first()
    if not descargo:
        print("Este paciente no tiene descargo.")
        return

    lineas = descargo.lineas
    if not lineas:
        print("El descargo no tiene servicios registrados.")
        return

    print("\nFactura generada:")
    paciente = session.get(Paciente, paciente_id)
    print(f"Paciente: {paciente.nombre}")
    print("Servicios:")
    total = 0
    for linea in lineas:
        print(f" - {linea.servicio.descripcion} (${linea.servicio.precio})")
        total += linea.servicio.precio

    descargo.valor = total
    session.commit()

    print(f"Total a pagar: ${total:.2f}")
    session.delete(descargo)
    session.commit()
    print("El paciente fue dado de alta y el descargo se cerró.")

def menu():
    precargar_servicios()
    while True:
        limpiar_consola()
        print("==== SISTEMA HOSPITALARIO ====")
        print("1. Registrar paciente")
        print("2. Crear descargo")
        print("3. Agregar servicio al descargo")
        print("4. Registrar servicio personalizado para un paciente")
        print("5. Generar factura y alta del paciente")
        print("6. Ver pacientes")
        print("7. Ver servicios")
        print("8. Salir")
        opcion = input("Seleccione una opción: ")

        limpiar_consola()

        if opcion == "1":
            registrar_paciente()
        elif opcion == "2":
            crear_descargo()
        elif opcion == "3":
            agregar_servicio_a_descargo()
        elif opcion == "4":
            registrar_servicio_personalizado_para_paciente()
        elif opcion == "5":
            generar_factura()
        elif opcion == "6":
            mostrar_pacientes()
        elif opcion == "7":
            mostrar_servicios()
        elif opcion == "8":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida")

        input("\nPresione ENTER para continuar...")

if __name__ == '__main__':
    menu()
