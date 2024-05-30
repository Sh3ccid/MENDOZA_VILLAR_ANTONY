# **Laboratorio del módulo 7: Introducción a IAM**
**OBJETIVO**: explorar los usuarios, grupos y políticas en el servicio AWS Identity and Access Management (IAM).
## **Tarea 1. Analizar los usuarios y grupos.**
1. Primero, anote la región en la que se encuentra en la esquina superior derecha de la página de la consola. Luego, elija el menú **Servicios**, busque los servicios de **Seguridad, identidad y conformidad**, y elija **IAM**. Finalmente, en el panel de navegación de la izquierda, elija **Usuarios**.

![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_7/IMAGENES/Screenshot_1.png)

1. Seleccione el nombre del **user-1**.

![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_7/IMAGENES/Screenshot_2.png)

1. Elija la pestaña **Grupos** en la pestaña **Credenciales de seguridad**.

![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_7/IMAGENES/Screenshot_3.png)

1. Seleccione el panel de navegación de la izquierda, elija **Grupos de usuarios**.

![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_7/IMAGENES/Screenshot_4.png)

1. Elija el nombre del grupo **EC2-Support** en la pestaña **permisos.**

![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_7/IMAGENES/Screenshot_5.png)

1. Elija el enlace de la política **AmazonEC2ReadOnlyAccess** en la pestaña **Resumen** y **JSON.**

![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_7/IMAGENES/Screenshot_6.png)
![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_7/IMAGENES/Screenshot_7.png)

1. Realice los pasos 4, 5 y 6 para visualizar estás pestañas para conocer sus permisos de cada grupo.

   |**Usuario**|**En un grupo**|**Permisos**|
   | :-: | :-: | :-: |
   |user-1|S3-Support|Read-only access to Amazon S3 (Acceso de solo lectura a Amazon S3)|
   |user-2|EC2-Support|Read-only access to Amazon EC2 (Acceso de solo lectura a Amazon EC2)|
   |user-3|EC2-Admin|Ver, comenzar y detener las instancias de Amazon EC2|

## **Tarea 2. Agregar usuarios a los grupos.**
1. Ahora agregaremos el **user-1 al grupo S3-Support** y elija **Agregar usuarios.** Luego, seleccione **user-1.**

![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_7/IMAGENES/Screenshot_8.png)
![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_7/IMAGENES/Screenshot_9.png)
![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_7/IMAGENES/Screenshot_10.png)

1. Ahora agregaremos el **user-2 al grupo EC2-Support** y elija **Agregar usuarios.** Luego, seleccione **user-2.**

![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_7/IMAGENES/Screenshot_11.png)
![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_7/IMAGENES/Screenshot_12.png)
1. Ahora agregaremos el **user-3 al grupo EC2-Admin** y elija **Agregar usuarios.** Luego, seleccione **user-3.**

![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_7/IMAGENES/Screenshot_13.png)
![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_7/IMAGENES/Screenshot_14.png)
## **Tarea 3. Iniciar sesión y probar los usuarios.**
1. ` `En una ventana privada o de incógnito en el navegador. Pegue el enlace de inicio de sesión en el navegador privado y presione INTRO.

![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_7/IMAGENES/Screenshot_15.png)
![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_7/IMAGENES/Screenshot_16.png)

1. Inicie sesión con las siguientes credenciales:
   - **Nombre de usuario de IAM:** user-1
   - **Contraseña:** Lab-Password1
1. ` `Elija el menú **Servicios** y, luego, **S3**.

![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_7/IMAGENES/Screenshot_17.png)

1. Elija el menú **Servicios** y, luego, **EC2**. Al terminar cierre la sesión.

![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_7/IMAGENES/Screenshot_18.png)

1. Inicie sesión con las siguientes credenciales:
   1. **Nombre de usuario de IAM:** user-2
   1. **Contraseña:** Lab-Password2
1. ` `Elija el menú **Servicios** y, luego, **EC2**. Elija **instancias** y verifique la región en la que inició el laboratorio. Seleccione el menú de **Estado de la instancia** y, a continuación, elija **Detener instancia**.

![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_7/IMAGENES/Screenshot_19.png)

1. Elija el menú **Servicios** y, luego, **S3**. Cierre sesión.

![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_7/IMAGENES/Screenshot_20.png)

1. Inicie sesión con las siguientes credenciales:
   1. **Nombre de usuario de IAM:** user-3
   1. **Contraseña:** Lab-Password3
1. ` `Elija el menú **Servicios** y, luego, **EC2**. Elija **instancias** y verifique la región en la que inició el laboratorio. Seleccione el menú de **Estado de la instancia** y, a continuación, elija **Detener instancia.**

![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_modulo_7/IMAGENES/Screenshot_21.png)

En esta ocasión la acción tiene éxito porque el *user-3* tiene permisos para 	detener las instancias de EC2.

**¡Felicitaciones! Ha completado el laboratorio.**
