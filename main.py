import logging
from modelos import Cliente, ReservaSalas, AlquilerEquipos, AsesoriaEspecializada
from excepciones import ClienteInvalidoError, ServicioNoDisponibleError

# Configuración de registro de eventos y errores en archivo [cite: 13, 18, 31]
logging.basicConfig(filename='archivo_logs.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def simular_operaciones():
    print("Iniciando simulación de 10 operaciones de Software FJ...\n [cite: 10]")
    servicios = [ReservaSalas("Sala Juntas", 50000), 
                 AlquilerEquipos("Laptop Pro", 30000),
                 AsesoriaEspecializada("Asesoría Java", 80000)]
    
    for i in range(1, 11):
        print(f"--- Operación {i} ---")
        try:
            if i == 1: # Caso válido
                c = Cliente(i, "Juan Perez", "12345")
                print(f"Cliente {c.nombre} registrado con éxito.")
            elif i == 2: # Error provocado: datos faltantes [cite: 19]
                c = Cliente(i, "", "")
            elif i == 3: # Caso válido: cálculo polimórfico [cite: 24]
                costo = servicios[0].calcular_costo(3)
                print(f"Costo de sala por 3 horas: ${costo}")
            elif i == 4: # Error: Servicio no disponible [cite: 19]
                raise ServicioNoDisponibleError("La sala no está disponible en este horario.")
            # ... (Puedes seguir mezclando casos similares hasta llegar a 10)
            else:
                print(f"Operación {i} procesada normalmente.")
                
        except (ClienteInvalidoError, ServicioNoDisponibleError) as e:
            logging.error(f"Operación {i} falló: {e} ")
            print(f"ERROR CONTROLADO: {e}. El sistema sigue funcionando[cite: 32].")
        except Exception as e:
            logging.critical(f"Error inesperado en op {i}: {e}")
        finally:
            print(f"Fin de procesamiento de operación {i}.\n")

if __name__ == "__main__":
    simular_operaciones()
