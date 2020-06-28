# TP-Final-Electrotecnia
1er Cuat 2020

1. Implementaci´on de interfaz gr´afica en Python
La habilidad para desarrollar interfaces gr´aficas utilizando lenguajes de alto nivel es muy ´util
cuando se requiere dise~nar software que sea f´acil de manejar por usuarios. En este ejercicio el objetivo
ser´a que dise~nen e implementan una interfaz gr´afica que tenga la capacidad de simular algunos de
los circuitos que se estudian en la materia.
Deber´an programar una interfaz gr´afica que le permita al usuario simular:
Filtros de primer orden
◦ Pasa bajos
◦ Pasa altos
◦ Pasa todo
◦ Filtro con polo y/o cero arbitrarios, detectar que tipo de filtro es (opcional)
Filtros de segundo orden
◦ Pasa bajos
◦ Pasa altos
◦ Pasa todo
◦ Pasa banda
◦ Notch
◦ Low-pass notch (opcional)
◦ High-pass notch (opcional)
◦ Filtro con polos y cero/s arbitrarios, detectar que tipo de filtro es (opcional)
Para cada filtro, el usuario debe poder configurar:
Primer orden: frecuencia del polo y/o cero.
Segundo orden: !0 y ξ de los polos y/o ceros.
Se debe poder configurar la ganancia en banda pasante o configurar la ganancia m´axima (las
dos).
La simulaci´on debe permitir graficar:
Salida del sistema con algunas entradas:
◦ Senoide de frecuencia y amplitud configurables
◦ Pulso u(t) de amplitud configurable
◦ Pulso peri´odico de amplitud y duty cycle configurables (opcional)
◦ Otras se~nales (opcional)
Gr´afico bode del sistema, con el eje de frecuencia en Hertz y el modulo en dBs
Diagrama de polos y ceros
Algunas consideraciones adicionales:
En el git con ejemplos est´a subido un apunte en el cu´al se define con mayor precisi´on de que
se trata cada filtro mencionado en la consigna.
Las librer´ıas que necesitar´an ser´an MatplotLib, Scipy.Signal y Numpy
Pueden agregar cualquier funcionalidad no obligatoria que le d´e valor al trabajo tanto de las
opcionales como alguna idea de ustedes, sumar´a puntos extra.
