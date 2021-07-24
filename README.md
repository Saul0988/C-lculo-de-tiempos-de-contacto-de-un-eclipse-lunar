# C-lculo-de-tiempos-de-contacto-de-un-eclipse-lunar
En este proyecto se realiza un código que nos permite calcular en buena aproximación el tiempo en que se dan los tiempos de contacto de un eclipse, introduciendo las coordenadas ecuatoriales del Sol y la Luna para el día del eclipse.
Para ingresar los datos hay que asegurarse de tener el formato: (ejemplo)
Hora    GHAs_grados   GHAs_minutos    Decs_grado    DecS_minutos    GHAm_grado    GHAm_minutos    DecM_grado    DecM_minutos    SS      PS      SM      PM 
02      207           13.3            -19           59.60	          029           11.2            20            34.90           16.30   08.939  166.70  61.300
03      222           13.1            -19           59.00	          043           33.3            20            30.50           16.30   08.939  16.70   61.300
-
-
...


Donde cada parámetro viene en los almanaques naúticos:

hora: hora en UT
GHAs_grado: ascensión recta del Sol (grados)
GHAs_minutos: ascensión recta del Sol (minutos)
DecS_grado: declinación del Sol (grados)
DecS_minutos: declinación del Sol (minutos)
GHAm_grado: ascensión recta de la Luna (grados)
GHAm_minutos: ascensión recta de la Luna (minutos)
DecM_grado: declinación de la Luna (grados)
DecM_minutos: declinación de la Luna (minutos)
SS: semidiámetro del Sol
PS: paralaje horizontal ecuatorial del Sol
SM: semidiámetro de la Luna
PM: paralaje horizontal ecuatorial de la Luna

A la hora de ejecutar el programa te da la opción a poner manualmente el semidiámetro del Sol, el paralaje horizontal ecuatorial del Sol, el semidiámetro de la Luna y el paralaje horizontal ecuatorial de la Luna, ya que no suelen variar mucho y por lo tanto no hace falta estar repitiendo el mismo valor en el documento txt. En caso de que se haya colocado en el documento txt., se solicita poner 0 en el valor de entrada.
