#prompts user to create an nxm matrix, and then performs Ordinary Least Squares on that matrix
#beta_hat = (X^T*X)^-1*X^T*y

def get_OLS():
    n=(input("Enter the matrix size in the format m,n: \n"))
    n = re.split(',',n)
    shape = (int(n[0]),int(n[1]))
    Design_Matrix = np.array(input("Enter " + str(int(n[0])*int(n[1])) + " values for the design matrix by row, separated by commas \n" ).split(',')).reshape(shape)


    Design_Matrix = Design_Matrix.astype(int)
    print(Design_Matrix)

    if np.linalg.det(np.matmul(Design_Matrix.T, Design_Matrix)) == 0:
        print("Singular Matrix Error: (X.T * X) is uninvertable")
        return

    v = input("Enter a " + str(n[0]) + " dimension response vector, separated by commas \n")
    v = re.split(',',v)
    Response_Vector = []
    for i in v:
        Response_Vector.append(int(i))
    if len(Response_Vector) != int(n[0]):
        print("incorrect length for Response Vector")
        return
    
    do_OLS(Design_Matrix, Response_Vector)
    

def do_OLS(Design_Matrix, Response_Vector):
    OLS = np.matmul(Design_Matrix.T, Design_Matrix)
    OLS = np.asmatrix(OLS)
    
    if np.size(OLS) != 1:
        OLS = np.matmul(OLS.I,Design_Matrix.T)
    else:
         OLS = np.matmul(OLS,np.asmatrix(Design_Matrix.T))
       
    OLS = np.matmul(OLS, np.asmatrix(Response_Vector).T)
    print(OLS)
    return OLS
get_OLS()
