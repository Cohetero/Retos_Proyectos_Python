from eventos.evento_dao import EventoDAO



eventos =  EventoDAO.seleccionar()
for evento in eventos:
    print(evento)