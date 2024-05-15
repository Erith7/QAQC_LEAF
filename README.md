Códigos para la realización de QAQC para las mallas de interpretación extraídas de CEO. 

Procedimiento de Ejecución:

1. 01_datareader.py : Este código realiza la lectura de las mallas de interpretación para los técnicos juniors y especialistas. Crea un archivo CSV que incluye todos los datos interpretados para la malla de campo, en un formato adecuado para la realización de los siguientes pasos.

2. 02A_Summarizer.py : Este código toma el archivo de salida de 01_datareader.py, y genera un nuevo archivo que contiene la clase de cambio alcanzada por los 3 interpretes para cada parcela, y se agrega una columna con el tipo de coincidencia de interopretación, para cada año.

3. 03A_overall_agreement :  Este código genera archivos con el porcentaje de coincidencias de cada técnico por año
   
5. 04_A_OASummary : Este código permite estimar el porcentaje de coincidencias con dos o un intérprete
6. 05_ChangesSummary: Este código permite generar porcentajes de coincidencias por clases y por año.

   Este procedimiento está concebido para ser corrido por cadas estrato de bosque.
