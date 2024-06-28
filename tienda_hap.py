from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="test",  # Nombre de la base de datos
    password=""
)
mycursor = mydb.cursor()
# Configuración de la base de datos
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'database': 'test',  
    'password': ''       
}

# Variables globales
carrito = {}
total = 0

# Funciones

def conectar_db():
    try:
        return mysql.connector.connect(**DB_CONFIG)
    except mysql.connector.Error as err:
        messagebox.showerror("Error de conexión", f"No se pudo conectar a la base de datos: {err}")
        return None

def login():
    login_window = tk.Toplevel(root)
    login_window.title("Inicio de sesión")
    login_window.geometry("300x200")

    # Campos de entrada
    tk.Label(login_window, text="Usuario:").grid(row=0, column=0, padx=10, pady=10)
    usuario_entry = tk.Entry(login_window)
    usuario_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(login_window, text="Contraseña:").grid(row=1, column=0, padx=10, pady=10)
    contrasena_entry = tk.Entry(login_window, show="*")  # Ocultar la contraseña
    contrasena_entry.grid(row=1, column=1, padx=10, pady=10)
    
    def iniciar_sesion():
        usuario = usuario_entry.get()
        contrasena = contrasena_entry.get()

        if usuario == "tienda" and contrasena == "tiendahap":
            login_window.destroy()  # Cerrar la ventana de inicio de sesión
            ventana_inicio()  # Abrir la ventana de inicio
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    def iniciar_sesion_compra():
        usuario = usuario_entry.get()
        contrasena = contrasena_entry.get()

        if usuario == "tienda" and contrasena == "tiendahap":
            login_window.destroy()  # Cerrar la ventana de inicio de sesión
            ventana_compra()  # Abrir la ventana 
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    # Botones
    tk.Button(login_window, text="Iniciar sesión", command=iniciar_sesion).grid(row=2, column=0, columnspan=2, pady=10)
    tk.Button(login_window, text="Comprar", command=iniciar_sesion_compra).grid(row=3, column=0, columnspan=2, pady=10)

def ventana_inicio():
    mydb = conectar_db()
    if not mydb:
        return  # Si no hay conexión, no abrir la ventana

    mycursor = mydb.cursor()
    inicio_window = tk.Toplevel(root)
    inicio_window.title("Inventario")

    tk.Label(inicio_window, text="codigo:").grid(row=0, column=0, padx=20, pady=20)
    codigo_entry = tk.Entry(inicio_window)
    codigo_entry.grid(row=0, column=1, padx=25, pady=20)

    tk.Label(inicio_window, text="nombre:").grid(row=1, column=0, padx=20, pady=20)
    nombre_entry = tk.Entry(inicio_window)
    nombre_entry.grid(row=1, column=1, padx=25, pady=20)

    tk.Label(inicio_window, text="descripcion:").grid(row=2, column=0, padx=20, pady=20)
    descripcion_entry = tk.Entry(inicio_window)
    descripcion_entry.grid(row=2, column=1, padx=25, pady=20)

    tk.Label(inicio_window, text="Precio:").grid(row=3, column=0, padx=20, pady=20)
    precio_entry = tk.Entry(inicio_window)
    precio_entry.grid(row=3, column=1, padx=25, pady=20)

    def agregar_producto():
        codigo = codigo_entry.get()
        nombre = nombre_entry.get()
        descripcion = descripcion_entry.get()
        precio = precio_entry.get()

        # Validación de datos (mejorada)
        if not all([codigo, nombre, descripcion, precio]):
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        try:
            precio = float(precio)
        except ValueError:
            messagebox.showerror("Error", "El precio debe ser un número")
            return

        # Insertar en la base de datos (corregido)
        sql = "INSERT INTO inventario (codigo, nombre, descripcion, precio) VALUES (%s, %s, %s, %s)"
        val = (codigo, nombre, descripcion, precio)
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("Éxito", "Producto agregado correctamente")
        limpiar_campos()

    def buscar_producto():
        codigo_a_buscar = codigo_entry.get()
        if not codigo_a_buscar:
            messagebox.showerror("Error", "Ingresa el código del producto a buscar")
            return

        sql = "SELECT * FROM inventario WHERE codigo = %s"
        val = (codigo_a_buscar,)
        mycursor.execute(sql, val)
        producto = mycursor.fetchone()

        if producto:
            codigo_entry.delete(0, tk.END)
            codigo_entry.insert(0, producto[1])
            nombre_entry.delete(0, tk.END)
            nombre_entry.insert(0, producto[2])
            descripcion_entry.delete(0, tk.END)
            descripcion_entry.insert(0, producto[3])
            precio_entry.delete(0, tk.END)
            precio_entry.insert(0, str(producto[4]))
        else:
            messagebox.showerror("Error", "Producto no encontrado")

    def eliminar_producto():
        codigo_a_eliminar = codigo_entry.get()
        if not codigo_a_eliminar:
            messagebox.showerror("Error", "Ingresa el código del producto a eliminar")
            return

        confirmacion = messagebox.askyesno("Confirmar eliminación", f"¿Estás seguro de que deseas eliminar el producto con código '{codigo_a_eliminar}'?")
        if confirmacion:
            sql = "DELETE FROM inventario WHERE codigo = %s"
            val = (codigo_a_eliminar,)
            mycursor.execute(sql, val)
            mydb.commit()
            messagebox.showinfo("Éxito", "Producto eliminado correctamente")
            limpiar_campos()
            
    def limpiar_campos(codigo_entry,nombre_entry,precio_entry,descripcion_entry):
        codigo_entry.delete(0, tk.END)
        nombre_entry.delete(0, tk.END)
        precio_entry.delete(0, tk.END)
        descripcion_entry.delete(0, tk.END)

    def mostrar_inventario():
        inventario_window = tk.Toplevel(inicio_window)
        inventario_window.title("Lista de inventario")

        tree = ttk.Treeview(inventario_window, columns=("ID", "Código", "Nombre", "Descripción", "Precio"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Código", text="Código")
        tree.heading("Nombre", text="Nombre")
        tree.heading("Descripción", text="Descripción")
        tree.heading("Precio", text="Precio")
        tree.pack()

        mycursor.execute("SELECT * FROM inventario")
        for row in mycursor:
            tree.insert("", tk.END, values=row)

        tk.Button(inventario_window, text="Volver", command=inventario_window.destroy).pack()

    tk.Button(inicio_window, text="Agregar producto", command=agregar_producto).grid(row=4, column=0, columnspan=2, pady=10)  # Botón de agregar productos
    tk.Button(inicio_window, text="Buscar producto", command=buscar_producto).grid(row=5, column=0, columnspan=2, pady=5)  # Botón de buscar productos
    tk.Button(inicio_window, text="Eliminar producto", command=eliminar_producto).grid(row=6, column=0, columnspan=2, pady=5)  # Botón de eliminar productos
    tk.Button(inicio_window, text="Mostrar Inventario", command=mostrar_inventario).grid(row=7, column=0, columnspan=2, pady=5)  # Botón de mostrar inventario

def ventana_compra():
    mydb = conectar_db()
    if not mydb:
        return

    mycursor = mydb.cursor()
    compra_window = tk.Toplevel(root)
    compra_window.title("Selección de productos a comprar")
    compra_window.geometry("350x800")

    # Cargar productos desde la base de datos
    mycursor.execute("SELECT codigo, nombre, descripcion, precio FROM inventario")
    productos = mycursor.fetchall()

    # Frame para el carrito
    carrito_frame = tk.LabelFrame(compra_window, text="Lista de compras")
    carrito_frame.pack(pady=1, padx=10)

    # Variables globales de la ventana de compra
    carrito = {}
    total = 0

    def agregar_al_carrito(producto, nombre, descripcion, precio, cantidad):
        if cantidad <= 0:
            messagebox.showerror("Error", "La cantidad debe ser mayor a cero")
            return

        if producto in carrito:
            carrito[producto]["cantidad"] += cantidad
        else:
            carrito[producto] = {
                "nombre": nombre,
                "descripcion": descripcion,
                "precio": precio,
                "cantidad": cantidad
            }
        actualizar_carrito()
    
    def actualizar_carrito():
        # Limpiar la visualización anterior del carrito
        for widget in carrito_frame.winfo_children():
            widget.destroy()

        # Mostrar los productos en el carrito
        if carrito:
            tk.Label(carrito_frame, text="TIENDA_HAP:").pack()
            for producto, detalles in carrito.items():
                subtotal = detalles["precio"]
                tk.Label(carrito_frame, text=f"{producto} (nombre: {detalles['nombre']}) x {detalles['precio']} = Bs{subtotal:.2f}").pack()
        else:
            tk.Label(carrito_frame, text="vacío").pack()

    def finalizar_compra():
        if not carrito:
            messagebox.showinfo("Carrito vacío", "No tienes productos en el carrito")
            return

        resumen_window = tk.Toplevel(compra_window)
        resumen_window.title("Factura")
        resumen_window.geometry("300x300")

        total = 0
        for producto, detalles in carrito.items():
            subtotal = detalles["precio"] * detalles["cantidad"]
            total += subtotal
            tk.Label(resumen_window, text=f"{detalles['nombre']} (Código: {producto}) x {detalles['cantidad']} = Bs{subtotal:.2f}").pack()

        tk.Label(resumen_window, text=f"Total: Bs{total:.2f}").pack(pady=10)
        tk.Label(resumen_window, text="¡Gracias por comprar en Tienda_HAP!").pack()

        def cerrar_factura():
            resumen_window.destroy()
            compra_window.destroy()

        tk.Button(resumen_window, text="Cerrar", command=cerrar_factura).pack()

    # Creación de la interfaz de ventana_compra()
    for producto, nombre, descripcion, precio in productos:
        producto_frame = tk.Frame(compra_window)
        producto_frame.pack(pady=5)

        tk.Label(producto_frame, text=f"{nombre} - Bs{precio:.2f}").pack(side=tk.LEFT)

        cantidad_var = tk.IntVar(value=1)
        cantidad_entry = tk.Entry(producto_frame, textvariable=cantidad_var, width=5)
        cantidad_entry.pack(side=tk.LEFT)

        tk.Button(producto_frame, text="Agregar al carrito", command=lambda p=producto, n=nombre, d=descripcion, pr=precio: agregar_al_carrito(p, n, d, pr, cantidad_var.get())).pack(side=tk.LEFT)

    tk.Button(compra_window, text="Finalizar compra", command=finalizar_compra).pack()

# Ventana principal
root = tk.Tk()
root.title("TIENDA_HAP") 
root.geometry("300x150")

tk.Button(root, text="Iniciar", command=login).pack(pady=20)

root.mainloop()