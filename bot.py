import random

def run():
  while True:
    pregunta = input("¿Qué quieres saber? ")
    respuesta = random.choice([
      "No lo sé",
      "Eso es una pregunta difícil",
      "¡No puedo creer que me hayas preguntado eso!"
    ])
    print(respuesta)

if __name__ == "__main__":
  run()
