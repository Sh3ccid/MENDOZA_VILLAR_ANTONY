# **Laboratorio del módulo 11: Uso de los balanceadores de carga**
**OBJETIVO**: crear y configurar un equilibrador de carga, registrar un sitio web como objetivo para el equilibrador de carga y probar el equilibrador de carga.
## **Tarea 1. Lanzar una instancia de EC2**
1. Creamos una instancia en el servicio EC2:

   Nómbrela, *Web Server 1*

   Img 1 

1. Elegimos la AMI **Amazon Linux** con el valor predeterminado **Amazon Linux 2023 AMI x86\_64 (HVM)**

   Img 2

1. Elegimos el tipo de instancia **t2.micro**

   Img 3

1. Seleccionamos un par de claves, en este caso **vockey.**

   Img 4

1. En la sección *Configuraciones de red*, seleccione **Editar**. Luego, realice lo siguiente:

   Img 5

1. Elija **Agregar regla del grupo de seguridad** para configurar la nueva regla de la siguiente manera
- **Tipo:** HTTP
- **Tipo de origen**: Cualquier lugar

Img 6

1. En el panel **Detalles avanzados** en la sección **Datos de usuario** ingresar lo siguiente:

   Img 7

1. En la parte final elegir lanzar **instancia** e inicialmente aparecerá en estado **Pendiente,** luego en **ejecución y Comprobación de estado** 2/2 comprobaciones aprobadas.

   Img 8 

## **Tarea 2. Acceder al sitio web de la instancia de EC2**
1. En la pestaña **Detalles**, copie el valor de la **dirección IPv4 pública** de su instancia en el portapapeles. Luego, ábrala en una nueva pestaña.

   Img 9 y 10
## **Tarea 3. Configurar una segunda instancia de EC2 para el balanceo de carga**
1. Regrese a la **Tarea 3** para configurar una segunda instancia de EC2 para el **balanceo de carga.**
1. En el menú **Acciones**, seleccione **Imagen y plantillas**, luego, elija **Lanzar más como esta**.

   Img 11, 12 y 13 

1. En el panel **Detalles avanzados** en la sección **Datos de usuario** ingresar lo siguiente:

   Img 14

1. En la parte final elegir lanzar **instancia** e inicialmente aparecerá en estado **Pendiente,** luego en **ejecución y Comprobación de estado** 2/2 comprobaciones aprobadas.

   Img 15 
## **Tarea 4. Acceder al sitio web en la segunda instancia de EC2**
1. En la pestaña **Detalles**, copie el valor de la **dirección IPv4 pública** de su instancia en el portapapeles. Luego, ábrala en una nueva pestaña.

   Img 16
## **Tarea 5. Crear un equilibrador de carga**
1. Devuelta en la consola de EC2, en el panel de navegación izquierdo, en **Equilibrio de carga** elija **Balanceadores de carga**. Luego, seleccione **Crear balanceador de carga**.

   Img 17

1. En **Balanceador de carga de aplicaciones**, seleccione **Crear**.

   Img 18

1. Realice la siguiente configuración.

   Img 19, 20 y 21

1. En el panel *Agentes de escucha y direccionamiento*:
   1. Elija **Crear un grupo de destino**.

Img 22

1. En el panel *Basic* **Configuración básica**:
   1. Mantenga configurado el destino en **Instancias**.

En **Nombre del grupo de destino**, ingrese *myalbTG*.

Img 23

1. En el panel *Comprobaciones de estado*:
   1. Para la **Ruta de comprobación de estado**, ingrese index.html después de la barra diagonal ( / ). Luego, elija **Siguiente**.

La ruta debería verse de la siguiente manera: /index.html

Img 24

1. En la página **Registrar destinos**, en el panel **Instancias disponibles**, marque las casillas junto a las instancias que creó en este laboratorio. Luego, seleccione **Incluir como pendiente a continuación**.

   Img 25

1. Elija **Crear un grupo de destino**. 

   Img 26

1. Vuelva a la pestaña de la consola **Balanceadores de carga.**
1. En la sección **Agentes de escucha y direccionamiento**, en **Agente de escucha**, elija el ícono de actualizar. En la lista desplegable, elija el grupo de destino **myalbTG** que creó. Finalmente, elija **Crear balanceador de carga**.

   Img 27

1. Antes de continuar, asegúrese de que el **Estado** del balanceador de carga que acaba de crear sea *Activo*.

   Img 28
## **Tarea 6. Probar el balanceador de carga**
1. En **Detalles** del balanceador de carga creado, copie en el portapapeles el valor de **Nombre DNS**.

   Img 29

1. Abra una nueva pestaña en su navegador web, pegue el nombre DNS que acaba de copiar y presione **Intro**.

   Img 30

1. Actualice la pestaña del navegador varias veces y verá cómo cambia entre las instancias creadas.

   Img 31 

**¡Felicitaciones! Ha completado el laboratorio.**

