longitud = float(input("Ingrese la longitud de la alberca en metros: "))
ancho = float(input("Ingrese el ancho de la alberca en metros: "))
altura = float(input("Ingrese la altura de la alberca en metros: "))
tarifa_por_metro_cubico = float(input("Ingrese la tarifa por metro cúbico: "))

volumen = longitud * ancho * altura
pago_total = volumen * tarifa_por_metro_cubico
print(f"El pago total por llenar la alberca es: ${pago_total:.2f}")