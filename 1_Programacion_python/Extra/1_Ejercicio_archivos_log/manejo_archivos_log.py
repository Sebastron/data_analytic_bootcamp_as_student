#Pueden ingresar cualquier extensión, como preferencia se trabajó con txt
log1 = input("Ingrese el Path y nombre del primer archivo log, formato 'ruta/nombre.extension': ")
log2 = input("Ingrese el Path y nombre del segundo archivo log, formato 'ruta/nombre.extension': ")
output = input("Ingrese la ruta y el nombre del archivo, donde desee guardar, en formato 'ruta/nombre.extension': ")

new_file = [] #Variable que almacena las lineas de dos archivos
#Lectura del primer log
with open(log1) as archivo1:
    #Se asume que hay salto de lines en el contenido y se recorre las lineas
    #Se recorre las lineas
    for i in archivo1.read().split("\n"):
      #Se separa en cada lines los valores por ;
      new_file.append(i.split(';'))

#Lectura del segundo log, se aplica el mismo procedimiento
with open(log2) as archivo2:
    for i in archivo2.read().split("\n"):
      new_file.append(i.split(';'))
#Se escribe en otro archivo
with open(output, 'w') as new_log:
  for new_line in sorted(new_file, key=lambda line : int(line[2]), reverse=False):
    cont = 0
    s = ''
    for column in new_line:
      if(cont+1 == len(new_line)):
        s += column
        break
      s += column + ";"
      cont+=1
    new_log.writelines(s + "\n")