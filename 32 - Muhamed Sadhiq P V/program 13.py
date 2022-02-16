import numpy
matrix1=numpy.matrix1([[1,2,3],[4,5,6],[7,8,9]])
matrix2=numpy.matrix2([[10,11,12],[13,14,15],[16,17,18]])
# Matrix Addition
matrix3=numpy.add(matrix1,matrix2)
print("matrix after addition")
print(matrix3)
# Matrix Subtraction
matrix4=numpy.subtract(matrix1,matrix2)
print("matrix after subtraction")
print(matrix4)
# Matrix Multiplication
matrix5=numpy.matmul(matrix1,matrix2)
print("matrix after multiplication")
print(matrix5)
# Scalar Multiplication
matrix6=2*matrix1
print("matrix1 after scalar multiplication")
print(matrix6)
# Matrix Transpose
matrix7=numpy.transpose(matrix1)
print("matrix1 after transpose")
print(matrix7)
