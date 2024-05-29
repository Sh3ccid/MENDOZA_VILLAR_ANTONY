# **Laboratorio del Módulo 6: Adjuntar un volumen de EBS**
**OBJETIVO:** se creará una instancia de Amazon Elastic Compute Cloud (Amazon EC2) y se le adjuntará un volumen de Amazon Elastic Block Store (Amazon EBS).
## **Tarea 1. Comenzar a crear la instancia y asignarle un nombre**
1. Creamos una instancia en el servicio EC2:
- Nómbrela, Web Server

![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_6/IMAGENES/Screenshot_1.png)
## **Tarea 2. Imágenes de aplicaciones y sistemas operativos**
1. Elegimos la AMI **Amazon Linux** con el valor predeterminado **Amazon Linux 2023 AMI x86\_64 (HVM)**

![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_6/IMAGENES/Screenshot_2.png)
## **Tarea 3. Elegir el tipo de instancia**
1. Elegimos el tipo de instancia **t2.micro**

![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_6/IMAGENES/Screenshot_3.png)
## **Tarea 4. Seleccionar un par de claves**
1. Seleccionamos un par de claves, en este caso **vockey.**

![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_6/IMAGENES/Screenshot_4.png)
## **Tarea 4. Seleccionar un par de claves**
1. Editamos esta sección realizando lo siguiente:

![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_6/IMAGENES/Screenshot_5.png)
## **Tarea 6. Configurar el almacenamiento**
1. Mantenemos la configuración predeterminada

![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_6/IMAGENES/Screenshot_6.png)
## **Tarea 7: Detalles avanzados**
1. En el panel **Detalles avanzados** en la sección **Datos de usuario** ingresar lo siguiente:

![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_6/IMAGENES/Screenshot_7.png)
## **Tarea 8. Revisar la instancia y lanzarla**
1. En la parte final elegir lanzar **instancia** e inicialmente aparecerá en estado **Pendiente,** luego en **ejecución y Comprobación de estado** 2/2 comprobaciones aprobadas**.** 

![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_6/IMAGENES/Screenshot_8.png)
## **Tarea 9. Acceder a la instancia de EC2**
1. En la pestaña **Detalles**, copie el valor de la **dirección IPv4 pública** de su instancia en el portapapeles. Luego, ábrala en una nueva pestaña.

![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_6/IMAGENES/Screenshot_9.png)
![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_6/IMAGENES/Screenshot_10.png)
## **Tarea 10. Actualizar el grupo de seguridad**
1. ` `En el panel de navegación izquierdo, en **Network & Security** (Red y seguridad), elija **Security Groups** (Grupos de seguridad). Seleccione la instancia en cuestión y seleccione la pestaña **Reglas de entrada**.

![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_6/IMAGENES/Screenshot_11.png)
## **Tarea 11. Crear una regla de entrada**
1. ` `Seleccione **Editar reglas de entrada** y, luego, elija **Agregar regla**. Luego, guarde las reglas.

![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_6/IMAGENES/Screenshot_12.png)
## **Tarea 12. Probar la regla**
1. ` `Realizamos nuevamente la tarea nueve.

![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_6/IMAGENES/Screenshot_13.png)
## **Tarea 13. Adjuntar un volumen de EBS a la instancia de EC2**
1. Seleccione la instancia en cuestión y en la pestaña **Redes** abajo, tome nota de la **Zona de disponibilidad** en la que se ejecuta la instancia. En el panel de navegación izquierdo, en **Elastic Block Store**, seleccione **Volúmenes**.

![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_6/IMAGENES/Screenshot_14.png)

1. Ahora vamos a crear un volumen con la siguiente configuración y luego se crea el volumen.

![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_6/IMAGENES/Screenshot_15.png)

1. Seleccione el nuevo volumen de 1 GiB de tamaño. A continuación, seleccione **Acciones** y **Asociar volumen**.

![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_6/IMAGENES/Screenshot_16.png)

**¡Felicitaciones! Ha completado el laboratorio**
