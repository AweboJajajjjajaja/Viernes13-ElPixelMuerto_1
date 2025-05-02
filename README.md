# Viernes13-ElPixelMuerto_1
Es para una tarea (LITERALMENTE)


¿De que irá el juego?

Este juego irá sobre el juego Viernes 13: The Game, pero una versión RPG (Estilo pokémon según mi clase, pero nosotros lo haremos un poco como queramos la verdad).

Primero: Menú de inicio
El menú de inicio es simple, y no me voy a poner a describirlo porque no importa, (Y lo tiene que diseñar mi amigo. Por ahora solo debemos tener algo de la jugabilidad hecho.)

Segundo: El mapa. 
El mapa será un camino en el que hay cabañas al rededor. Listo. 
¿Como se deberia de ver? --> Ir a los archivos que dejaré dentro de una carpeta llamada "Imagenes de muestra", o algo asi. Realmente no sé que poner.

Tercero: JUGABILIDAD (Lo importante, básicamente)
¿Como debe de ser?

En la programación del juego se harán 3 pantallas. La pantalla del punto de inicio, el mapa en sí (En donde comienza el juego), y las casas por dentro (Que realmente no será en la casa, será en el "tejado", pero aún así hay que hacer una pantalla a parte solo para eso, según lo que entiendo de programación. Ya que son escenarios distintos.)

Cuando el juego inicia (Luego de seleccionarlo en el menú de inicio), el personaje principal/que controlamos, estará dentro de su "casa"/"Choza"/Punto de inicio (pantalla 4, en el código se hace referencia a esto). 

El cual será la caseta de Jason junto a una mesa en donde habrán 2 items para tomar, un machete y un mapa (Que lo segundo es de decoración, ya que simplemente se usará el machete).

El juego no debe permitir salir al jugador hasta que haya tomado almenos el machete, ya que al salir, se cambiarán los sprites del jason sin machete a un jason con machete (Que todavía no ha terminado y tampoco ha hecho animaciones).

Al salir de la casa se pasará a la siguiente pantalla (la del mapa), en la cual deben haber 20 campistas, que solo serán 5 campistas aleatorios, junto a sus animaciones de andar que solo van hacia arriba y hacia abajo, (Para moverse a los lados van a usar cualquiera de esas dos direcciones, porque mi amigo no va a hacer el movimiento hacia los lados de esos).

Habrán 4 "casas"/"Chozas" en las cuales entrar, y cada una de ellas tendrá un cuadrado verde encima para marcar al jugador de que no ha entrado en esa casa/choza. Para entrar habría que romper las puertas pulsando repetidamente la "E". 
(Mi amigo quiere que esas 4 casas vayan rotando para que el juego no se haga repititivo. Pero en caso de que no se logre, no importa. No hay tiempo)

Y al entrar en esas "casas"/"Chozas", habria que llevar al jugador a la pantalla 6 (Mencionada en el código).

-----(LO QUE SE PODRÍA HACER)-----
-
Claramente, para que cada vez que entres a una casa que ya has entrado, hay que guardar el valor de la casa para que en el caso de que vuelvas a entrar, no hayan campistas. 

---- (LO QUE YO PREFERIRÍA HACER, LA VERDAD)----
-
O, hacer que luego de entrar a una casa/choza, no puedas salir de esta hasta matar a los campistas, y una vez salgas, no puedas volver a entrar. Para ahorrarse lo de guardar el valor y todo eso. Y luego de salir, cambiar el color del cuadrado, mencionado anteriormente, a rojo.

Habría un tiempo limite de 10 minutos para matar a los 20 campistas. Al iniciar el juego, sonaria la voz de la madre de jason. Al matar a la mitad de campistas igual. Y al matarlos a todos, aparte de una pantalla de victoria, otra vez la voz de la madre.

A los 5 minutos, si todavía no se han matado a todos los campistas, aparecería Tommy Jarvis, el cual cuenta con una escopeta con balas infinitas, pero un tiempo entre disparo y disparo de 15 o 30 segundos. (Daño de cada bala: 50)
Tommy Jarvis disparará al jugador/jason, y lo matará de 3 disparos.

----> VIDA DE JASON(el jugador) <----
-
Jason contará con un valor de vida(150), que será controlado por los disparos de Tommy Jarvis (que reciba), o, si se le escapa un campista a la hora de tratar de matarlo.

Cuando Jason "mata" (ataca) a un campista, realmente tendria que aparecer una "barra de precisión" en la que Jason solo tiene 5 segundos para acertar en un punto aleatorio de esa barra (Como al atacar en Undertale). El punto aleatorio estará marcado por un color verde que ocupe el 10% de una barra roja. (Digamos que la barra ROJA es de 200x40, pues en un punto aleatorio de esta barra, un 20x40 será de color verde) Si el jugador le da a la zona verde, matará al campista, pero si no le da, el campista escapará y hará un pequeño daño al Jason, (Si Jason tiene 150 de vida, el campista hace 5 de daño). Incluso si el campista escapa, no saldrá de la casa/choza (O entrará. Los campistas no van a entrar/salir de las chozas, simplemente estarán en la pantalla en la que se encuentren).


(CREO QUE NO ME HE DEJADO NADA, Pero en el caso de que alguien vea un error, que me avise. Llevo aproximadamente 1 hora con este texto y me he olvidado lo que he puesto. Ahora voy a poner la carpeta mencionada en las primeras lineas)
