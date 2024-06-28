# TIENDA HAP
> Tienda_hap. "tienda harina, arroz y pasta"


    Esta tienda contiene un archivos Python llamados tienda_hap.py. El programa trabaja con una base de datos MySQL para administrar el inventario de productos, las transacciones de clientes. El sistema está diseñado para gestionar operaciones básicas.


El programa esta desarrollado en Python utilizando la biblioteca tkinter para la interfaz gráfica y mysql.connector para la interacción con una base de datos MySQL.

## Características principales :

- **Gestión de Inventario:** Permite agregar, buscar, editar y eliminar productos del inventario.

- **Panel de Compra:**

    - Muestra la lista de productos disponibles con sus precios.
    
    - Permite agregar productos al carrito de compras con la cantidad deseada.
    
    - Calcula el total de la compra.
    
    - Genera una factura detallada al finalizar la compra.

- **Autenticación:** Requiere inicio de sesión con usuario y contraseña para accedera las funciones de gestión de inventario y compra.

## Requisitos:

- **Python:** Asegúrate de tener Python instalado en tu sistema.

- **MySQL:** Necesitas tener un servidor MySQL en funcionamiento y una base de datos llamada test (puedes cambiar el nombre en la configuración).

- **XAMPP (opcional):** Si no tienes un servidor MySQL configurado, puedes usar XAMPP, que incluye MySQL y facilita la instalación.

- **Biblioteca mysql.connector:** Instala esta biblioteca con el comando pip install mysql.connector.

## Configuración:
### Base de Datos:
Crea una base de datos MySQL llamada test (o modifica el nombre en DB_CONFIG).

### Tabla inventario:
Crea una tabla en la base de datos con la siguiente estructura:

    CREATE TABLE inventario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    codigo VARCHAR(255) UNIQUE NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10, 2) NOT NULL
    )

### Credenciales:

Reemplaza los valores de user (usuario) y password (contraseña) en
DB_CONFIG con tus credenciales de MySQL.

## Uso:

1. Guarda el código como un archivo .py (por ejemplo, tienda.py) y ejecútalo desde tu terminal con el comando python tienda.py.

2. Iniciar sesión:
    - En la ventana principal, haz clic en "Iniciar".
    - Ingresa el usuario "tienda" y la contraseña "tiendahap" para acceder.

3. Panel de Gestión de Inventario:

    - Utiliza los botones para agregar, buscar, editar o eliminar productos del inventario.
    - El botón "Mostrar Inventario" abre una ventana con la lista completa de productos.

4. Panel de Compra:
    
    - Selecciona los productos que deseas comprar e ingresa la cantidad.- Haz clic en "Agregar al carrito".
    - Cuando hayas terminado, haz clic en "Finalizar compra" para ver la factura y el mensaje de agradecimiento.
Nota
----
        El usuario y contraseña estandar es:
            usuario: tienda
            contraseña: tiendahap
