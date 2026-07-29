fecha="20-07-2016"
def sacar_anio(fecha):
    date_splitter = fecha.split("-")
    anio = date_splitter[2]
    return anio
anio_de_fecha = sacar_anio(fecha)
print()

fecha="20-07-2016"
date_split = lambda x: x.split("-")[2]
print(date_split(fecha))