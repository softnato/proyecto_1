from datos.datos_asignaturas import obtener_listado_asignaturas,guardar_asignatura

def listado_asignaturas():
    #if asignaturas != None:
        #print(f'imprimiendo listado distinto de != none: {asignaturas}')
    print('listado de asignaturas')
    print('=======================')
    asignaturas = obtener_listado_asignaturas()
    if len(asignaturas)> 0 and asignaturas != '':
        contador = 0 
        for asignatura in asignaturas:
            contador += 1
            print(f'[{contador}] {asignatura}')
        print()
    else:
        print('no se han encontrado elementos')

def agregar_asignatura():
    listado_asignaturas()
    nueva_asignatura = input('ingrese el nmbre de su nueva asignatura: ')
    print()
    asignaturas = obtener_listado_asignaturas()
    if len(asignaturas) > 0:
        if nueva_asignatura != '':
            asignaturas.append(nueva_asignatura.title())
        dato_guardar = f'asignaturas = {asignaturas}'
        guardar_asignatura(dato_guardar)
    listado_asignaturas()

def modificar_asignatura():
    listado_asignaturas()
    indicar_asignatura = input('indique el numero de la asignatura) ')
    try:
        numero_asignatura = int(indicar_asignatura)
        asignaturas = obtener_listado_asignaturas()
        if len(asignaturas) > 0:
            asignatura_modificada = input(
                'ingrese el nuevo nombre de su asignatura: ')
            if asignatura_modificada != '':
                asignaturas[numero_asignatura - 1] = asignatura_modificada
        datos_guardar = f'asignaturas = {asignaturas}'
        guardar_asignatura(datos_guardar)
    except:
        print('valor NO corresponde')

def eliminar_asignatura():
    listado_asignaturas()
    indicar_asignatura = input('Indique el numro de la asignatura: ')
    try:
        numero_asignatura = int(indicar_asignatura)
        asignaturas = obtener_listado_asignaturas()
        if len(asignaturas) > 0:
            asignaturas.pop(numero_asignatura - 1)
        datos_guardar = f'asignaturas = {asignaturas}'
        guardar_asignatura(datos_guardar)
    except:
        print('valor NO corresponde')