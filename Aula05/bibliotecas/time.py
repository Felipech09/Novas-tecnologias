import time

# Retorna a hora atual em segundos desde 00:00:00 de 1/1/1970 (Epoch)
segundos = time.time()
print("Segundos desde Epoch:", segundos)

# Converte um valor em segundos para string legível
print("Data/hora formatada:", time.ctime(segundos))

# Retorna a hora local como struct_time
print("Hora local:", time.localtime())

# Retorna a hora UTC como struct_time
print("Hora UTC:", time.gmtime(segundos))
