Given an NxN matrix (nested list), print the NW to SE diagonal values on a new line, starting from the NE most corner down to the SW most corner.  For example:

input:

    M = [
    [95,  2, 46, 74, 21],
    [78, 62, 61, 81, 30],
    [49, 97, 84, 72,  0],
    [71,  2,  2, 76, 34],
    [93,  0, 67, 99, 54]
    ]

output:

    21
    74 30
    46 81  0
     2 61 72 34
    95 62 84 76 54
    78 97  2 99
    49  2 67
    71  0
    93