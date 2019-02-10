# CADENAS DE DOCUMENTACIÓN (Docstrings)

'''This is a multiline docstring.'''
print('Hello, World!')

# VARIABLES

x = 5
y = "Lil"
print(x)
print(y)

x = 4  # x is of type int
x = 'Lil'  # x is now type str
print(x)  # (Las variables son sensibles, pueden cambiar el tipo)

x = 'awesome'
print('Python is ' + x)  # (Se usa + para combinar texto y variable)

x = 'Python is '
y = 'awesome'
z = x + y
print(z)  # (Variable + variable)

x = 5
y = 10
print(x + y)  # (En números el + funciona como operador matemático)

# x = 5
# y = 'Lil'
# print(x + y) (Error, no se puede string + número)

# NÚMEROS (int, float, complex), (para verificar: type () )

x = 1  # int entero, sin decimales
# float con decimales (Números científicos agrega e indica potencia de 10)
y = 2.8
z = 1j  # complex complejos (Se escriben con j como la parte imaginaria)

print(type(x))
print(type(y))
print(type(z))


# CONDICIONALES (if, elif, else)

if 5 > 2:
    print('Five is greater than two!')

if 3 > 2:
    print("It works!")

if 5 > 2:
    print("5 is indeed greater than 2")
else:
    print("5 is not greater than 2")

name = "Lil"
if name == "Dav":
    print("Hey Dav!")
elif name == "Lil":
    print("Hey Lil")
else:
    print("Hey anonymous!")

volume = 57
if volume < 20:
    print("It's kinda quiet")
elif 20 <= volume < 40:  # volumen >=20 and volumen <40
    print("It's nice for background music")
elif 40 <= volume < 60:  # volumen >=40 and volumen <60
    print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
    print("Nice for parties")
elif 80 <= volume < 100:
    print("A bit loud")
else:
    print("My ears hurt! :(")

# (Cambiar el volumen si está muy alto o muy bajo)
if volume < 20 or volume > 80:
    volume = 50
    print("Mucho mejor!")
print(volume)

# FUNCIONES


def hi():
    print("Hi there!")
    print("How are you?")


hi()


def hola(nombre):
    if nombre:
        print("Hola" + " " + nombre)
    else:
        print("Hola anónimo")


hola("Lil")


def hi(name):
    if name == "Hola":
        print("Hi hola!")
    elif name == "Lil":
        print("Hi Lil!)")
    else:
        print("Hi anonymous!")


hi("legolas")


def hi(name):
    print("Hi " + name + "!")


hi("Lil")

# BUCLES

girls = ["Ilta", "Azucena", "Luna", "Abril", "Iris"]

for name in girls:
    hi(name)
    print("Next girl")

# Mientras i = 1, sea menor que 6, i++
for i in range(1, 6, 1):
    print(i)

# Esto es lo mismo que lo de arriba
contador = 1
while contador < 6:
    print('contador vale: '+str(contador))
    contador += 1

# Java
# for (i = 1; i < 6; i+=1) {
#         System.out.println(i);
# }

# Triples comillas (''' o """) son llamadas docstrings -
# puedes escribirlos en la parte superior de un archivo, clase o método
# para describir lo que hace.
'''

'''
