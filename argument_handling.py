import sys 
i = 1
result = ""


while i < len(sys.argv):
    result = result + " " +(sys.argv[i] + " ")*i
    i = i + 1
print result

