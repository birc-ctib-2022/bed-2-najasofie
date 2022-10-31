# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

from bed import BedLine

from sort_bed import (
    sort_file,
)

from bed import (
    Table
)


#f = open("data/input.bed")


#def test_sort():
#    for i in range(len(sort_file(f))):
#        assert sort_file(f)[i][0] <=  sort_file(f)[i+1][0] and sort_file(f)[i][1] <= sort_file(f)[i+1][1] == True


def test_1984():
    assert 2 + 2 == 4

#def test_sort():
#    bedlines = [
#        BedLine(chrom='chr1', chrom_start=20100, chrom_end=20101, name='foo'),
#        BedLine(chrom='chr1', chrom_start=600, chrom_end=601, name='baz')
#        ]
#    expected = [
#        BedLine(chrom='chr1', chrom_start=600, chrom_end=601, name='baz'),
#        BedLine(chrom='chr1', chrom_start=20100, chrom_end=20101, name='foo')
#        ]
#    assert sort_file(bedlines) == expected