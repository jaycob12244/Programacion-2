import os

servidor_id = input("Ingrese el ID del Servidor: ")

# minimizando errores de entrada 
try:
    cpu = float(input("Ingrese la carga de CPU (%): "))
    temperatura = float(input("Ingrese la temperatura del Rack (°C): "))
    energia = float(input("Ingrese el consumo de energía (W): "))
except:
    print("Error: Debe ingresar valores numéricos en CPU, temperatura y energía.")
    exit()

os.system("cls")

print("===================================")
print("  GUARDIÁN DE INFRAESTRUCTURA v1.0 ")
print("===================================")
print("Servidor:", servidor_id)
print("Carga CPU:", cpu, "%")
print("Temperatura:", temperatura, "°C")
print("Consumo Energía:", energia, "W")
print("-----------------------------------")

# Control de Energía
if energia > 400:
    exceso = energia - 400
    print("EXCESO DE ENERGÍA:", exceso, "W por encima del límite.")
else:
    print("Consumo de energía dentro del rango permitido.")

# Alerta Crítica
if temperatura > 75 and cpu > 80:
    print("[PELIGRO CRÍTICO]: Apagado de emergencia inminente.")
elif temperatura > 75 or cpu > 80:
    print("[ADVERTENCIA]: Rendimiento comprometido.")
else:
    print("[ESTADO]: Operación normal.")

# Capacidad de Reserva
if cpu >= 90:
    procesos = (100 - cpu) / 2
    print("Puede recibir aproximadamente", int(procesos), "procesos adicionales antes de colapsar.")
else:
    print("El servidor aún tiene capacidad disponible suficiente.")

