# **Laboratorio del Módulo 6: Adjuntar un volumen de EBS**
**OBJETIVO:** se creará una instancia de Amazon Elastic Compute Cloud (Amazon EC2) y se le adjuntará un volumen de Amazon Elastic Block Store (Amazon EBS).
## **Tarea 1. Comenzar a crear la instancia y asignarle un nombre**
1. Creamos una instancia en el servicio EC2:
- Nómbrela, Web Server

Img 1
## **Tarea 2. Imágenes de aplicaciones y sistemas operativos**
1. Elegimos la AMI **Amazon Linux** con el valor predeterminado **Amazon Linux 2023 AMI x86\_64 (HVM)**

   Img 2
## **Tarea 3. Elegir el tipo de instancia**
1. Elegimos el tipo de instancia **t2.micro**

   Img 3
## **Tarea 4. Seleccionar un par de claves**
1. Seleccionamos un par de claves, en este caso **vockey.**

   **Img 4**
## **Tarea 4. Seleccionar un par de claves**
1. Editamos esta sección realizando lo siguiente:

   Img 5
## **Tarea 6. Configurar el almacenamiento**
1. Mantenemos la configuración predeterminada

   img 6
## **Tarea 7: Detalles avanzados**
1. En el panel **Detalles avanzados** en la sección **Datos de usuario** ingresar lo siguiente:

Img 7
## **Tarea 8. Revisar la instancia y lanzarla**
1. En la parte final elegir lanzar **instancia** e inicialmente aparecerá en estado **Pendiente,** luego en **ejecución y Comprobación de estado** 2/2 comprobaciones aprobadas**.** 

   Img 8
## **Tarea 9. Acceder a la instancia de EC2**
1. En la pestaña **Detalles**, copie el valor de la **dirección IPv4 pública** de su instancia en el portapapeles. Luego, ábrala en una nueva pestaña.

   Img 9 y 10
## **Tarea 10. Actualizar el grupo de seguridad**
1. ` `En el panel de navegación izquierdo, en **Network & Security** (Red y seguridad), elija **Security Groups** (Grupos de seguridad). Seleccione la instancia en cuestión y seleccione la pestaña **Reglas de entrada**.

   Img 11
## **Tarea 11. Crear una regla de entrada**
1. ` `Seleccione **Editar reglas de entrada** y, luego, elija **Agregar regla**. Luego, guarde las reglas.

   Img 12
## **Tarea 12. Probar la regla**
1. ` `Realizamos nuevamente la tarea nueve.

   Img 13
## **Tarea 13. Adjuntar un volumen de EBS a la instancia de EC2**
1. Seleccione la instancia en cuestión y en la pestaña **Redes** abajo, tome nota de la **Zona de disponibilidad** en la que se ejecuta la instancia. En el panel de navegación izquierdo, en **Elastic Block Store**, seleccione **Volúmenes**.

   Img 14

1. Ahora vamos a crear un volumen con la siguiente configuración y luego se crea el volumen.

   Img 15

1. Seleccione el nuevo volumen de 1 GiB de tamaño. A continuación, seleccione **Acciones** y **Asociar volumen**.

   Img 16

**¡Felicitaciones! Ha completado el laboratorio**
