**Laboratorio del módulo 5: Uso de CloudFront como CDN para un sitio web**

**OBJETIVO**: EN este laboratorio, utilizará Amazon CloudFront como red de entrega de contenido (CDN) para un sitio web que se almacena en Amazon Simple Storage Service (Amazon S3).

**Tarea 1: Crear un bucket de S3 mediante la utilización de AWS CLI**

1. Para crear un bucket desde el CLI de AWS, se debe hacer uso del servicio CloudShell

   Copie y pegue el siguiente código en un editor de texto:

   cd ~

   aws s3api create-bucket --bucket (bucket-name) --region us-east-1

   Sustituya **(Nombre del bucket)** por un nombre único compatible con el sistema de nombres de dominio (**DNS**) para el nuevo bucket.

1. Al ejecutarlo debe salir lo siguiente:

   ![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_m%C3%B3dulo_5/IMAGENES/Aspose.Words.568275f9-159d-46ea-90b3-8260b865ec9e.001.png)

   **Nota:** Cuando crea un bucket con este comando, el bucket estará abierto al público. 

**Tarea 2: Agregar una política de bucket**

1. Visualizamos de que se hay creado el bucket en S3.

   ![Interfaz de usuario gráfica, Texto, Aplicación
Descripción generada automáticamente](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_m%C3%B3dulo_5/IMAGENES/Aspose.Words.568275f9-159d-46ea-90b3-8260b865ec9e.002.png)

1. Seleccione la pestaña **Permisos**. En **Bloquear acceso público [configuración del bucket]**, seleccione **EDITAR**. Desactive la marca de verificación de **Bloquear todo el acceso público**. Seleccione **Guardar cambios**. Confirme los cambios.

   ![Interfaz de usuario gráfica, Texto, Aplicación
Descripción generada automáticamente](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_m%C3%B3dulo_5/IMAGENES/Aspose.Words.568275f9-159d-46ea-90b3-8260b865ec9e.003.png)

   ![Interfaz de usuario gráfica, Texto, Aplicación, Correo electrónico
Descripción generada automáticamente](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_m%C3%B3dulo_5/IMAGENES/Aspose.Words.568275f9-159d-46ea-90b3-8260b865ec9e.004.png)

1. En **Propiedad del objeto**, elija **Editar**. Seleccione **ACL habilitadas**. Compruebe la confirmación y seleccione **Guardar cambios**.

   ![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_m%C3%B3dulo_5/IMAGENES/Aspose.Words.568275f9-159d-46ea-90b3-8260b865ec9e.005.png)

8. En la sección **Política de bucket**, elija **Editar**, copie y pegue la siguiente política de bucket en el editor de políticas.

   ![Texto
Descripción generada automáticamente](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_m%C3%B3dulo_5/IMAGENES/Aspose.Words.568275f9-159d-46ea-90b3-8260b865ec9e.006.png)

   En la política, reemplace **example-bucket** por el nombre del bucket en cuestión.

![Interfaz de usuario gráfica, Texto, Aplicación
Descripción generada automáticamente](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_m%C3%B3dulo_5/IMAGENES/Aspose.Words.568275f9-159d-46ea-90b3-8260b865ec9e.007.png)

![Interfaz de usuario gráfica, Texto, Aplicación, Correo electrónico
Descripción generada automáticamente](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_m%C3%B3dulo_5/IMAGENES/Aspose.Words.568275f9-159d-46ea-90b3-8260b865ec9e.008.png)

**Tarea 3: Cargar un documento HTML**

1. A continuación, Seleccione: Guardar enlace como [index.html](https://aws-tc-largeobjects.s3.us-west-2.amazonaws.com/CUR-TF-100-ACCAIC-1-91563/02-lab-4.2-S3/s3/index.html)
1. En la consola, seleccione la pestaña **Objetos y** cargue el archivo index.html en el bucket.

   ![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_m%C3%B3dulo_5/IMAGENES/Aspose.Words.568275f9-159d-46ea-90b3-8260b865ec9e.009.png)

- Elija **Cargar** 
- Arrastre y suelte el archivo index.html en la página de carga.
- Como alternativa, seleccione **Agregar archivos**, vaya al archivo y seleccione **Abrir**.

![Interfaz de usuario gráfica, Texto, Aplicación
Descripción generada automáticamente](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_m%C3%B3dulo_5/IMAGENES/Aspose.Words.568275f9-159d-46ea-90b3-8260b865ec9e.010.png)

20. Expanda la sección **Propiedades** y seleccione **Conceder acceso público de lectura**. Debajo de la advertencia, marque la casilla de advertencia y en la parte inferior de la página, seleccione **Cargar**. Seleccione **Cerrar**.

    ![Interfaz de usuario gráfica, Texto, Aplicación
Descripción generada automáticamente](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_m%C3%B3dulo_5/IMAGENES/Aspose.Words.568275f9-159d-46ea-90b3-8260b865ec9e.011.png)

**Tarea 4: Probar el sitio web.**

1. Seleccione la pestaña **Propiedades** y baje hasta la sección **Alojamiento de sitios web estáticos.** Seleccione **Editar**. Seleccione **Habilitar**. En el cuadro de texto **Documento de índice**, ingrese index.html. Seleccione **Guardar Cambios.**

   ![Interfaz de usuario gráfica, Texto, Aplicación, Correo electrónico
Descripción generada automáticamente](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_m%C3%B3dulo_5/IMAGENES/Aspose.Words.568275f9-159d-46ea-90b3-8260b865ec9e.012.png)

1. Desplácese hacia abajo a la sección **Alojamiento de sitios web estáticos** y copie la **URL** del punto de enlace del sitio web del bucket en el portapapeles.

   ![Interfaz de usuario gráfica, Texto, Aplicación, Correo electrónico
Descripción generada automáticamente](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_m%C3%B3dulo_5/IMAGENES/Aspose.Words.568275f9-159d-46ea-90b3-8260b865ec9e.013.png)

1. Abra una nueva pestaña en su navegador web, pegue la **URL** que acaba de copiar y presione **Intro** y debería aparecer el sitio web **Hello World Take me to your leader**.

   ![Interfaz de usuario gráfica, Texto, Aplicación, Correo electrónico
Descripción generada automáticamente](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_m%C3%B3dulo_5/IMAGENES/Aspose.Words.568275f9-159d-46ea-90b3-8260b865ec9e.014.png)

**Tarea 5: Crear una distribución de CloudFront para servir el sitio web**

1. ora nos dirigimos al servicio CloudFront. Elija **Crear una distribución de CloudFront**.

   ![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_m%C3%B3dulo_5/IMAGENES/Aspose.Words.568275f9-159d-46ea-90b3-8260b865ec9e.015.png)

1. En **Origen**, elija el cuadro de texto junto a **Dominio de origen** y seleccione el punto de enlace de su bucket de S3.

   ![Interfaz de usuario gráfica, Texto, Aplicación
Descripción generada automáticamente](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_m%C3%B3dulo_5/IMAGENES/Aspose.Words.568275f9-159d-46ea-90b3-8260b865ec9e.016.png)

1. Para la **Política de protocolo del lector**, asegúrese de que **HTTP y HTTPS** estén seleccionados. En **Firewall para aplicaciones web [WAF],** seleccione **No habilitar protecciones de seguridad**.

   ![Interfaz de usuario gráfica, Texto, Aplicación, Correo electrónico
Descripción generada automáticamente](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_m%C3%B3dulo_5/IMAGENES/Aspose.Words.568275f9-159d-46ea-90b3-8260b865ec9e.017.png)

   ![Interfaz de usuario gráfica, Texto, Aplicación
Descripción generada automáticamente](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_m%C3%B3dulo_5/IMAGENES/Aspose.Words.568275f9-159d-46ea-90b3-8260b865ec9e.018.png)

1. Vaya a la parte inferior de la página y seleccione **Crear distribución**. Aparecerá una nueva distribución de CloudFront en la lista de distribuciones. El **Estado** dirá ***Implementando.*** Copie el valor del **Nombre de dominio** de su distribución y guárdelo en un editor de texto para utilizarlo más adelante.

   ![Interfaz de usuario gráfica, Texto, Aplicación
Descripción generada automáticamente](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_m%C3%B3dulo_5/IMAGENES/Aspose.Words.568275f9-159d-46ea-90b3-8260b865ec9e.019.png)

1. ` `Cree un nuevo archivo HTML para probar la distribución.
   1. Busque y descargue una imagen de Internet.
   1. Vaya al bucket de S3 y suba el archivo de imagen a él, asegúrese de conceder acceso público como hizo al subir el archivo HTML anteriormente en este laboratorio.
   1. Cree un nuevo archivo de texto con el Bloc de notas y copie el siguiente texto en él:

      <html>

          <head>My CloudFront Test</head>

          <body>

              <p>My test content goes here.</p>

              <p><img src="http://domain-name/object-name" alt="my test image">

          </body>

      </html>

   1. Sustituya **domain-name** por el nombre de dominio que copió anteriormente para su distribución de CloudFront.
   1. Sustituya **object-name** por el nombre del archivo de imagen que subió al bucket de S3.
   1. Guarde el archivo de texto con una extensión HTML.

![Interfaz de usuario gráfica, Texto, Aplicación, Correo electrónico
Descripción generada automáticamente](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_m%C3%B3dulo_5/IMAGENES/Aspose.Words.568275f9-159d-46ea-90b3-8260b865ec9e.020.png)

1. Utilice un navegador de Internet para abrir el archivo HTML que acaba de crear. Si se muestra la imagen que subió, la distribución de CloudFront fue correcta. Si no es así, repita el laboratorio.

   ![](https://github.com/Sh3ccid/MENDOZA_VILLAR_ANTONY/blob/main/AWS_1/Laboratorio_m%C3%B3dulo_5/IMAGENES/Aspose.Words.568275f9-159d-46ea-90b3-8260b865ec9e.021.png)

**¡Felicitaciones! Ha completado el laboratorio.**
