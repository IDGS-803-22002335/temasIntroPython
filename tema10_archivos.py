from io import open


texto = "una line"  # lo que se va a escribir en el archivo

# especificar la forma de apertura si es de lectura o de escritura
archivo = open("archivo.txt", "w")
archivo.write(texto)
texto = "\nUna line nueva"
archivo.write(texto)
texto = "\nUna line nueva tres"
archivo.write(texto)
archivo.close()
