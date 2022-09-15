import os
import time
import random

def BorrarPantalla():
  os.system("cls" if os.name == "nt" else "clear")
iniciar_trivia=True
intentos=0
while iniciar_trivia==True:
 #Comienzo del programa 
  intentos+=1
  BorrarPantalla()
  
  RED = '\033[31m'
  GREEN = '\033[32m'
  YELLOW = '\033[33m'
  BLUE = '\033[34m'
  RESET = '\033[39m'
  CYAN = '\033[36m'
  print(YELLOW+"Bienvenido a mi trivia sobre Harry Potter"+RESET)
  print(RED+"\n           WARNING: No apto para muggles"+RESET)
  print("\n¿Cuál es tu nombre?\n")
  nombre=input("        Yo soy ")
  print("\nAntes de empezar", nombre, "recuerda lo siguiente:\n")
  print("- Para responder sólo debes digitar la letra de la alternativa y presionar Enter\n")

  print(YELLOW+"....EMPECEMOS...\n"+RESET)
  
  carga=10
  for i in range(1,carga+1):
    print(carga-i)
    time.sleep(1)
    
  
  BorrarPantalla()
  x=random.randint(0,10)
  y=random.randint(10,15)
  z=random.randint(15,20)
  xn=random.randint(15,20)
  yn=random.randint(8,12)
  zn=random.randint(0,8)

  
  puntaje=random.randint(0,20)
  print(BLUE+"Comenzarás con: ",puntaje," puntos\n"+RESET)
  print("\n____________NIVEL 1___________\n")
  print("1.A Harry se le conoce como el niño que: \n")
  print("a) sobrevivio\n")
  print("b) comio\n")
  print("c) peleo\n")
  print("d) vivio\n")
  
  rpta1=input(YELLOW+"Tu respuesta es: "+RESET).lower()
  while rpta1 not in ("a","b","c","d"):
    rpta1=input("Debes ingresar a, b, c o d. \nIngresa nuevamente tu respuesta: ").lower()
  if rpta1 == "d":
    puntaje+=10
    print(GREEN+"\nCorrecto",nombre,"!"+RESET)
  else:
    puntaje-=15
    print(RED+"\nIncorrecto ",nombre,"!"+RESET)
  
  time.sleep(2)
  BorrarPantalla() 
  
  print(BLUE+"Puntaje acumulado: ", puntaje,""+RESET)
  print("\n____________NIVEL 1___________\n")
  print("2.El nombre de su tía es: \n")
  print("a) Petunia\n")
  print("b) McGonagall\n")
  print("c) Olivia\n")
  print("d) Hermione\n")
  rpta2=input(YELLOW+"Tu respuesta es: ").lower()
  while rpta2 not in ("a","b","c","d"):
     rpta2=input("\nDebes ingresar a, b, c o d.\n \nIngresa nuevamente tu respuesta: ").lower()
  if rpta2 == "a":
    puntaje+=x
    print(GREEN+"\nCorrecto",nombre,"!"+RESET)
  else:
    puntaje-=xn
    print(RED+"\nIncorrecto ",nombre,"!"+RESET)
  
  time.sleep(2)
  BorrarPantalla() 
  
  
  print(BLUE+"Puntaje acumulado: ", puntaje,""+RESET)
  print("\n____________NIVEL 1___________\n")
  print("3.A qué casa pertenece Draco Malfoy? \n")
  print("a) Gryffindor\n")
  print("b) Ravenclaw\n")
  print("c) Slytherin\n")
  print("d) Hufflepuff\n")
  rpta3=input(YELLOW+"Tu respuesta es: "+RESET).lower()
  while rpta3 not in ("a","b","c","d"):
    rpta3=input("Debes ingresar a, b, c o d. \nIngresa nuevamente tu respuesta: ").lower()
  if rpta3 == "c":
   print(GREEN+"\nCorrecto",nombre,"!"+RESET)
   puntaje=puntaje+x
  else:
   puntaje-= xn
   print(RED+"\nIncorrecto ",nombre,"!"+RESET)
  
  if rpta1=="d" and rpta2=="a" and rpta3=="c":
   print("\n",nombre," eres un verdadero mago. Pasaste el 1er Nivel sin errores!\n")
   gg=1
  
  time.sleep(3)
  BorrarPantalla()
  
  print(BLUE+"Puntaje acumulado: ", puntaje,""+RESET)
  print("\n                NIVEL 2             \n")
  print("1.¿El sombrero seleccionador quiso poner a Hermione en que casa antes de Gryffindor?\n")
  print("a) Gryffindor\n")
  print("b) Ravenclaw\n")
  print("c) Slytherin\n")
  print("d) Hufflepuff\n")
  rpta4=input(YELLOW+"Tu respuesta es: "+RESET).lower()
  while rpta4 not in ("a","b","c","d"):
   rpta4=input("Debes ingresar a, b, c o d. \nIngresa nuevamente tu respuesta: ").lower()
  if rpta4=="b":
     puntaje=puntaje+y
     print(GREEN+"\nCorrecto",nombre,"!"+RESET)
  else:
   puntaje-= yn
   print(RED+"\nIncorrecto ",nombre,"!"+RESET)
  
  time.sleep(3)
  BorrarPantalla()
  
  print(BLUE+"Puntaje acumulado: ", puntaje,""+RESET)
  print("\n                NIVEL 2             \n")
  print("2.¿Para qué sirve el encantamiento Leviosa?\n")
  print("a) Levantar objetos\n")
  print("b) Abrir puertas\n")
  print("c) Cambiar de forma\n")
  print("d) Encender la varita\n")
  rpta5=input(YELLOW+"Tu respuesta es: "+RESET).lower()
  while rpta5 not in ("a","b","c","d"):
   rpta5=input("Debes ingresar a, b, c o d. \nIngresa nuevamente tu respuesta: ").lower()
  if rpta5=="a":
    puntaje=puntaje+y
    print(GREEN+"\nCorrecto",nombre,"!"+RESET)
  else:
   puntaje-= yn
   print(RED+"\nIncorrecto ",nombre,"!"+RESET)
  
  time.sleep(3)
  BorrarPantalla()
  
  print(BLUE+"Puntaje acumulado: ", puntaje,""+RESET)
  print("\n                NIVEL 2             \n")
  print("3.	¿Qué profesor se convertía en lobo?\n")
  print("a) Sirius\n")
  print("b) Sprout\n")
  print("c) Flitwick\n")
  print("d) Lupin\n")
  rpta6=input(YELLOW+"Tu respuesta es: "+RESET).lower()
  while rpta6 not in ("a","b","c","d"):
    rpta6=input("Debes ingresar a, b, c o d. \nIngresa nuevamente tu respuesta: ").lower()
  if rpta6=="d":
   print("\nHogwarts es tu hogar ",nombre,"Pasaste el 2do Nivel, ya te falta poco!\n")
   puntaje=puntaje+y
  else:
   puntaje-= yn
   print(RED+"\nIncorrecto ",nombre,"!"+RESET)
  time.sleep(4)
  if gg==1 and rpta4=="b" and rpta5=="a" and rpta6=="d":
   print("\n",nombre," sigues de buena racha.\n")
   ggg=1
  else:
    print("\n",nombre, " ya sólo queda un nivel. Aumenta tu puntaje Tu puedes, haz un expecto patronum!")
  
  time.sleep(4)
  BorrarPantalla()
  
  print(BLUE+"Puntaje acumulado: ", puntaje,""+RESET)
  print("\n                NIVEL 3             \n")
  print("1.	En Quidditch, ¿cuántos puntos recibes por atrapar la snitch?\n")
  print("a) 100\n")
  print("b) 200\n")
  print("c) 250\n")
  print("d) 150\n")
  rpta7=input(YELLOW+"Tu respuesta es: "+RESET).lower()
  while rpta7 not in ("a","b","c","d","e"):
   rpta7=input("Debes ingresar a, b, c o d. \nIngresa nuevamente tu respuesta: ").lower()
  if rpta7=="d":
      puntaje=puntaje+z
      print(GREEN+"\nCorrecto",nombre,"!"+RESET)
  elif rpta7=="e":
      print("\nRepuesta secreta: Si se atrapa la snitch se termina el juego")
      puntaje=puntaje+50
  else:
    puntaje-=zn
    print(RED+"\nIncorrecto ",nombre,"!"+RESET)
    
  time.sleep(4)
  BorrarPantalla()
  
  print(BLUE+"Puntaje acumulado: ", puntaje,""+RESET)
  print("\n                NIVEL 3             \n")
  print("2.	¿Cuál es el nombre del hipogrifo de Hagrid?\n")
  print("a) Hedwig\n")
  print("b) Buckbeak\n")
  print("c) Scabbers\n")
  print("d) Crookshanks\n")
  rpta8=input(YELLOW+"Tu respuesta es: "+RESET).lower()
  while rpta8 not in ("a","b","c","d"):
    rpta8=input("Debes ingresar a, b, c o d. \nIngresa nuevamente tu respuesta: ").lower()
  if rpta8=="b":
    puntaje=puntaje+z
    print(GREEN+"\nCorrecto",nombre,"!"+RESET)
  else:
    puntaje-=zn
    print(RED+"\nIncorrecto ",nombre,"!"+RESET)
  
  time.sleep(2)
  BorrarPantalla()
  
  print(BLUE+"Puntaje acumulado: ", puntaje,""+RESET)
  print("\n                NIVEL 3             \n")
  print("3.	¿Cuál es el tercer nombre del director de Hogwarts?\n")
  print("a) Percival\n")
  print("b) Albus\n")
  print("c) Brian\n")
  print("d) Wulfric\n")
  rpta9=input(YELLOW+"Tu respuesta es: "+RESET).lower()
  while rpta9 not in ("a","b","c","d"):
    rpta9=input("Debes ingresar a, b, c o d. \nIngresa nuevamente tu respuesta: ").lower()
  if rpta9=="d":
   puntaje=puntaje+z
   print(GREEN+"\nCorrecto",nombre,"!"+RESET)
  else:
    puntaje-=zn
    print(RED+"\nIncorrecto ",nombre,"!"+RESET)

  time.sleep(2)
  BorrarPantalla()
  
  print(BLUE+"Puntaje acumulado: ", puntaje,""+RESET)
  print("\n              PREGUNTA COMODIN             \n")
  print("¿Cómo se llama la mamá de Hagrid?\n")
  print("a) Abacua\n")
  print("b) Wilhemina\n")
  print("c) Fridwulfa\n")
  print("d) Fiona\n")
  rpta10=input(YELLOW+"Tu respuesta es: "+RESET).lower()
  while rpta9 not in ("a","b","c","d"):
    rpta10=input("Debes ingresar a, b, c o d. \nIngresa nuevamente tu respuesta: ").lower()
  if rpta10=="c":
   puntaje=puntaje*puntaje
   print(GREEN+"\nCorrecto",nombre,"!"+RESET)
  elif rpta10=="b":
    puntaje+=5
    print(RED+"\nIncorrecto ",nombre,"!"+RESET)
  elif rpta10=="a":
    puntaje-=5
    print(RED+"\nIncorrecto ",nombre,"!"+RESET)
  elif rpta10=="d":
    puntaje=puntaje/2
    print(RED+"\nIncorrecto ",nombre,"!"+RESET)
  

  
  print(BLUE+"\nTu puntuaje fue de: ",puntaje,""+RESET)
  seguir=input(YELLOW+"\nQuieres jugar de nuevo? Responde 'si' para repetir o cualquier tecla para finalizar: "+RESET).lower()
  
  if seguir!="si":
      iniciar_trivia=False
      print(CIAN+"\nFue un gusto conocerte ",nombre,"\n      LUMOS "+RESET)
  else:
      iniciar_trivia=True
      
