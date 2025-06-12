"""
🐍 Reto Semanal #2 - Sistema de Reservas de Citas
🎯 Objetivo:
Crear un programa que permita a los usuarios agendar, cancelar y consultar citas, simulando el sistema de una clínica o consultorio.

✅ Requisitos mínimos:
1. Usa mínimo 2 módulos:
    - main.py (interfaz de usuario)
    - agenda.py (donde estará la lógica con clases)

2. Usa al menos una clase (Cita o Agenda).
3. Guarda las citas en un archivo .txt o .json para persistencia de datos.
4. Cada cita debe tener:
    - Nombre del paciente
    - Fecha y hora
    - Motivo de la cita

💡 Opciones del programa:
    - 📅 Agendar una nueva cita
    - ❌ Cancelar una cita por nombre y fecha
    - 📖 Ver todas las citas agendadas
    - 💾 Las citas deben guardarse automáticamente

✍️ Ejemplo de uso:

Bienvenido al sistema de citas

1. Agendar cita
2. Cancelar cita
3. Ver citas
4. Salir

> 1
Nombre: Mauricio
Fecha (YYYY-MM-DD HH:MM): 2025-06-14 10:30
Motivo: Revisión general
✅ ¡Cita agendada!

> 3
📅 2025-06-14 10:30 - Mauricio: Revisión general
------------------------
⭐ Nivel extra (si te animas):
Verifica que no haya dos citas a la misma hora.

Ordena las citas por fecha.

Usa json en lugar de .txt.
"""