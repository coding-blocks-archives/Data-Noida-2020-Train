def subseq(processed, unprocessed):

    if len(unprocessed) == 0:
        print(processed)
        return

    ch = unprocessed[0]

    subseq(processed + ch, unprocessed[1:])
    subseq(processed, unprocessed[1:])


def ret_subseq(processed, unprocessed):

    if len(unprocessed) == 0:
        if len(processed) == 0:
            return []
        return [processed]

    ch = unprocessed[0]

    acc = []
    acc.extend(ret_subseq(processed + ch, unprocessed[1:]))
    acc.extend(ret_subseq(processed, unprocessed[1:]))

    return acc


def count_subseq(processed, unprocessed):

    if len(unprocessed) == 0:
        return 1

    ch = unprocessed[0]

    left = count_subseq(processed + ch, unprocessed[1:])
    right = count_subseq(processed, unprocessed[1:])

    return left + right


print(ret_subseq("", "abc"))