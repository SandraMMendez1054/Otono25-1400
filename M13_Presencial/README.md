
🔎 Preguntas de Investigación y Experimentación

# Diferencia entre fullmatch y search:
Si en la función validar_email usáramos re.search en lugar de re.fullmatch, ¿qué pasaría si la cadena de entrada fuera "Esto es invalido email@valido.com el resto"? ¿Por qué es fullmatch la elección correcta para una validación de formato estricta?

- re.search: esta funcion Busca coincidencia en cualquier parte, ejemplo encuenta email@valido.com dentro del texto.

- re.fullmath: exige coincidencia en toda la cadena. ejemplo Devuelve None porque la cadena completa no es un email válido

# Grupos de Captura: 
En el TODO 2, ¿por qué fue importante usar el metacaracter () para "capturar" solo los 5 dígitos, en lugar de usar solo el patrón sin agrupar? Investiga y explica cómo el uso de match.group(1) te permite aislar la información específica que necesitas.

Los paréntesis () en expresiones regulares permiten capturar subgrupos dentro de una coincidencia. En el TODO 2, se usaron para aislar los 5 dígitos del código de producto. Gracias a match.group(1), obtenemos directamente el ID (12345) en lugar de toda la cadena (PROD-12345).


# Clases de Caracteres y Negación: 
En el TODO 3, ¿cómo se logra la "negación" de un conjunto de caracteres (es decir, hacer coincidir todo excepto letras, números o espacios)? ¿Qué ocurriría si intentaras usar la función re.search en lugar de re.sub para esta tarea? Explica por qué re.sub fue la herramienta correcta para la tarea de "limpieza" de texto.

La negación en clases de caracteres se logra con [^...]. En el TODO 3, esto permitió identificar cualquier carácter que no fuera letra, número o espacio. Usar re.search solo detectaría el primero, mientras que re.sub reemplaza todos los caracteres no permitidos, logrando la limpieza completa del texto.