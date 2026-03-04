#cos ho cambiato: | while i != f or l[m]==n: | qua : or l[m]==m diciamo di continuare anche se il numero è uguale
# ---->sostituito con i<=f
# quando controllo se l[m]< n : aggiungo uno se > sottraggo uno 
#evito che come prima , sommando i 2 numeri e poi dividendoli davano sempre lo stesso risultato facendoli ripartire dalla stessa posizione facendolo all infinito
def ricercaDicotomica(l, n):
    i = 0
    f = len(l) - 1
    while i <= f:

        m = (i + f) // 2    

        print(i, m, f) 

        if l[m] == n:
            return True

        elif l[m] < n:
            i = m + 1

        else:
            f = m - 1

    return False

lista = [10, 12, 44, 72, 88, 96, 104, 1000]
print(ricercaDicotomica(lista, 1000))


