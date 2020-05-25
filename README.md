# Prueba Técnica programador python para Crusardi SAS

Repositorio con la solución de la prueba técnica para analista de datos utilizando python y Postgresql.

Link de la prueba https://gitlab.com/crusardi/prueba_tecnica

"Objetivo
Revisar conceptos de API's y transformación de data usando las herramientas básicas de Python.

Procedimiento.

Desde http://dummy.restapiexample.com/api/v1/employees obtener todos los empleados.
Por cada uno de los empleados obtener los 5 con mejor salario. (consultar http://dummy.restapiexample.com/)  Dichos datos deben ser guardados en la base de datos de su elección (PostgreSQL, MySQL, MongoDB, SQlite)
Guardar toda la base de datos en un archivo .json.
Al ejecutarse el programa, se debe imprimir el tiempo de ejecución total del programa.
La prueba debe entregarse en un repositorio de Git, deseable con instrucciones de ejecución.
"

## Librerias necesarias

Las librerias necesarias para el virtual environment se encuentran en el archivo requirements.txt.


## Ejecución del programa

El programa se ejecuta desde el archivo start.py.
Se conectará automáticamente a la base de datos alojada en heroku.
Se extrae la información de la API call, se ordenan los empleados de mayor a menor.
Los cinco primeros se guardarán en la base de datos.
Por medio de consultas con Psycopg2  se extraen los datos de la base y se guardan en un archivo json en el directorio /data/.
Por último se imprime el tiempo de ejecución del programa.

## Funcionalidades adicionales
El programa tambien consiste con funcionalidades adicionales como crear archivos cvs con la información en el módulo /modules/Functions.
Se puede manipular la base de datos directamente mediante consultas preestablecidas en el módulo /modules/Queries.

## Autor

Juan David Ortiz
www.jtruji.xyz
https://github.com/jtruji68



