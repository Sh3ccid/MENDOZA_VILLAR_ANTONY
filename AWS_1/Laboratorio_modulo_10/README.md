# **Laboratorio del módulo 10: Creación de una instancia de base de datos de Amazon RDS**
**OBJETIVO**: crear una instancia de base de datos (DB) de Amazon Relational Database Service (Amazon RDS) que mantenga los datos que utiliza una aplicación web.
## **Tarea 1. Configurar una instancia de base de datos RDS**
1. Ingrese al servicio **RDS** en el panel **Base de datos.** Luego elija **Crear base de datos,** en la sección elija **un método de creación de base de datos,** finalmente **creación fácil.**

   Img1

1. En la sección **Configuración**, configure lo siguiente y al final elija **Crear base de datos**.

   Img 2 y 3

1. En el panel de la parte superior de la página, seleccione **Ver detalles de credenciales**. Guarde está información en un block de notas.

   Img 4 y 5
## **Tarea 2. Descargue e instale SQL Server Management Studio**
1. Para conectarse a la instancia de la base de datos RDS, deberá descargar e instalar SQL Server Management Studio. <https://aka.ms/ssmsfullsetup>

   **Nota:** Si no puede instalar el nuevo software en su equipo local, siga [las instrucciones](https://aws-tc-largeobjects.s3.us-west-2.amazonaws.com/CUR-TF-100-ACCAIC-1-91563/07-lab-10-RDS/s3/readme_windows_ec2.html) para utilizar la instancia de Amazon Elastic Compute Cloud (Amazon EC2) que se lanzó en este entorno de laboratorio.
## **Tarea 3. Haga que la base de datos sea de acceso público**
1. Seleccione el nombre de la base de datos **SQL Server** que creó. Luego, elija en la sección **Conectividad y seguridad**, en **Seguridad**, observe que **Acceso público** se encuentra actualmente establecido en **No**.

   Img 6

   - Seleccione **Modificar** en la parte superior de la página. 
   - Baje hasta la sección **Conectividad** y expanda **Configuración adicional**.
   - En **Acceso público**, seleccione **Acceso público**.

Img 7

- Desplácese hasta el final de la página y elija **Continuar**.
- En la sección **Programación de las modificaciones**, en **Cuándo aplicar las modificaciones**, seleccione **Aplicar inmediatamente**. Al final seleccione **Modificar instancia de base de datos.**

Img 8

Después de unos 30 segundos, el **Estado** de la base de datos 		cambia a *En modificación*. Antes de continuar, espere hasta que el 	estado cambie a *Available* (Disponible).
## **Tarea 4. Actualizar el grupo de seguridad de la VPC**
1. En esta tarea, activará las conexiones entrantes de SQL Server desde la dirección IP.

Primero obtenga su dirección IP.

- En una nueva pestaña o ventana del navegador, vaya a <https://whatismyipaddress.com/>.
- Copie el valor **IPv4** en un editor de texto para utilizarlo luego en el laboratorio.

1. En la página **RDS>Base de dados**, elija el nombre que creó. En la sección **Conectividad y seguridad**, en **Grupos de seguridad de la VPC**, elija el nombre del grupo de seguridad.
   - En la página **Grupos de seguridad**, seleccione la pestaña **Reglas de entrada**.
   - Seleccione **Editar reglas de entrada** y elija **Agregar regla**.
   - En **Tipo**, seleccione **MSSQL**.
   - En **Origen**, elija **Personalizado** e ingrese la dirección IP o la dirección IP de la instancia de en el cuadro de texto. 
   - Agregue /32 al final de la dirección IP y seleccione **Guardar reglas**.

**Img 9**
## **Tarea 5. Conectarse a la instancia de la base de datos**
1. Regrese a la página **RDS>Base de dados**, elija el nombre que creó. En la sección **Conectividad y seguridad.** Luego, copie el valor del **Punto de enlace** en un editor de texto.

   Img 10

1. Observe el puerto, para SQL Server es 1433. Si el número de su puerto es diferente, copie ese valor en su editor de texto.
1. ` `Abra la aplicación Microsoft SQL Server Management Studio. Luego, Aparece el cuadro de diálogo **Conectar con el servidor**.

   Img 11

1. ` `Ahora configuraremos el login para conectar la base de datos con el servidor.
- Para el **Server type** (Tipo de servidor), seleccione **Database Engine** (Motor de base de datos).
- En **Server name** (Nombre del servidor), ingrese el valor del punto de enlace de la base de datos que copió.
- Al final del valor del punto de enlace, agregue una coma ( , ) y el número de puerto (el número de puerto predeterminado es **1433**).
- Por ejemplo, el nombre del servidor debe ser similar al siguiente: **database.abc2defghije.us-west-2.rds.amazonaws.com,1433**
- En **Authentication** (Autenticación), seleccione **SQL Server Authentication** (Autenticación de SQL Server).
- En **Inicio de sesión**, introduzca el nombre de usuario de su instancia de base de datos.
- Esto también se conoce como el nombre de usuario del administrador. El valor por defecto es **admin**.
- En **Password** (Contraseña), ingrese la contraseña que copió para la instancia de la base de datos.
- También se conoce como la contraseña del usuario administrador.
- Haga clic en **Connect** (Conectar).

Img 12
## **Tarea 6. Explorar la estructura de la base de datos relacional**
1. ¡Bien hecho! Puede explorar la estructura de la base de datos relacional mediante la expansión de las áreas en el panel del **Explorador de Objetos**.

Img 13

**¡Felicitaciones! Ha completado el laboratorio.**
