# Tarea-1-Lab-C-de-D

Repositorio destinado a la Tarea 1 del Laboratorio de Ciencias de Datos. Este es el [enunciado](./tarea1.pdf).

Para editar el informe, hacer click [aquí](https://www.overleaf.com/6431364931fbzjxsjtfymh). Se puede observar el informe [aquí](./Tarea_1_Lab_C_de_D.pdf).

## Forma de trabajar:

* Para agregar contenido al informe, dirigirse a la carpeta `_preguntas`.
* Cuando se trabaje, hacer distintas ramas con nombres significativo, dependiendo de la pregunta. Recordar que la rama `master` debe estar "limpia".
* Para ver los símbolos actuales, y para agregar un nuevo símbolo, dirigirse a `simbolos.tex`
* Para agregar una nueva imagen, agregarla a `img` (categorizar por carpetas, eg: si se agrega un gráfico, hacer una carpeta `graf` o `graficos`).
* Cuando trabajemos con código, crear una nueva carpeta para éste (por favor, seguir el formato usual de escribir las carpetas sin mayúsculas y sin espacios, de otra forma, no se puede ocupar en la ventana de comando).
 
## TODO's

Esta será la lista de quehaceres.

### P1.1.

* ~~Crear un módulo de las rutas a la data.~~
* ~~Cargar la base de datos de `'all'` en una sola tabla.~~ 
* ~~Agregar los datos de `'furnished'` a la tabla original.~~
* ~~Agregar una nueva columna de categoría.~~
* ~~Asegurarse que la base de datos se cargó en una sola tabla correctamente.~~ 

### P1.2.

* ~~Limpiar las columnas Precio, área del inmueble, número de habitaciones y número de baños para asegurarse que estas columnas no tengan elementos `nan`.~~
* ~~Crear tres columnas a partir de `'property_type|rent_type|location'`:~~
    * ~~Columna `'Tipo de inmueble'`.~~
    * ~~Columna `'Tipo de oferta'`.~~
    * ~~Columna `'location'`.~~

### P1.3.

* ~~Desarrollar las funciones necesarias para el procesamiento de las columnas.~~
* ~~Mapear y procesar las columnas con las funciones creadas.~~
* ~~Agregar las columnas procesadas al `DataFrame` principal.~~

### P1.4.

* Clasificar las observaciones por tipo de producto, de acuerdo a los criterios de la tabla que aparede en el [enunciado](tarea1.pdf).

### P3 (Parte teórica)

* Mostrar que la distribución posterior de los parámetros w es proporcional a una gaussiana y escribir la demostración en el reporte. 
* Mostras la forma de la distribución predictiva posterior y escribir la demostración en el reporte.
* Deducir la forma de la log-verosimilitud de p(y| alpha, beta) y escribir el desarrollo en el reporte.
* Maximizar la función log-verosimilitud marginal en (3) para obtener las soluciones implícitas y escribir el desarrollo en el reporte.
 