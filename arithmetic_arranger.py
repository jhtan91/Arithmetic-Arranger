#This is a program to arrange the arithmetic calculation.

import numpy as np

def arithmetic_arranger(problems,reveal_ans=None):
    
    #problems is a variable with strings.
    upper_problems_f=[]*len(problems)
    expression_problems=[]*len(problems)
    lower_problems=[]*len(problems)
    lower_problems_f=[]*len(problems)
    lines="-"
    total_ans_lines_f=[]
    total_space=[]
    total_space_f=[]
    
    #Check if the number of problems are more than 5.
    if len(problems)>5:
        arranged_problems="Error: Too many problems."
        
        return arranged_problems
    
    else:
        pass
    
    #Start the loop to join the strings from upper part to upper_problems,
    #operators to expression_problems, and lower part to lower_problems.
    i=0
    
    for max_numbers in problems:
        split_problems = problems[i].split(" ")
        x=split_problems[0]
        y=split_problems[1]
        z=split_problems[2]
        total_ans_lines=[]
        
        #Check if digits more than 4 for both top and bottom operands
        if len(x)>4:
            arranged_problems="Error: Numbers cannot be more than four digits."
            
            return arranged_problems
            
        elif len(z)>4:
            arranged_problems="Error: Numbers cannot be more than four digits."
            
            return arranged_problems
        
        #If the value contain none digits, go to except.
        #If the integer of the top or bottom cannot be added, go to except.    
        try:
            a = int(x)
            a+=1
            b = int(z)
            b+=1
        
        except:
            arranged_problems="Error: Numbers must only contain digits."
            
            return arranged_problems
        
        #Make space for longest numbers
        #For x > z
        if len(x)>len(z):
            
            u_space=2
            l_space=len(x)-len(z)+1
            num_lines=len(x)+2
            
            #Check operands and do operation
            if y=="+":
                
                total=int(x)+int(z)
                
            elif y=="-":
                
                total=int(x)-int(z)
                
            elif y=="x" or y=="/":
            
                arranged_problems="Error: Operator must be '+' or '-'."
                
                return arranged_problems
        
        #For x==z
        elif len(x)==len(z):
        
            u_space=2
            l_space=1
            num_lines=len(x)+2
            
            #Check operands and do operation
            if y=="+":
                
                total=int(x)+int(z)
                
            elif y=="-":
                
                total=int(x)-int(z)
                
            elif y=="x" or y=="/":
            
                arranged_problems="Error: Operator must be '+' or '-'."
                
                return arranged_problems
            
        #For x<z
        else:
        
            u_space=len(z)-len(x)+2
            l_space=1
            num_lines=len(z)+2
        
            #Check operands and do operation
            if y=="+":
                
                total=int(x)+int(z)
                
            elif y=="-":
                
                total=int(x)-int(z)
                
            elif y=="x" or y=="/":
            
                arranged_problems="Error: Operator must be '+' or '-'."
                
                return arranged_problems
        
        #Empty spaces in front of answer = number of lines - length of string of answer
        ans_space = num_lines - len(str(total))
        
        #Join the strings with empty spaces in front
        total_space="".join((" "*ans_space,str(total)))
        upper_problems="".join((" "*u_space,x))
        lower_problems="".join((y," "*l_space,z))
        total_ans_lines="".join((lines*num_lines))
        
        #Append the strings into the designated array
        upper_problems_f.append(upper_problems)
        lower_problems_f.append(lower_problems)
        total_ans_lines_f.append(total_ans_lines)
        total_space_f.append(total_space)
        
        i=i+1
        
        #End of loop
    
    #Ensure 4 spaces between each problems.
    upper_problems_ff=('    '.join(upper_problems_f))
    lower_problems_ff=('    '.join(lower_problems_f))
    total_ans_lines_ff=('    '.join(total_ans_lines_f))
    total_space_ff=('    '.join(total_space_f))
    
    #Check if the optional argument exists to reveal the answer.
    if reveal_ans == True:
        arranged_problems=upper_problems_ff+"\n"+lower_problems_ff+"\n"+total_ans_lines_ff+"\n"+total_space_ff
    
    else:
        arranged_problems=upper_problems_ff+"\n"+lower_problems_ff+"\n"+total_ans_lines_ff
    
    return arranged_problems
    
print(arithmetic_arranger(['320 - 698', '1 - 3801', '4512 - 4', '123 - 49', '988 + 40'],True))
