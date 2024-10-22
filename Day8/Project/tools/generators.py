def generador_turnos(area):
    turno_perfumeria = 0
    turno_farmacia = 0
    turno_cosmeticos = 0
    while True:
        match area:
            case 'perfumeria':
                turno_perfumeria = turno_perfumeria + 1
                yield f"P - {turno_perfumeria}"
            case 'farmacia':
                turno_farmacia += 1
                yield f"F - {turno_farmacia}"
            case 'cosmeticos':
                turno_cosmeticos += 1
                yield f"C - {turno_cosmeticos}"
