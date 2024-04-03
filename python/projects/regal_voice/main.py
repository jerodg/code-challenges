SRC = [["H", "E", "H", "O", "L"], ["H", "L", "H", "E", "L"], ["E", "L", "O", "O", "E"], ["E", "L", "O", "H", "E"],
       ["H", "E", "H", "L", "L"]]
WD = len(SRC[0])
HT = len(SRC)
LN = WD if WD > HT else HT
ROWS = [-1, 0, 0, 1]
COLS = [0, 1, -1, 0]


def valid(row, col, prow, pcol):
    return (row >= 0) and (row < HT) and (col >= 0) and (col < WD) and not (row == prow and col == pcol)


def check(mat, row, col, prow, pcol, word, res, idx, n):
    if idx > n or mat[row][col] != word[idx]:
        return

    res += word[idx]
    if idx == n:
        print('res:', res)
        return res

    acc = []
    for i in range(len(ROWS)):
        if valid(row + ROWS[i], col + COLS[i], prow, pcol):
            if next_valid_letter := check(mat, row + ROWS[i], col + COLS[i], row, col, word, res, idx + 1, n):
                acc.append(next_valid_letter)
    return acc


def find_count(mat, word, n):
    res = []
    for i in range(HT):
        for j in range(WD):
            if mat[i][j] == word[0]:
                # print("Found H")
                if this_word := check(mat, i, j, -1, -1, word, '', 0, n):
                    res.append(this_word)

    print(*res, sep='\n')
    return len(res)


word = 'HELLO'
out = find_count(SRC, list(word), len(word) - 1)
print(out)

# def count_words(mat, word):
#     wrd = {x: 0 for x in word}
#     sum(x.count(

# count_words(SRC, list('HELLO')
