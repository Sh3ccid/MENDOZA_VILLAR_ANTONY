# **Laboratorio del módulo 9: Creación de una alarma de CloudWatch que inicie un mensaje de Amazon SNS**
**OBJETIVO**: crear una alarma de Amazon CloudWatch para que le notifique cuando la cuenta gaste una cantidad de dinero mayor a la determinada. La alarma envía un mensaje a Amazon Simple Notification Service (Amazon SNS) para enviar una notificación por correo electrónico o mensaje de texto.
## **Tarea 1. Crear y suscribirse a un tema de SNS**
1. Ingrese al servicio **Simple Notification Service. Luego, e**n el panel de navegación, seleccione **Temas**. Seleccione **Crear un tema**.

   Img 1

1. Luego realizar la siguiente configuración y al final elija **Crear un tema.**

   **img2**

1. Ahora, se suscribirá al tema creado para que, cuando se publique un mensaje en él, este llegue al teléfono o correo electrónico.  En la sección **Suscripciones**, elija **Crear una suscripción**.

   Img 3

1. Realizar la siguiente configuración y luego elija **Crear una suscripción.**

   **Img 4**
## **Tarea 2. Crear una alarma de CloudWatch**
1. Ingrese al servicio **CloudWatch**. Luego, en el panel de navegación izquierdo, seleccione **Alarmas**. Elija **Crear alarmas** y seleccione **Crear alarma**.

   Img 5

1. Elija **Seleccione una métrica**. Seleccione **Facturación,** luego Cargo total estimado y al final marque la casilla **EstimatedCharges.** Ahora elija **Seleccionar una métrica.**

   **img6**

1. En la sección **Condiciones**, configure la siguiente información y al finalizar elija **siguiente**.

   img7

1. En la sección **Notificación**, configure la siguiente información y al finalizar elija **siguiente**.

   Img 8

1. Ingrese el nombre de la alarma y luego elija **siguiente**.

   Img 9

1. ` `Revise todos los ajustes que se han realizado anteriormente y elija **Crear alarma.**

   **Img 10 y 11 y 12**

**¡Felicitaciones! Ha configurado una alarma de CloudWatch que utiliza Amazon SNS para enviar una alerta cuando el costo de los servicios alcance los 100 USD.**
