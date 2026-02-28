sistemaActivo= True
tienePermiso= False
if sistemaActivo:
    if tienePermiso:
        print("Acceso concedido")
    else:
        print("Acceso denegado: No tiene permiso")
else:
    print("Acceso denegado: Sistema inactivo")