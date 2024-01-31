def feladat():
    db = 0
    i = 0
    for i in range(10, 100):
        i += 1
        if i % 2 == 0:
            db += 1
    return db