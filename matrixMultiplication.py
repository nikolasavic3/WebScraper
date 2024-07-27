import sys

def saveMatrixToFile(matrix, output_file):
    with open(output_file, "w") as f:
        for row in matrix:
            f.write(" ".join([str(val) for val in row]) + "\n")
                
def multiplyMatricies(matricies):
    normal_matricies = []
    n_rows_1, n_columns_1 = matricies[0]["shape"]
    n_rows_2, n_columns_2 = matricies[1]["shape"]
    if n_columns_1 != n_rows_2:
        print("It is not possible to muliply matricies.\nNumber of rows in 1. Matrix needs to be the same as number of columns in 2.Matrix")
        exit()
    for id in range(2):
        rows, columns = matricies[id]["shape"]
        matrix = [[0]*columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                if (i, j) in matricies[id]["data"]:
                    matrix[i][j] = int(matricies[id]["data"][(i,j)])

        print(f"{id+1}. Matrix:")
        print(matrix)
        normal_matricies.append(matrix)
        #row of m1 must be col len m2
    matrix = [[0]*n_columns_2 for _ in range(n_rows_1)]
    for i in range(n_rows_1):
        for j in range(n_columns_2):
            for k in range(n_columns_1):
                matrix[i][j] += normal_matricies[0][i][k] * normal_matricies[1][k][j]
    print("1. Matrix * 2. Matrix =")
    print(matrix)
    return matrix


def printMatricies(matricies):
    print("Matrix Dimensions: " + str(matricies[0]["shape"]))
    [print(f"{key}  {matricies[0]["data"][key]}") for key in matricies[0]["data"]]
    print("Dimensions: "+str(matricies[1]["shape"]))
    [print(f"{key}  {matricies[1]["data"][key]}") for key in matricies[1]["data"]]

def readFile(input_file_path):
     with open(input_file_path, "r") as f_in:
        matricies = []
        data = f_in.read()
        rows = data.split("\n")
        num_r, num_c = rows[0].split(" ")
        matrix = {"shape": (int(num_r), int(num_c)), "data": {}}
        for r in rows[1:]:
            row = r.split(" ")
            if len(row) == 3: # row, col, val
                r, c, v = row
 
                matrix["data"][(int(r), int(c))] = v
            if len(row) == 2: 
                matricies.append(matrix)
                num_r, num_c = row
                matrix = {"shape": (int(num_r), int(num_c)), "data": {}}
        matricies.append(matrix)
        printMatricies(matricies)
        return matricies
        
                

def main():
    if len(sys.argv) < 2:
        print("Usage: zadatak1.py <input_file>.txt <output_file>.txt")
        exit(1)
    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    [matrix1, matrix2] = readFile(input_file_path)
    matrix = multiplyMatricies([matrix1, matrix2])
    saveMatrixToFile(matrix, output_file_path)
    
if __name__ == "__main__":
    main()
