**Laboratorio 1 del Módulo 4: Lanzamiento de una instancia de EC2**

OBJETIVO: crear un bucket de Amazon Simple Storage Service (Amazon S3) para alojar un sitio web estático.

**Tarea 1. Crear un S3 Bucket**

1. Seleccione **Crear bucket** en la parte derecha de la página.

   ![](Aspose.Words.4725a7bf-f523-47a6-819f-14681c266091.001.png)

1. Introduzca un nombre único compatible con el sistema de nombres de dominio (DNS) para su nuevo bucket.

   ![Interfaz de usuario gráfica, Texto, Aplicación

Descripción generada automáticamente](Aspose.Words.4725a7bf-f523-47a6-819f-14681c266091.002.png)

1. En cuanto a la **Región**, elija la región de AWS en la que desea que resida el bucket.
1. Desmarque la casilla **Bloquear todo el acceso público** porque quiere poder probar si el sitio web funciona y marque la casilla de advertencia.

   ![Texto, Aplicación

Descripción generada automáticamente con confianza media](Aspose.Words.4725a7bf-f523-47a6-819f-14681c266091.003.png)

1. Vaya al final de la página y seleccione **Crear bucket**

   ![Interfaz de usuario gráfica, Texto, Aplicación, Correo electrónico

Descripción generada automáticamente](Aspose.Words.4725a7bf-f523-47a6-819f-14681c266091.004.png)

   Lo siguiente indica que se ha creado correctamente un bucket.

   ![Interfaz de usuario gráfica, Texto, Aplicación

Descripción generada automáticamente](Aspose.Words.4725a7bf-f523-47a6-819f-14681c266091.005.png)

**Tarea 2. Agregar una política de bucket para que el contenido esté disponible de manera pública**

1. Elija el enlace del nombre de su bucket y, a continuación, seleccione la pestaña Permisos.

   ![Interfaz de usuario gráfica, Texto, Aplicación, Correo electrónico

Descripción generada automáticamente](Aspose.Words.4725a7bf-f523-47a6-819f-14681c266091.006.png)

1. En la sección **Política del bucket**, elija **Editar**.

   Para conceder acceso de lectura público al sitio web, copie la siguiente política de bucket y péguela en el editor de políticas.

{

`    `"Version":"2012-10-17",

`    `"Statement":[

`        `{

`            `"Sid":"PublicReadGetObject",

`            `"Effect":"Allow",

`            `"Principal":"\*",

`            `"Action":[

`                `"s3:GetObject"

`            `],

`            `"Resource":[

`                `"arn:aws:s3:::example-bucket/\*"

`            `]

`        `}

}


En la política, reemplace **example-bucket** por el nombre del bucket en cuestión.

![](Aspose.Words.4725a7bf-f523-47a6-819f-14681c266091.007.png)

1. Elija **Guardar cambios**.

   ![](Aspose.Words.4725a7bf-f523-47a6-819f-14681c266091.008.png)

**Tarea 3. Cargar un documento HTML**

1. A continuación, Seleccione: Guardar enlace como <https://aws-tc-largeobjects.s3.us-west-2.amazonaws.com/CUR-TF-100-ACCAIC-1-91563/02-lab-4.2-S3/s3/index.html>
1. En la consola, seleccione la pestaña **Objetos y** cargue el archivo index.html en el bucket.

   ![Interfaz de usuario gráfica, Texto, Aplicación, Correo electrónico

Descripción generada automáticamente](Aspose.Words.4725a7bf-f523-47a6-819f-14681c266091.009.png)

- Elija **Cargar** 
- Arrastre y suelte el archivo index.html en la página de carga.
- Como alternativa, seleccione **Agregar archivos**, vaya al archivo y seleccione **Abrir**.

![Interfaz de usuario gráfica, Texto, Aplicación

Descripción generada automáticamente](Aspose.Words.4725a7bf-f523-47a6-819f-14681c266091.010.png)

1. Expanda la sección **Propiedades** y Asegúrese de que la clase de almacenamiento **Estándar** se encuentra seleccionada.

   ![Interfaz de usuario gráfica, Aplicación

Descripción generada automáticamente](Aspose.Words.4725a7bf-f523-47a6-819f-14681c266091.011.png)

1. En la parte inferior de la página, seleccione **cargar** y Elija **cerrar**. Para que luego le aparezca el archivo subido.

   ![Interfaz de usuario gráfica, Texto, Aplicación, Correo electrónico

Descripción generada automáticamente](Aspose.Words.4725a7bf-f523-47a6-819f-14681c266091.012.png)

**Tarea 4. Probar el sitio web**

1. Seleccione la pestaña **Propiedades** y baje hasta la sección **Alojamiento de sitios web estáticos**. Elija **Editar**.

   ![Interfaz de usuario gráfica, Texto, Aplicación, Correo electrónico

Descripción generada automáticamente](Aspose.Words.4725a7bf-f523-47a6-819f-14681c266091.013.png)

   ![Interfaz de usuario gráfica, Texto, Aplicación

Descripción generada automáticamente](Aspose.Words.4725a7bf-f523-47a6-819f-14681c266091.014.png)

1. ` `Selcione **Habilitar**, luego en el cuadro de texto **Documento de índice**, ingrese index.html y Seleccione **Guardar cambios**.

   ![Interfaz de usuario gráfica, Texto, Aplicación, Correo electrónico

Descripción generada automáticamente](Aspose.Words.4725a7bf-f523-47a6-819f-14681c266091.015.png)

1. Desplácese hacia abajo a la sección **Alojamiento de sitios web estáticos** y copie la **URL** del punto de enlace del sitio web del bucket en el portapapeles.

   ![](Aspose.Words.4725a7bf-f523-47a6-819f-14681c266091.016.png)

1. Abra una nueva pestaña en su navegador web, pegue la **URL** que acaba de copiar y presione **Intro** y debería aparecer el sitio web **Hello World Take me to your leader**.

   ![Interfaz de usuario gráfica, Texto, Aplicación

Descripción generada automáticamente](Aspose.Words.4725a7bf-f523-47a6-819f-14681c266091.017.png)

   **¡Felicitaciones! Ha completado el laboratorio.**
