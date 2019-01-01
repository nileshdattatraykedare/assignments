

def matmult(a, b):
    zip_b = zip(*b)
    return [[sum(ele_a * ele_b for ele_a, ele_b in zip(row_a, col_b))
             for col_b in zip_b] for row_a in a]

# unit test


X = [[1, 2, 3],
     [4, 5, 6]]

Y = [[1, 4],
     [2, 5],
     [3, 6]]

c = matmult(X, Y)

print c
# result [[14, 32], [32, 77]]
