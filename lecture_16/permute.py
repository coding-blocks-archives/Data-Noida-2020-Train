def permute(processed, unprocessed):
    if len(unprocessed) == 0:
        print(processed)
        return

    for i in range(len(unprocessed)):
        ch = unprocessed[i]
        rec_unprocessed = unprocessed[:i] + unprocessed[i+1:]
        permute(processed + ch, rec_unprocessed)


permute("", "abc")



