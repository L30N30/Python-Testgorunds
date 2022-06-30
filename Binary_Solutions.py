def binario_decimal(binario):
    exponentes = []

    for i in range(len(binario)):
        exponentes.append(i)

    binario.reverse()
    result = 0

    for i in range(len(binario)):
        if binario[i] == 1:
            result += 2 ** exponentes[i]

    print(result)


def decimal_binario(decimal, num_ceros):
    exponentes = []
    result = []

    for i in range(num_ceros):
        exponentes.append(i)
    exponentes.reverse()

    for i in exponentes:
        if decimal >= 2 ** i:
            decimal -= 2 ** i
            result.append(1)
        else:
            result.append(0)

    print(result)


binario_decimal([1,1,0,0,1,0,1,1])
# decimal_binario(99, 8)