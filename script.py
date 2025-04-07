# Escritura en un archivo de texto
with open("my_notes.txt", "w", encoding="utf-8") as file:
    file.write("Primera nota: El Martes 08 de Abril cumplo 18 años.\n")
    file.write("Segunda nota: Naci el 08 de Abril de 2007, un Domingo.\n")
    file.write("Tercera nota: Me gusta la tecnología en general .\n")

# Lectura del archivo línea por línea
with open("my_notes.txt", "r") as file:
    line = file.readline()
    while line:  # Mientras haya líneas para leer
        print(line.strip())  # Imprime la línea sin espacios extra
        line = file.readline()  # Lee la siguiente línea
