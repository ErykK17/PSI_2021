lista_liczb = [6,3,7,3,7,8,4,2,6,3,1]
lista_liczb_2 = (lista_liczb[5:])
lista_liczb = lista_liczb[:5]
lista_polaczona = lista_liczb + lista_liczb_2
lista_polaczona.insert(0,0)
kopia_polaczonej = lista_polaczona
kopia_polaczonej_sorted = kopia_polaczonej.sort(reverse=True)

print(lista_liczb, "\n", lista_liczb_2)
print (lista_polaczona)
print (kopia_polaczonej_sorted)
