def testanumeros(a,b):
    assert a > 0 and b > 0 , "Numeros precisam ser maior que 0"
    assert a < 10, "Numero 'a' precisa ser menor que 10"
    return a + b

print(testanumeros(4,2))