**Laboratorio 1 del Módulo 4: Lanzamiento de una instancia de EC2**

OBJETIVO:  En este laboratorio, creará una instancia de Amazon Elastic Compute Cloud (Amazon EC2) que aloja un sitio web sencillo.

**Tarea 1. Comenzar a crear la instancia y asignarle un nombre**

1. Seleccione **Lanzar instancia**

   ![Interfaz de usuario gráfica, Texto, Aplicación, Correo electrónico Descripción generada automáticamente](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_1_modulo_4/IMAGENES/Aspose.Words.408e875d-db55-496b-a0de-0cd412e6d6a1.001.png)

1. Nombre la instancia por Web Server 1

   ![Interfaz de usuario gráfica, Texto, Aplicación, Correo electrónico Descripción generada automáticamente](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_1_modulo_4/IMAGENES/Aspose.Words.408e875d-db55-496b-a0de-0cd412e6d6a1.002.png)

   **Nota**: *Nombre* solo es otra etiqueta. La *clave* para esta etiqueta es Name y el *valor* es Web Server 1.


**Tarea 2. Imágenes de aplicaciones y sistemas operativos**

1. Elegir la AMI **Amazon Linux y** mantener el valor predeterminado de la **Amazon Linux 2023 AMI x86\_64 (HVM)**

   ![Interfaz de usuario gráfica, Texto, Aplicación, Correo electrónico Descripción generada automáticamente](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_1_modulo_4/IMAGENES/Aspose.Words.408e875d-db55-496b-a0de-0cd412e6d6a1.003.png)

**Tarea 3. Elegir el tipo de instancia**

1. En el panel *Tipos de instancia* seleccionar el valor **t2.micro**.

   ![Interfaz de usuario gráfica, Texto, Aplicación Descripción generada automáticamente](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_1_modulo_4/IMAGENES/Aspose.Words.408e875d-db55-496b-a0de-0cd412e6d6a1.004.png)

**Tarea 4. Seleccionar un par de claves**

1. En el menú **Nombre de par de claves**, seleccione **vockey**.

   ![Interfaz de usuario gráfica, Texto, Aplicación, Correo electrónico Descripción generada automáticamente](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_1_modulo_4/IMAGENES/Aspose.Words.408e875d-db55-496b-a0de-0cd412e6d6a1.005.png)

**Tarea 5. Configuración de la red**

1. Mantenga la configuración predeterminada de *VPC* y *subred*. También mantenga la configuración de **Asignar automáticamente la IP pública** en **Habilitada**.

   ![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_1_modulo_4/IMAGENES/Aspose.Words.408e875d-db55-496b-a0de-0cd412e6d6a1.006.png)

1. En *Firewall* elija la opción **Crear grupo de seguridad**.
   1. **Nombre del grupo de seguridad por** Web Server.
   1. En **Descripción ingrese lo siguiente** Security group for my web server.
   1. Elija **Eliminar** para eliminar la regla de entrada SSH predeterminada

![Interfaz de usuario gráfica, Texto, Aplicación, Correo electrónico Descripción generada automáticamente](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_1_modulo_4/IMAGENES/Aspose.Words.408e875d-db55-496b-a0de-0cd412e6d6a1.007.png)

**Tarea 6. Configurar el almacenamiento**

1. En la sección *Configurar almacenamiento*, mantenga la configuración predeterminada.

   ![Interfaz de usuario gráfica, Texto, Aplicación, Correo electrónico
Descripción generada automáticamente](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_1_modulo_4/IMAGENES/Aspose.Words.408e875d-db55-496b-a0de-0cd412e6d6a1.008.png)

**Tarea 7: Detalles avanzados**

1. Expanda el panel Detalles avanzados y desplácese hasta el cuadro **Datos de usuario** e ingrese lo siguiente:

   #!/bin/bash

   yum update -y

   yum -y install httpd

   systemctl enable httpd

   systemctl start httpd

   echo '<html><h>Hello World!</h></html>' > /var/www/html/index.html

   ![Interfaz de usuario gráfica, Texto, Aplicación, Correo electrónico
Descripción generada automáticamente](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_1_modulo_4/IMAGENES/Aspose.Words.408e875d-db55-496b-a0de-0cd412e6d6a1.009.png)

**Tarea 8. Revisar la instancia y lanzarla**

1. ` `Elija **Lanzar instancia** y luego verá un mensaje de resultado correcto.

   ` `![Interfaz de usuario gráfica, Texto, Aplicación
Descripción generada automáticamente](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_1_modulo_4/IMAGENES/Aspose.Words.408e875d-db55-496b-a0de-0cd412e6d6a1.010.png)

1. Elija **Ver todas las instancias**.

   ![Interfaz de usuario gráfica, Aplicación
Descripción generada automáticamente](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_1_modulo_4/IMAGENES/Aspose.Words.408e875d-db55-496b-a0de-0cd412e6d6a1.011.png)

1. Seleccione la instancia **Web Server 1**(Servidor web 1) y revise la pestaña **Detalles** que aparece en el panel inferior.

Antes de continuar, espere a que su instancia muestre lo siguiente:

- **Estado de la instancia:** *En ejecución*
- **Comprobación de estado:** 2/2 comprobaciones aprobadas

![Interfaz de usuario gráfica, Texto, Aplicación, Word
Descripción generada automáticamente](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_1_modulo_4/IMAGENES/Aspose.Words.408e875d-db55-496b-a0de-0cd412e6d6a1.012.png)

Esperar a que se cumpla la segunda condición.

![Interfaz de usuario gráfica, Texto, Aplicación
Descripción generada automáticamente](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_1_modulo_4/IMAGENES/Aspose.Words.408e875d-db55-496b-a0de-0cd412e6d6a1.013.png)

**Tarea 9. Acceder a la instancia de EC2**

1. En la pestaña **Detalles**, copie el valor de la **dirección IPv4 pública y** abra una nueva pestaña en su navegador web, pegue la dirección IP pública que acaba de copiar y presione **Intro**.

   ![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_1_modulo_4/IMAGENES/Aspose.Words.408e875d-db55-496b-a0de-0cd412e6d6a1.014.png)

   El sitio web no se carga. Debe actualizar el grupo de seguridad para poder acceder a la página.

**Tarea 10. Actualizar el grupo de seguridad**

1. En el panel de navegación izquierdo, en **Network & Security**, elija **Security Groups**

   ![Interfaz de usuario gráfica, Texto, Aplicación, Correo electrónico
Descripción generada automáticamente](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_1_modulo_4/IMAGENES/Aspose.Words.408e875d-db55-496b-a0de-0cd412e6d6a1.015.png)

1. Seleccione el grupo de seguridad **Web Server** y en la parte inferior** seleccione la pestaña **Reglas de entrada**.

   ![Interfaz de usuario gráfica, Texto, Aplicación
Descripción generada automáticamente](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_1_modulo_4/IMAGENES/Aspose.Words.408e875d-db55-496b-a0de-0cd412e6d6a1.016.png)

**Tarea 11. Crear una regla de entrada**

1. Seleccione **Editar reglas de entrada** y, luego, elija **Agregar regla**. ![Interfaz de usuario gráfica, Texto, Aplicación, Chat o mensaje de texto
Descripción generada automáticamente](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_1_modulo_4/IMAGENES/Aspose.Words.408e875d-db55-496b-a0de-0cd412e6d6a1.017.png)
1. Configure lo siguiente:
- **Tipo:** HTTP
- **Origen:** Anywhere-IPv4
- Seleccione **Guardar reglas**.

La nueva regla de entrada HTTP crea una entrada para direcciones IPv4 (0.0.0.0/0) e IPv6 (: :/0).

![Interfaz de usuario gráfica, Aplicación, Word
Descripción generada automáticamente](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_1_modulo_4/IMAGENES/Aspose.Words.408e875d-db55-496b-a0de-0cd412e6d6a1.018.png)

**Tarea 12. Probar la regla**

1. La página debería mostrar el mensaje Hello World!

   ![Interfaz de usuario gráfica, Texto, Aplicación, Correo electrónico
Descripción generada automáticamente](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_1_modulo_4/IMAGENES/Aspose.Words.408e875d-db55-496b-a0de-0cd412e6d6a1.019.png)

   **¡Felicitaciones! Ha completado el laboratorio.**
