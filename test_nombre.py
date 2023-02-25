from cafeteria import checkName

#NOM1: Cantidad mínima de caracteres válidos
def testMinChar():
    assert checkName("Té") == "Entrada del nombre válida"

#NOM2: Por debajo de la mínima de caracteres válidos
def testUnderMinChar():
    assert checkName("s") == "El nombre es menor al mínimo tamaño"

#NOM3: La máxima cantidad de caracteres válidos
def testMaxChar():
    assert checkName("ChocolateChocol") == "Entrada del nombre válida"

#NOM4: Por arriba de la máxima cantidad de caracteres válidos 
def testOverMaxChar():
    assert checkName("ChocolateChocolate") == "El nombre excede el máximo tamaño"

#NOM5: Dentro del rango aceptado de caracteres válidos 
def testWithinRange():
    assert checkName("Chocolate") == "Entrada del nombre válida"

#NOM6: Combinación de nombre alfanuméricos
def testAlphanumeric():
    assert checkName("Va1nilla") == "El nombre no puede incluir valores que no sean alfabéticos"

#NOM7: Nombres compuestos (con espacios) por debajo del límite de caracteres
def testValidComplexNames():
    assert checkName("Atole de fresa") == "Entrada del nombre válida"

#NOM7: Nombres compuestos (con espacios) por arriba del límite de caracteres
def testLongerComplexNames():
    assert checkName("Atole de chocolate") == "El nombre excede el máximo tamaño"
