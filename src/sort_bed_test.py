# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_


from sort_bed import (
    sort_file,
)

def test_sort(x):
    for i in range(len(sort_file(x))):
        assert sort_file(list)[i][0] <=  sort_file(list)[i+1][0] and sort_file(list)[i][1] <= sort_file(list)[i+1][1] == True
