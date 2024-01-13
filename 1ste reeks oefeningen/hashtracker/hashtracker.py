ingevoerd = {}
while (True):

    invoer = input("Geef een stukje teskt in: ")

    if invoer == 'q':
        break

    invoerHash = str(hash(invoer))

    if invoerHash not in ingevoerd:
        ingevoerd[invoerHash] = invoer
        print(f"De hash van het ingevoerde tekst is: {str(hash(invoer))}")
    else:
        print(f'Deze hash is al gebruikt we nemen een hash van de hash')
        while invoerHash in ingevoerd:
            invoerHash = str(hash(invoerHash))
        ingevoerd[invoerHash] = invoer
        print(f"De nieuwe hash is {invoerHash}")
for hash, tekst in ingevoerd.items():
    print(f"{hash}: {tekst}")
