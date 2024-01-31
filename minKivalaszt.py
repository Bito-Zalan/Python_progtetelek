def feladat2():
    VEGE = 0
    db = 0
    min = 2147483647
    while (szam := int(input("Szám: "))) != VEGE:
        if szam < min:
            min = szam
        db += 1
    print(f"A választott {db} számból a legkissebb: {min}.")