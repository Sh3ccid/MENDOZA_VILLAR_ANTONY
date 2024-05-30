# **Module 14 Lab: AWS Pricing Calculator**
OBJETIVO: Utilizar la Calculadora de precios para elegir un servicio y, posteriormente, configurarlo. Creará una estimación que contabilice el uso de varios servicios de AWS. A medida que agregue y configure distintos servicios, el costo inicial, el costo mensual y se mostrará la estimación del costo total de 12 meses al final de la pantalla.
## **Pasos del laboratorio**
**Nota:** Para este laboratorio, no es necesario elegir **Start Lab** (Comenzar Laboratorio) en el entorno del laboratorio. Puede utilizar la Calculadora de precios de AWS sin acceder a la Consola de administración de AWS.

1. Diríjase a la [Calculadora de precios](https://calculator.aws/) y seleccione **Crear una estimación.**
1. Para crear la estimación de costos de Amazon EC2, configure las siguientes opciones:
   - Mantenga seleccionada la opción **Buscar por tipo de ubicación**.
   - Para **elegir un tipo de ubicación**. seleccione **Región**.
   - Para **Seleccionar una región**, elija **(EE. UU. Oeste [Oregón])**. 
   - En **Buscar servicio**, ingrese *ec2* y, a continuación, en la lista de resultados filtrados, en el cuadro **Amazon EC2**, elija **Configurar**.

Img 1

1. En la ventana **Configure Amazon EC2** (Configurar Amazon EC2), configure los siguientes detalles:
   1. En **Description** (Descripción), ingrese on-demand EC2 instance.
   1. En **Operating system** (Sistema operativo), seleccione **Linux**.
   1. En **Number of instances** (Número de instancias), escriba 1.

Img 2

1. En **Search instance type** (Buscar tipo de instancia), ingrese t2.medium, y en la lista de resultados filtrados, seleccione este tipo de instancia.

Img 3

1. En la sección **Payment options** (Opciones de pago), seleccione **On-Demand** (Bajo demanda) y luego configure las siguientes opciones:
   1. Para **Uso**, ingrese 8.
   1. En **Usage type** (Tipo de uso), elija **Hours / Day** (Horas/Día).
   1. Elija **Save and add service** (Guardar y agregar servicio).

img 4

1. Para crear la estimación de costos de Amazon S3, en el área de búsqueda **Find Service** (Buscar servicio), escriba S3, luego, en la lista de resultados filtrados, en el cuadro **Amazon Simple Storage Service (S3)**, elija **Configure** (Configurar).

   Img 5

1. En la ventana **Configure Amazon Simple Storage Service (S3)** (Configurar Amazon Simple Storage Service [S3]), configure los siguientes detalles:
   1. En **Description** (Descripción), ingrese data storage.
   1. En **Select S3 Storage classes and other features** (Seleccionar clases de almacenamiento de S3 y otras funciones), mantenga seleccionadas las opciones **S3 Standard** y **Data Transfer** (Transferencia de datos).

Img 6

1. En **S3 Standard storage** (Almacenamiento S3 Standard), ingrese 60, y en **Unit** (Unidad), elija **GB per month** (GB al mes).
1. En **How will data be moved into S3 Standard?** (¿Cómo se moverán los datos a S3 Standard?) mantenga seleccionada la opción **The specified amount of data is already stored in S3 Standard** (La cantidad especificada de datos ya está almacenada en S3 Standard).
1. En **GET, SELECT, and all other requests from S3 Standard** (Solicitudes GET SELECT y todas las demás desde S3 Standard), ingrese 100.

Img 7

1. En la sección **Data Transfer** (Transferencia de datos), para **Outbound Data Transfer** (Transferencia de datos de salida), configure las siguientes opciones:
   1. En **Data transfer to** (Transferencia de datos a), seleccione **Internet**. 
   1. En **Enter Amount** (Introducir importe), ingrese 3.
   1. En **Data amount** (Cantidad de datos), elija **GB per month** (GB al mes).
1. Elija **Save and add service** (Guardar y agregar servicio).

Img 8

1. Dirijase al final de la página y Elija **View summary.**

   Img 9 y 10

1. Para agregar el costo del plan Basic Support a la estimación, elija **Add support** (Agregar soporte).
1. En la página **Support estimate** (Estimación de soporte), configure las siguientes opciones:
   1. En **Description** (Descripción), ingrese basic support.
   1. Mantenga las demás opciones predeterminadas, incluido **Basic support plan** (plan Basic Support).
   1. Seleccione **Add to my estimate** (Agregar a mi estimación).

Img 11

1. Img 12
1. En la pestaña superior de página seleccione **Export**, elija el formato **PDF**.

   Img 13

La **Calculadora** de precios ofrece un conjunto de funciones que se pueden usar para crear una estimación del costo de los servicios de AWS cuando sabe qué servicios usará y cómo piensa usarlos. Se adjunta el reporte anterior.

Img 14
