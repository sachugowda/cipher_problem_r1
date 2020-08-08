#Python 3.0

open_list = ["[","{","("] 
close_list = ["]","}",")"] 
 
def pattern(myStr): 
    stack = [] 
    for i in myStr: 
        if i in open_list: 
            stack.append(i) 
        elif i in close_list: 
            pos = close_list.index(i) 
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])): 
                stack.pop() 
            else: 
                return "NO"
    if len(stack) == 0: 
        return "YES"
    else: 
        return "NO"
 #testinput
test1 = "[({})]"
test2 = "{(]}"
print("Test1: ",test1, "->", pattern(test1)) 
print("Test2: ",test2, "->", pattern(test2)) 
