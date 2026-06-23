# Entrada de datos
try:
    height  = int(input("Introduzca su altura en cm: "))
    credits = int(input("Introduzca sus crÃ©ditos: "))
except ValueError:
    print("Error: introduzca solo nÃºmeros enteros.")
    exit()

# Mensajes de respuesta
respuestas = {
    "ok":          "Enjoy the ride!",
    "low_height":  "You are not tall enough to ride.",
    "low_credits": "You don't have enough credits.",
}

# Ãrbol de decisiones
if height < 130:
    print(respuestas["low_height"])
elif credits < 2:
    print(respuestas["low_credits"])
else:
    print(respuestas["ok"])
