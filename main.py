from version.version import entregar_version
from auxiliares.val_numero import valida_numero

# Proyecto : Control de inventario de un almacen
# Autor: Manuel Sánchez Cárcamo

def fn_mostrar_producto(nombre, precio, cantidad):
    """
    Funcion para mostrar los 3 datos de un producto

    Parámetros:
    -----------
        - nombre: nombre del producto -> str
        - precio: precio del producto -> float
        - cantidad: stock del prodcuto -> int
    """
    print(f"Nombre  : {nombre}")
    print(f"Precio  : {precio}")
    print(f"Cantidad: {cantidad}")
    #fn_mostrar_producto

def fn_buscar_producto(productos, nom):
    largo = len( productos )
    esta = False
    i = 0
    while i < largo and not esta:
        if ( nom.lower() == productos[i].lower()):
            esta = True
        else:
            i = i + 1
    if esta:
        return(i)
    else:
        return( -1 )

#Programa Principal
lnombre = ['Plumon', 'Borrador', 'Pizarra']
lprecio = [1850.0, 3500.0, 13500.0]
lstock = [20, 5, 10]
# lprecio = []
# lnombre = []
# lstock  = [] 
salir = False
while (not salir):
    print(f"**** MENU {entregar_version} ****")
    print("[1] Agregar Producto")
    print("[2] Listar Productos")
    print("[3] Buscar Producto")
    print("[4] Modificar Stock")
    print("[5] Eliminar Producto")
    print("[6] Salir")
    op = input("Opción: ")
    # AGREGAR PRODUCTO *************
    if (op == "1"):
        print("AGREGAR PRODUCTO")
        nom = input("Ingrese nombre  : ")
        pre = valida_numero("Ingrese Precio  : ")
        cant = valida_numero("Ingrese cantidad: ")
        lnombre.append( nom )
        lprecio.append( pre )    
        lstock.append( cant )    
        print(f"El producto {nom} se agregó correctamente.\n")
    # LISTAR PRODUCTO *************
    if (op == "2"):
        print("\nLISTAR PRODUCTOS\n")
        largo = len( lnombre )
        if largo == 0:
            print("No hay productos en el inventario\n")
        else:
            for i in range( largo ):
                fn_mostrar_producto(lnombre[i],lprecio[i],lstock[i] )
                print("____________________________________\n")
    # BUSCAR PRODUCTO *************
    if (op == "3"):
        print("\nBUSCAR PRODUCTOS\n")
        nom = input("Producto a buscar : ")
        pos = fn_buscar_producto(lnombre, nom)
        if pos != -1:
            fn_mostrar_producto(lnombre[pos],lprecio[pos],lstock[pos] )
        else:
            print(f"El producto {nom} no está en el inventario")
    # MODIFICAR PRODUCTO *************
    if (op == "4"):
        print("\nMODIFICAR PRODUCTO\n")
        nom = input("Producto a Modificar : ")
        pos = fn_buscar_producto(lnombre, nom)
        if pos != -1:  # si lo encontró
            fn_mostrar_producto(lnombre[pos],lprecio[pos],lstock[pos] )
            resp = input("Seguro desea modificar [si/no]: ")
            if (resp.lower() == "si"): #para evitar SI Si sI...etc
                cant = valida_numero("Nueva Cantidad: ")
                lstock[pos] = int(cant)
                print("La cantidad cambió.")
            else:
                print("La cantidad no cambió.")
        else:
            print(f"El producto {nom} no está en el inventario")
    # ELIMINAR PRODUCTO *************
    if (op == "5"):
        print("\nELIMINAR PRODUCTO\n")
        nom = input("Producto a Eliminar : ")
        largo = len( lnombre )
        esta = False
        i = 0
        while i < largo and not esta:
            if ( nom.lower() == lnombre[i].lower()):
                fn_mostrar_producto(lnombre[i],lprecio[i],lstock[i] )
                esta = True
                resp = input("Seguro desea Eliminar [si/no]: ")
                if (resp.lower() == "si"): #para evitar SI Si sI...etc
                    del lnombre[i] #eliminando de cada lista , la misma posicion
                    del lprecio[i] 
                    del lstock[i]
                    print(f"El producto {nom} ha sido eliminado")
                else:
                    print(f"El producto {nom} NO ha sido eliminado")
            i = i + 1
        if not esta:
            print(f"El producto {nom} no está en el inventario")
    if op == "6": 
        salir = True
        print("Hasta luego")
    