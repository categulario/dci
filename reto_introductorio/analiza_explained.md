# analiza.py

## ¿Cuál es el día de la semana, la hora y el sentido en los que hay mayor flujo de transporte en este tramo de carretera?

Una revisión rápida a los datos presentados en el archivo muestra que cada registro es un vehículo del cual se describen sus propiedades en cada columna. Para responder a la pregunta de qué día de la semana tiene mayor flujo de coches bastaría hacer un conteo de filas agrupadas por su día de la semana.

Para saber de ese día qué hora tuvo mayor flujo es necesario agrupar por día:hora y luego filtrar del ranking de horas aquellas cuyo día sea el ganador, y escoger la hora de ese día con más tráfico.

Para saber qué carril fue en general el más usado basta hacer un conteo agrupado por carril, y escoger el carril con el conteo mayor.

Las respuestas obtenidas fueron:

	El día con más tráfico es 5 con 22244 coches en suma
	de ese día, las 19 es la hora con más tráfico
	El sentido 1 es el más ocupado

### Implementación

Para hacer esto de forma eficiente se puede revisar el archivo de forma secuencial, es decir, registro por registro guardando solamente los conteos necesarios para al final poder dar la respuesta a las preguntas. La implementación actual recoge esa idea revisando cada registro, incrementando seis contadores según sea el caso y descartando el registro inmediatamente para no saturar la memoria. Toma más o menos medio segundo (intel i5) revisar el archivo entero.

## ¿Cuál es el día de la semana, la hora y el sentido en los que hay mayor tonelaje de peso cruzando en este tramo de carretera?

Responder a estas preguntas es casi idéntico a responder las anteriores excepto por un par de consideraciones:

* estimar el peso del vehículo depende de la unidad en que está dada la carga del vehículo (columna 25), la cual se encuentra en una gran variedad de formatos sin embargo un conteo rápido de los mismos muestra que solo TONELADAS es relevante pues el resto tienen a lo más 25 registros de los ~75,000 presentes.
* Acumular el peso requiere leer la columna 26 del archivo

Las respuestas obtenidas fueron:

	El día con más peso es 4 con 22820.379999999983 toneladas en suma
	de ese día, las 8 es la hora más pesada
	El sentido 1 es el más ocupado

### Implementación

Se hace en el mismo ciclo que la pregunta anterior para no añadir complejidad, preguntando por la unidad en que está la carga del vehículo e incrementando los acumuladores en el peso indicado.
