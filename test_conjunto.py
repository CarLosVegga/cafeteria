from cafeteria import checkOrder

# CON1: Siguen el orden solicitado
def testOrder():
    assert checkOrder("Chocolate, 5, 7, 8") == "Entrada de la orden válida"

# CON2: El orden está inverso
def testInverseOrder():
    assert checkOrder("14, 28, 30, Chocolate") == "La orden fue escrita al revés. Debe ser nombre, tamaños"

# CON3: El orden está aleatorio
def testRandomOrder():
    assert checkOrder("1, Tequila, 5, 8") == "Corrobore que el nombre de la orden solo incluya valores alfabéticos, seguido de una coma y los tamaños (separados por comas si hay más de uno)"

# CON4: Tiene estrictamente una coma entre nombre y números
def testOneComma():
    assert checkOrder("Margarita, 13, 18") == "Entrada de la orden válida"

# CON5: No tiene coma entre nombre y tamaño
def testNoComma():
    assert checkOrder("Gibson 22, 27") == "Corrobore que el nombre de la orden solo incluya valores alfabéticos, seguido de una coma y los tamaños (separados por comas si hay más de uno)"

# CON6: Coma en una posición no correcta
def testRandomComma():
    assert checkOrder("Limonada 21, 28") == "Corrobore que el nombre de la orden solo incluya valores alfabéticos, seguido de una coma y los tamaños (separados por comas si hay más de uno)"

# CON7: Aceptar espacios que separen la unión de la order y el tamaño
def testSpaces():
    assert checkOrder("Margarita  ,  29, 32") == "Entrada de la orden válida"