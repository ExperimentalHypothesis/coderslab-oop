def middle_elements(sequences: list) -> list:
    result = []
    for sequence in sequences:
        if not sequence:
            continue
        middle_idx = len(sequence) // 2
        middle_elm = sequence[middle_idx]
        result.append(middle_elm)
    return result


class SequenceOfNumbers:
    def __init__(self, start, stop, step):
        self._data = range(start, stop, step)

    def __len__(self):
        return len(self._data)

    def __getitem__(self, idx):
        if idx < 0:
            raise IndexError
        return self._data[idx]


if __name__ == "__main__":

    a = SequenceOfNumbers(0, 10, 1)   # mid = 5
    b = SequenceOfNumbers(0, 110, 10) # mid = 50
    c = SequenceOfNumbers(14, 46, 4)  # mid = 3
    res = middle_elements([a, b, c])
    print(res)
