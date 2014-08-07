import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()
maxMatrixSize = 10
# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    matrixName = record[0]
    row = record[1]
    col = record[2]
    v = record[3]

    for matrixSize in range(0,maxMatrixSize):
        if matrixName == 'a':
            mr.emit_intermediate((row,matrixSize), record)
        if matrixName == 'b':
            mr.emit_intermediate((matrixSize,col), record)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    a_mtx = {}
    b_mtx = {}
    for v in list_of_values:
        if v[0] == 'a':
            a_mtx[v[1],v[2]] = v[3]
        if v[0] == 'b':
            b_mtx[v[1],v[2]] = v[3]

    result = 0;
    found = False;
    for i in range(0,maxMatrixSize):
        if (key[0],i) in a_mtx.keys() and (i,key[1]) in b_mtx.keys():
            found = True;
            result = result + a_mtx[(key[0],i)] *b_mtx[(i,key[1])];

    if found == True:
        mr.emit((key[0],key[1], result))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
