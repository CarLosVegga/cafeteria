import re

def checkOrder(order):
    VALID_NAME = "Entrada del nombre válida"
    VALID_SIZE = "Entrada de números válida"

    # Check for inverse order organization (quantity, name)
    inverseName = order.rsplit(",", 1)[1]
    inverseSize = order.rsplit(",", 1)[0]
    if (checkName(inverseName) == VALID_NAME and checkSizes(inverseSize) == VALID_SIZE):
        return "La orden fue escrita al revés. Debe ser nombre, tamaños"

    # Check for correct order organization (name, quantity)
    name = order.split(",", 1)[0]
    size = order.split(",", 1)[1]
    if (checkName(name) != VALID_NAME or checkSizes(size) != VALID_SIZE):
        return "Corrobore que el nombre de la orden solo incluya valores alfabéticos, seguido de una coma y los tamaños (separados por comas si hay más de uno)"
    return "Entrada de la orden válida"



def checkName(name):
    name = name.replace(" ", "")
    
    # Check for names within longitude range
    if len(name) > 15:
        return "El nombre excede el máximo tamaño"
    if len(name) < 2:
        return "El nombre es menor al mínimo tamaño"
    
    # Check for alphabetical names
    if not (name.isalpha()):
        return "El nombre no puede incluir valores que no sean alfabéticos"
    return "Entrada del nombre válida"



def checkSizes(sizes):
    MIN_VALUE = 1
    MAX_VALUE = 48
    MIN_QUANTITY = 1
    MAX_QUANTITY = 5

    # Check for incorrect format (consecutive commas)    
    hasConsecutiveCommas = re.search(",(,+)", sizes)
    if hasConsecutiveCommas:
        return "Formato incorrecto de comas en el tamaño. Úsalo para separar múltiples tamaños"
    
    # Check for an empty string
    sizes = sizes.replace(" ", "").split(",")
    if len(sizes) == 1 and sizes[0] == "":
        return "El tamaño esta por debajo la cantidad mínima permitida"

    # Check that only integers are in the input
    orderedSizes = []
    try:
        for num in sizes:
            orderedSizes.append(int(num))
    except:
        return "En el tamaño se deben ingresar solo números enteros"
    
    # Check that the non-repeatable values are within the valid range
    orderedSizes.sort()
    sizes = [int(x) for x in sizes]
    prev = None
    for num in orderedSizes:
        if num < MIN_VALUE:
            return "En el tamaño un valor está por debajo del rango aceptable"
        if num > MAX_VALUE:
            return "En el tamaño un valor está por arriba del rango aceptable"
        if num == prev:
            return "En el tamaño no se permiten valores repetidos"
        prev = num

    # Check that the input quantity is within range
    if len(orderedSizes) > MAX_QUANTITY:
        return "El tamaño excede la cantidad máxima permitida"
    elif len(orderedSizes) < MIN_QUANTITY:
        return "El tamaño esta por debajo la cantidad mínima permitida"
    
    # Check that the array is order ascendently
    if (orderedSizes != sizes):
        return "En el tamaño se debe ingresar los números ascendentemente"
    
    return "Entrada de números válida"
