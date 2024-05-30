# **Laboratorio del módulo 11: Uso de los balanceadores de carga**
**OBJETIVO**: crear y configurar un equilibrador de carga, registrar un sitio web como objetivo para el equilibrador de carga y probar el equilibrador de carga.
## **Tarea 1. Lanzar una instancia de EC2**
1. Creamos una instancia en el servicio EC2:

   Nómbrela, *Web Server 1*

   ![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_11/IMAGENES/Screenshot_1.png) 

1. Elegimos la AMI **Amazon Linux** con el valor predeterminado **Amazon Linux 2023 AMI x86\_64 (HVM)**

   ![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_11/IMAGENES/Screenshot_2.png)

1. Elegimos el tipo de instancia **t2.micro**

   ![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_11/IMAGENES/Screenshot_3.png)

1. Seleccionamos un par de claves, en este caso **vockey.**

   ![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_11/IMAGENES/Screenshot_4.png)

1. En la sección *Configuraciones de red*, seleccione **Editar**. Luego, realice lo siguiente:

   ![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_11/IMAGENES/Screenshot_5.png)

1. Elija **Agregar regla del grupo de seguridad** para configurar la nueva regla de la siguiente manera
- **Tipo:** HTTP
- **Tipo de origen**: Cualquier lugar

![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_11/IMAGENES/Screenshot_6.png)

1. En el panel **Detalles avanzados** en la sección **Datos de usuario** ingresar lo siguiente:

   ![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_11/IMAGENES/Screenshot_7.png)

1. En la parte final elegir lanzar **instancia** e inicialmente aparecerá en estado **Pendiente,** luego en **ejecución y Comprobación de estado** 2/2 comprobaciones aprobadas.

   ![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_11/IMAGENES/Screenshot_8.png) 

## **Tarea 2. Acceder al sitio web de la instancia de EC2**
1. En la pestaña **Detalles**, copie el valor de la **dirección IPv4 pública** de su instancia en el portapapeles. Luego, ábrala en una nueva pestaña.

   ![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_11/IMAGENES/Screenshot_9.png)
   ![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_11/IMAGENES/Screenshot_10.png)
## **Tarea 3. Configurar una segunda instancia de EC2 para el balanceo de carga**
1. Regrese a la **Tarea 3** para configurar una segunda instancia de EC2 para el **balanceo de carga.**
1. En el menú **Acciones**, seleccione **Imagen y plantillas**, luego, elija **Lanzar más como esta**.

   ![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_11/IMAGENES/Screenshot_11.png)
   ![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_11/IMAGENES/Screenshot_12.png)
   ![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_11/IMAGENES/Screenshot_13.png)

1. En el panel **Detalles avanzados** en la sección **Datos de usuario** ingresar lo siguiente:

   ![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_11/IMAGENES/Screenshot_14.png)

1. En la parte final elegir lanzar **instancia** e inicialmente aparecerá en estado **Pendiente,** luego en **ejecución y Comprobación de estado** 2/2 comprobaciones aprobadas.

   ![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_11/IMAGENES/Screenshot_15.png) 
## **Tarea 4. Acceder al sitio web en la segunda instancia de EC2**
1. En la pestaña **Detalles**, copie el valor de la **dirección IPv4 pública** de su instancia en el portapapeles. Luego, ábrala en una nueva pestaña.

   ![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_11/IMAGENES/Screenshot_16.png)
## **Tarea 5. Crear un equilibrador de carga**
1. Devuelta en la consola de EC2, en el panel de navegación izquierdo, en **Equilibrio de carga** elija **Balanceadores de carga**. Luego, seleccione **Crear balanceador de carga**.

   ![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_11/IMAGENES/Screenshot_17.png)

1. En **Balanceador de carga de aplicaciones**, seleccione **Crear**.

   ![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_11/IMAGENES/Screenshot_18.png)

1. Realice la siguiente configuración.

   ![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_11/IMAGENES/Screenshot_19.png)
   ![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_11/IMAGENES/Screenshot_20.png)
   ![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_11/IMAGENES/Screenshot_21.png)

1. En el panel *Agentes de escucha y direccionamiento*:
   1. Elija **Crear un grupo de destino**.

![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_11/IMAGENES/Screenshot_22.png)

1. En el panel *Basic* **Configuración básica**:
   1. Mantenga configurado el destino en **Instancias**.

En **Nombre del grupo de destino**, ingrese *myalbTG*.

![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_11/IMAGENES/Screenshot_23.png)

1. En el panel *Comprobaciones de estado*:
   1. Para la **Ruta de comprobación de estado**, ingrese index.html después de la barra diagonal ( / ). Luego, elija **Siguiente**.

La ruta debería verse de la siguiente manera: /index.html

![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_11/IMAGENES/Screenshot_24.png)

1. En la página **Registrar destinos**, en el panel **Instancias disponibles**, marque las casillas junto a las instancias que creó en este laboratorio. Luego, seleccione **Incluir como pendiente a continuación**.

   ![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_11/IMAGENES/Screenshot_25.png)

1. Elija **Crear un grupo de destino**. 

   ![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_11/IMAGENES/Screenshot_26.png)

1. Vuelva a la pestaña de la consola **Balanceadores de carga.**
1. En la sección **Agentes de escucha y direccionamiento**, en **Agente de escucha**, elija el ícono de actualizar. En la lista desplegable, elija el grupo de destino **myalbTG** que creó. Finalmente, elija **Crear balanceador de carga**.

   ![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_11/IMAGENES/Screenshot_27.png)

1. Antes de continuar, asegúrese de que el **Estado** del balanceador de carga que acaba de crear sea *Activo*.

   ![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_11/IMAGENES/Screenshot_28.png)
## **Tarea 6. Probar el balanceador de carga**
1. En **Detalles** del balanceador de carga creado, copie en el portapapeles el valor de **Nombre DNS**.

   ![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_11/IMAGENES/Screenshot_29.png)

1. Abra una nueva pestaña en su navegador web, pegue el nombre DNS que acaba de copiar y presione **Intro**.

   ![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_11/IMAGENES/Screenshot_30.png)

1. Actualice la pestaña del navegador varias veces y verá cómo cambia entre las instancias creadas.

   ![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_11/IMAGENES/Screenshot_31.png) 

**¡Felicitaciones! Ha completado el laboratorio.**

