# **Laboratorio del módulo 12: Uso de Elastic Beanstalk y CloudFormation**
**OBJETIVO**: crear una aplicación con AWS Elastic Beanstalk. También utilizará una plantilla y AWS CloudFormation para crear una Virtual Private Cloud (VPC).
## **Tarea 1. Implementar una aplicación con Elastic Beanstalk**
1. Ingrese al servicio **Elastic Beanstalk**. Luego, elija **Crear aplicación.** Para el **Nombre de aplicación**, ingrese un nombre para su aplicación; por ejemplo, *MyLabApp*

   Img 1

1. En **Plataforma**, seleccione **PHP**. Para el **Código de la aplicación**, seleccione **Aplicación de ejemplo** y elija **Siguiente**.

   Img 2

1. Realice la siguiente configuración y luego elija **Siguiente**.

   Img 3

1. En **VPC**, seleccione la VPC disponible. En **Dirección IP pública**, seleccione **Activado**. En **Subredes de instancia**, seleccione dos como mínimo. Elija **Siguiente**.

   Img 4

1. En **Grupos de seguridad de EC2**, seleccione **default** (predeterminado).
   1. Elija **Siguiente**.

Img 5

1. En **Informes de estado**, elija **Básico**.
   1. En **Actualizaciones administradas**, anule la selección de **Activado**.
   1. Elija **Siguiente**.
   1. Seleccione **Enviar**.

Img 6

1. Observe la consola mientras Elastic Beanstalk crea y ejecuta los recursos necesarios para ejecutar la aplicación. El proceso tarda entre 5 y 10 minutos en completarse.

   Img 7

1. Cuando se completa, la pantalla cambia para mostrar el entorno recién creado. Está listo para que cargue una aplicación PHP.
   1. Abra una nueva pestaña o ventana del navegador. Vaya a la [página web de Tutoriales y muestras de AWS](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/tutorials.html).
   1. En la página, en la segunda lista de descargas, busque **PHP - php.zip**. Descargue la aplicación **PHP** de ejemplo en su equipo.
   1. Ahora debería tener un archivo llamado *php.zip*.
1. Vuelva a la pestaña de la consola de **Elastic Beanstalk.**
   1. Seleccione **Cargar e implementar**.
   1. Elija **Elegir archivo,** vaya y seleccione el archivo *php.zip* que descargó y elija **Abrir**.
   1. Elija **Implementar**.

Img 8

1. Para ver su sitio web PHP, en **Environment overview** (Información general sobre el entorno), elija **Domain** (Dominio).

   Img 9 y 10
## **Tarea 2. Implementar una aplicación mediante CloudFormation**
1. Ingrese al servicio EC2, **Red y seguridad**, seleccione **Pares de claves**.

   Img 11

   1. Elija **Crear par de claves**.
   1. En **Nombre**, ingrese CFLearner
   1. Elija **Crear par de claves**.
   1. Cuando se abra la ventana de descarga, seleccione **Cancelar**. No es necesario descargar el archivo.

Img 12

1. Ingrese el servicio **CloudFormation.** Seleccione **Crear pila.**

   Img 13

1. Seleccione **Con nuevos recursos (estándar)**.
   1. En la sección **Prerequisite** (Requisitos previos), seleccione **Use a sample template** (Utilizar una plantilla de muestra).
   1. En la sección **Select a sample template** (Seleccione una plantilla de muestra), seleccione **WordPress blog** (Blog de WordPress). Finalmente seleccione **Siguiente**.

Img 14

1. En **Stack name** (Nombre de la pila), ingrese: *WordPressStack*

img 15

1. En la sección **Parameters**(Parámetros), configure lo siguiente:
1. **DBPassword:** Ingrese Testing1
1. **DBUser:** Ingrese testadmin
1. **KeyName:** Elija el par de claves **CFLearner**

Img 16

1. Elija **Siguiente** y, a continuación, vuelva a elegir **Siguiente**.
   1. Revise la configuración de la pila y, a continuación, seleccione **Enviar**.

Img 17

**¡Felicitaciones! Ha completado el laboratorio.**

