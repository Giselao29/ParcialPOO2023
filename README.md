![Planetas](https://images.pexels.com/photos/17505896/pexels-photo-17505896/free-photo-of-hombre-corriendo-nebulosa.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1)<br>

## Modelo básico de personas y planetas.

Nos piden armar parte del modelo de un juego con temática de Star Wars, que incluye a los planetas y a sus habitantes.
De cada persona se registra su edad, o sea cuántos años tiene. Debe poder obtenerse: la potencia, la inteligencia y si es o no destacado. Potencia e inteligencia son dos valores numéricos. En principio, corresponden estas definiciones:
<br><ul>
  <li>la inteligencia es de 12 para las personas de entre 20 y 40 años, y de 8 para las otras.</li>
  <li>la potencia es de 20 para todas las personas.</li>
  <li>una persona es destacada si tiene, exactamente, 25 ó 35 años. O sea, si una persona tiene 25 años es destacada, si tiene 35 años es destacada, si tiene cualquier otra edad no es destacada.</li>
</ul><br>
Además de estas definiciones que sirven para la generalidad de las personas, se definen algunos tipos de personas con características especiales. En principio vamos a contemplar a los atletas y los docentes.<br>
De cada atleta se mantienen la masa muscular (que comienza en 4 kilos) y la cantidad de técnicas que conoce (que comienza en 2).<br>
La potencia de un atleta es la suma del valor común para todas las personas, con la multiplicación entre masa muscular y cantidad de técnicas que conoce.<br>
Un atleta es destacado si cumple la condición común para todas las personas, o bien, conoce más de 5 técnicas.<br>
Definir las siguientes dos acciones para los atletas:
<br>
<ul>
  <li>aprender una técnica: el efecto es sumar uno a la cantidad de técnicas que conoce el atleta.</li>
  <li>entrenar una cantidad de días: el efecto es sumar a la masa muscular 1 kilo por cada 5 días de entrenamiento. P.ej. el efecto de entrenar 15 días, es sumar 3 kilos a la masa muscular</li>
</ul>
<br>De cada docente se conoce la cantidad de cursos que dio, que arranca en 0.<br>
La inteligencia de un docente es la suma del valor común para todas las personas, con el doble de la cantidad de cursos que dio.<br>
Un docente es destacado si dio más de 3 cursos.<br>
¡Atención! la condición general para considerar a una persona como destacada no corre para los docentes, o sea, un docente que haya dado 3 o menos cursos nunca es destacado, aunque tenga p.ej. 25 años.<br>
De cada planeta se conocen los habitantes, que son personas. También la cantidad de museos que hay en el planeta.<br>
Se tiene que poder obtener, para cada planeta<br>
<br>
<ul>
  <li>si es culto: la condición es que haya al menos dos museos, y que todos los habitantes tengan al menos 10 unidades de inteligencia</li>
  <li>la delegación diplomática, que está formada por los habitantes destacados.</li>
  <li>la potencia real: es la suma de la potencia de todos los habitantes.</li>
</ul>



