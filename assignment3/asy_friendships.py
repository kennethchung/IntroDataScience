import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    name = record[0]
    friend = record[1]
    mr.emit_intermediate((name,friend), 1)
    mr.emit_intermediate((friend,name), -1)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts

    count = 0
    for v in list_of_values:
        count = count+v
    if count == 1 or count == -1:
        mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
