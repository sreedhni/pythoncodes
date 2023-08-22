# pattern matching
# regular expression that specifies a set of strings that matches it
# re.search(patter,string)

# python variable creation rule

# startting with an alphabet
# no length limit
# _ only allowed

rule="[a-z,A-Z][_,A-Z,a-z,0-9]"

# methods
  # search()
  # sub()
  # findall()
  # fullmatch()
#  import the fn 
# from re import* (* indicate all the methods are imported )

# rules
# [a-z]-/w
# [0-9]- /d
# space- /s
#  /D (expect alphabet)(^[a-z])

# quantity filter
# a* >> any nmbr of a may be zero a 
#a{2} >> 2 times a
#a{2,3} >>a minumum 2 times maximum 3 times


