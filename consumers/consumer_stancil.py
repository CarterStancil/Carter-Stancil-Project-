def consumer(q, storage):
    while True:
        row = q.get()
        if row is None:   
            break
        storage.append(row)