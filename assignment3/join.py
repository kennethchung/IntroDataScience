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

    order_id = record[1]
    dict = {}
    #dict[1] = [1,2]
    dict[1] =[];
    dict[1].append(3)
    #print dict[1]
    mr.emit_intermediate(order_id, record)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts

    jointables = {}
    for v in list_of_values:
        if v[0] not in  jointables.keys():
            jointables[v[0]] = []
        jointables[v[0]].append(v)

    for o1 in jointables['order']:
        for l1 in jointables['line_item']:
            result = o1+l1
            mr.emit(result)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
