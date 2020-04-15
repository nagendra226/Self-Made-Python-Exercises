class Matrix:
    '''
    This Program and Module is a Matrix File.
    You can generate add 2X2 Matix
    3X2 Matrix
    4x2 Matrix
    '''

    def add_twobytwo_matrix(self, matrix1, matrix2):
        '''
        :param matrix1:  list with 2*2 matrix [[a1,b1],[x1,y1]]  = [[1,2],[2,3]]
        :param matrix2:  list with 2*2 matrix [[a2,b2],[x2,y2]]  = [[2,3],[4,4]]
        :return:2*2 matrix with sum [[a1+a2,b1+b2],[x1+x2,y1+y2]]= [[3,5],[6,7]]
        '''

        # return a new list result matrix
        result_matrix = list()

        # check the length of each matrix
        if len(matrix1[0]) == 2 and len(matrix1[1]) == 2 and len(matrix2[0]) == 2 and len(matrix2[1]) == 2:
            try:
                for m, (i, j) in enumerate(matrix1):
                    for n, (k, l) in enumerate(matrix2):
                        if m == n:
                            result_matrix.append([i + k, k + l])
            except TypeError as err:
                return "Please enter only numbers either natural or whole or integers"
        else:
            raise ValueError("Given matrices are not the same size.")

        return result_matrix

    def add_threebytwo_matrix(self, matrix1, matrix2):
        '''
        :param matrix1:  list with 2*2 matrix [[a1,b1,c1],[x1,y1,z1]]    = [[1,2,3],[2,3,4]]
        :param matrix2:  list with 2*2 matrix [[a2,b2,c2],[x2,y2,z2]]    = [[2,3,4],[4,4,4]]
        :return:2*2 matrix with [[a1+a2,b1+b2,c1+c2][x1+x2,y1+y2,z1+z2]] = [[3,5,7],[6,7,8]]
        '''

        # return a new list result matrix
        result_matrix = list()

        # check the length of each matrix
        if len(matrix1[0]) == 3 and len(matrix1[1]) == 3 and len(matrix2[0]) == 3 and len(matrix2[1]) == 3:
            try:
                for a, (i, j, k) in enumerate(matrix1):
                    for b, (l, m, n) in enumerate(matrix2):
                        if a == b:
                            result_matrix.append([i + l, j + m, k + n])
            except TypeError as err:
                return "Please enter only numbers either natural or whole or integers"
        else:
            raise ValueError("Given matrices are not the same size.")

        return result_matrix

    def add_fourbytwo_matrix(self, matrix1, matrix2):
        '''
        :param matrix1:  list with 2*2 matrix [[a1,b1,c1,d1],[w1,x1,y1,z1]]      = [[1,2,3,1],[2,3,4,1]]
        :param matrix2:  list with 2*2 matrix [[a2,b2,c2,d2],[w2,x2,y2,z2]]      = [[2,3,4,1],[4,4,4,4]]
        :return:2*2 matrix [[a1+a2,b1+b2,c1+c2,d1+d2],[w1+w2,x1+x2,y1+y2,z1+z2]] = [[3,5,7,2],[6,7,8,5]]
        '''

        # return a new list result matrix
        result_matrix = list()

        # check the length of each matrix
        if len(matrix1[0]) == 4 and len(matrix1[1]) == 4 and len(matrix2[0]) == 4 and len(matrix2[1]) == 4:
            try:
                for a, (i, j, k, l) in enumerate(matrix1):
                    for b, (m, n, o, p) in enumerate(matrix2):
                        if a == b:
                            result_matrix.append([i + m, j + n, k + o, l + p])
            except TypeError as err:
                return "Please enter only numbers either natural or whole or integers"
        else:
            raise ValueError("Given matrices are not the same size.")

        return result_matrix
