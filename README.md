# ACADES

V 1.0

Edison Javier Herran Cortes - ejherran.c@ŋmail.com

Implementación académica del algoritmo DES sobre lenguaje Python 2.x


== Descripción ==

Esta pieza de código permite emular el conocido algoritmo de cifrado DES (Data Encryption Standard – http://es.wikipedia.org/wiki/Data_Encryption_Standard); utilizando cadenas des texto compuestas por 1 y 0 para representar las operaciones a nivel de bits del algoritmo original.

Su propósito es meramente académico, ya que el uso de cadenas de texto como sustituto de los bloques de bits genera una ralentización desmedida del algoritmo, esto sumado al hecho de que la presente implementación solo puede operar sobre ficheros de texto plano, hacen de la misma una solución por completo inútil en casos de aplicación real.


== Contenido ==

+> acades.py: Punto de inicio de la ejecución, lee y escribe los ficheros objetivos.


+> basico: Modulo de funciones básicas para conversión de tipos.

+----> numbers.py: Modulo para conversión de tipos (entero, carácter, binario, hexadecimales).

+----> utils.py: Modulo de funciones útiles para operar cadenas de textos en formatos de 1 y 0.


+> algoritmo: Modulo general del algoritmo DES.

+----> key.py: Modulo para generar y verificar las claves a usar en el algoritmo des modo BIN y HEX.

+----> subkeys.py: Modulo que genera las 16 subclaves que usa el algoritmo DES.

+----> des.py: Modulo principal que ejecuta las funciones de cifrado y descifrado.

== Uso ==

Use los siguientes comandos:

        python acades.py -genkey                                #Generar una clave
        python acades.py -key [DESKEY] -enc [ARCHIVO].txt       #Cifrar un archivo txt.
        python acades.py -key [DESKEY] -des [ARCHIVO].hex       #Descifrar un archivo hex.

ACADES cifra archivos de texto plano (txt) y genera archivos hexadecimales (hex) y descifra en sentido contrario (hex -> txt).
