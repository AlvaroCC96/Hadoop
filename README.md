# Hadoop
---
## Autores.

Patricio Araya.

Alvaro Castillo. 

---
Desarrolle mappers y reducers en Python que den solución a las siguientes preguntas, las cuales están enfocadas en el archivo “access_log” presente en el directorio “udacity_training_data” de la máquina virtual de Cloudera.

### a) ¿Cuántas peticiones GET devolvieron un error 4XX?

### b) Muestre cuántas peticiones se hacen al servidor agrupadas por mes.

Primeramente, se leen los registros, mientras se formatean los datos necesitados en el archivo **mapper.py** obteniendo resultados basados en una **KEY** y un **VALUE**, evitando el daño y perdida de datos a través de la programación defensiva. Luego se reducen los resultados obtenidos en el mapper a través del archivo **reducer.py**.

El resultado final para cada problema se generó en las carpetas **output_*** respectivamente.

