from cafeteria import checkSizes

# TAM1: Array ordenado ascendentemente
def testArrayAsc():
    assert checkSizes("4, 5, 6") == "Entrada de números válida"

# TAM2: Array ordenado descencientemente
def testArrayDesc():
    assert checkSizes("6, 5, 4") == "En el tamaño se debe ingresar los números ascendentemente"

# TAM3: Array con valores repetidos
def testArrayRepetition():
    assert checkSizes("3, 3, 7") == "En el tamaño no se permiten valores repetidos"

# TAM4: Array no ordenado
def testArrayRandom():
    assert checkSizes("40, 23, 47, 4") == "En el tamaño se debe ingresar los números ascendentemente"

# TAM5: Comas colocadas correctamente
def testCommasWellPlaced():
    assert checkSizes("5, 6, 7") == "Entrada de números válida"

# TAM6: Dos comas seguidas sin separar valores
def testCommasBadlyPlaced():
    assert checkSizes("18,, 29, 30") == "Formato incorrecto de comas en el tamaño. Úsalo para separar múltiples tamaños"

# TAM7: Valores no separados por comas
# Se considera como 293031, por lo tanto está fuera del rango
def testNoCommas():
    assert checkSizes("29 30 31") == "En el tamaño un valor está por arriba del rango aceptable"

# TAM8: El máximo de valores colocados
def testMaxQuantity():
    assert checkSizes("4, 5, 6, 7, 8") == "Entrada de números válida"

# TAM9: Excede la cantidad máxima de valores
def testOverMaxQuantity():
    assert checkSizes("13, 14, 15, 16, 17, 18") == "El tamaño excede la cantidad máxima permitida"

# TAM10: El mínimo de valores colocados
def testMinQuantity():
    assert checkSizes("38") == "Entrada de números válida"

# TAM11: Por debajo del mínimo de valores
def testUnderMinQuantity():
    assert checkSizes("") == "El tamaño esta por debajo la cantidad mínima permitida"

# TAM12: Un valor por debajo del rango mínimo
def testUnderMinRange():
    assert checkSizes("0") == "En el tamaño un valor está por debajo del rango aceptable"

# TAM13: Un valor por arriba del rango válido
def testOverMaxRange():
    assert checkSizes("57") == "En el tamaño un valor está por arriba del rango aceptable"

# TAM14: Un valor dentro del rango válido
def testWithinRange():
    assert checkSizes("33") == "Entrada de números válida"

# TAM15: Un decimal dentro de las cantidades
def testDecimal():
    assert checkSizes("2.4, 5") == "En el tamaño se deben ingresar solo números enteros"

# TAM16: Un espacio entre números
def testSpace():
    assert checkSizes("4, 1 0") == "Entrada de números válida"

# TAM17: Se incluyen valores no numéricos
def testNoNumericValues():
    assert checkSizes("A9, 4, 9") == "En el tamaño se deben ingresar solo números enteros"