# **Laboratorio del módulo 7: Introducción a IAM**
**OBJETIVO**: explorar los usuarios, grupos y políticas en el servicio AWS Identity and Access Management (IAM).
## **Tarea 1. Analizar los usuarios y grupos.**
1. Primero, anote la región en la que se encuentra en la esquina superior derecha de la página de la consola. Luego, elija el menú **Servicios**, busque los servicios de **Seguridad, identidad y conformidad**, y elija **IAM**. Finalmente, en el panel de navegación de la izquierda, elija **Usuarios**.

   Img 1

1. Seleccione el nombre del **user-1**.

   Img 2

1. Elija la pestaña **Grupos** en la pestaña **Credenciales de seguridad**.

   Img 3

1. Seleccione el panel de navegación de la izquierda, elija **Grupos de usuarios**.

   Img 4

1. Elija el nombre del grupo **EC2-Support** en la pestaña **permisos.**

   Img 5

1. Elija el enlace de la política **AmazonEC2ReadOnlyAccess** en la pestaña **Resumen** y **JSON.**

   Img 6 y 7

1. Realice los pasos 4, 5 y 6 para visualizar estás pestañas para conocer sus permisos de cada grupo.

   |**Usuario**|**En un grupo**|**Permisos**|
   | :-: | :-: | :-: |
   |user-1|S3-Support|Read-only access to Amazon S3 (Acceso de solo lectura a Amazon S3)|
   |user-2|EC2-Support|Read-only access to Amazon EC2 (Acceso de solo lectura a Amazon EC2)|
   |user-3|EC2-Admin|Ver, comenzar y detener las instancias de Amazon EC2|

## **Tarea 2. Agregar usuarios a los grupos.**
1. Ahora agregaremos el **user-1 al grupo S3-Support** y elija **Agregar usuarios.** Luego, seleccione **user-1.**

   Img 8 y 9 y 10

1. Ahora agregaremos el **user-2 al grupo EC2-Support** y elija **Agregar usuarios.** Luego, seleccione **user-2.**

   **Img 11 y 12**

1. Ahora agregaremos el **user-3 al grupo EC2-Admin** y elija **Agregar usuarios.** Luego, seleccione **user-3.**

   **Img 13 y 14**
## **Tarea 3. Iniciar sesión y probar los usuarios.**
1. ` `En una ventana privada o de incógnito en el navegador. Pegue el enlace de inicio de sesión en el navegador privado y presione INTRO.

   Img 15 y 16

1. Inicie sesión con las siguientes credenciales:
   - **Nombre de usuario de IAM:** user-1
   - **Contraseña:** Lab-Password1
1. ` `Elija el menú **Servicios** y, luego, **S3**.

   Img 17

1. Elija el menú **Servicios** y, luego, **EC2**. Al terminar cierre la sesión.

   Img 18

1. Inicie sesión con las siguientes credenciales:
   1. **Nombre de usuario de IAM:** user-2
   1. **Contraseña:** Lab-Password2
1. ` `Elija el menú **Servicios** y, luego, **EC2**. Elija **instancias** y verifique la región en la que inició el laboratorio. Seleccione el menú de **Estado de la instancia** y, a continuación, elija **Detener instancia**.

   Img 19

1. Elija el menú **Servicios** y, luego, **S3**. Cierre sesión.

   Img 20

1. Inicie sesión con las siguientes credenciales:
   1. **Nombre de usuario de IAM:** user-3
   1. **Contraseña:** Lab-Password3
1. ` `Elija el menú **Servicios** y, luego, **EC2**. Elija **instancias** y verifique la región en la que inició el laboratorio. Seleccione el menú de **Estado de la instancia** y, a continuación, elija **Detener instancia.**

Img 21 

En esta ocasión la acción tiene éxito porque el *user-3* tiene permisos para 	detener las instancias de EC2.

**¡Felicitaciones! Ha completado el laboratorio.**
