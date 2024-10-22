def addItem(items, key):
    if key in items:
        items[key] += 1
        return
    items[key] = 1
    return
