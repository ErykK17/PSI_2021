name = "Eryk"
surname = "Krygier"

def reverse_name(name):
    namel=name.lower()
    lenght= len(namel)
    newstring =namel[lenght-1].upper()+ namel[lenght-2::-1]
    return str(newstring)
print(reverse_name(name), reverse_name(surname))