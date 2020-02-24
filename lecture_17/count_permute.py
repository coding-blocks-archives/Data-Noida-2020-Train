def permute(processed, unprocessed):

    if len(unprocessed) == 0:
        return 1

    acc = 0
    for i in range(len(unprocessed)):
        ch = unprocessed[i]
        rec_unprocessed = unprocessed[:i] + unprocessed[i+1:]
        acc += permute(processed + ch, rec_unprocessed)

    return acc


print(permute("", "abc"))
