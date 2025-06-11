a = ~12
print(a)
"-13"

"""
Note : But how ? ~ titled symbol did 2's complement of the given value which is 12 2's complement is -13 because our system
doesn't store negative values right.

2's Complement Steps : (-13 how comes for ~12)
        1.1's Complement : 
             (13) ->   0 0 0 0 1 1 0 1 
             After one's complement - >  1 1 1 1 0 0 1 0

        2.2's Complement : 
                1 1 1 1 0 0 1 0
                              1
                ---------------
                1 1 1 1 0 0 1 1  -> 2's Complement of 13

Final Steps :
        1's Complement of Given value (0 0 0 0 1 1 0 0 -> 1 1 1 1 0 0 1 1) =  2's Complement of Output Value
        Both are same. 
"""

a = 12 & 13
print(a)
"12"

"""
Note : Why 12 is the answer for the above ? what did & operator ?

Explanation : 
        1.Find out both number binary format
            12 -> 0 0 0 0 1 1 0 0
            13 -> 0 0 0 0 1 1 0 1
        2.Use AND operation of both
                  0 0 0 0 1 1 0 0
                  0 0 0 0 1 1 0 1
                  ---------------
                  0 0 0 0 1 1 0 0

"""

a = 12 | 13
print(a)
"13"

"""
Note : Why 13 is the answer for the above ? what did | operator ?

Explanation : 
        1.Find out both number binary format
            12 -> 0 0 0 0 1 1 0 0
            13 -> 0 0 0 0 1 1 0 1
        2.Use OR operation of both
                  0 0 0 0 1 1 0 0
                  0 0 0 0 1 1 0 1
                  ---------------
                  0 0 0 0 1 1 0 1
"""

A = 12 ^ 13
print(A)
"1"

"""
Note : Why 1 is the answer for the above ? what did ^ operator ?

Explanation : 
        1.Find out both number binary format
            12 -> 0 0 0 0 1 1 0 0
            13 -> 0 0 0 0 1 1 0 1
        2.Use XOR operation of both ( if same = 0 , otherwise it is 1)
                  0 0 0 0 1 1 0 0
                  0 0 0 0 1 1 0 1
                  ---------------
                  0 0 0 0 0 0 0 1
"""

a = 10 << 2
print(a)
"40"

"""
Note : Why 40 is the answer for the above ? what did << operator ?

Explanation : 
        1. 10 -> 0 0 0 0 1 0 1 0
        2. After ending consider 0 0 0 0 1 0 1 0.0 0 0 0 0 0 0 0 just like that 
        3. Left shift did shift the bit from right to left which the . after 0 0 is comes to the left
        4. Answer is 0 0 1 0 1 0 0 0 which is 40.
"""

a = 10 >> 2
print(a)
"2"

"""
Note : Why 2 is the answer for the above ? what did >> operator ?

Explanation : 
        1. 10 -> 0 0 0 0 1 0 1 0
        2. After ending consider 0 0 0 0 1 0 1 0.0 0 0 0 0 0 0 0 just like that 
        3. Right shift did shift the bit from left to right which the . Before value is comes to the Right.
        4. Answer is 0 0 0 0 0 0 1 0 which is 2.
"""