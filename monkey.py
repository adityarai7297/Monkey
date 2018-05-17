
health = 2000
injury = 1
with open("input.txt", 'rb') as f1:
    input_lines = f1.readlines()


input_list=[] #this will contain data parsed from input.txt file

for line in input_lines:
    input_list.append(int(line))



maximum=0
num = input_list[0] #first entry gives number of monkeys
                    #subsequent entries i.e input_list[1],input_list[2]......give damage value of monkey

pos = 0   # pos = 1 means after 1st monkey pos = 2 means after 2nd monkey and so on
while pos<=num:
    health = 2000
    injury = 1
    m=0
    for x in range(1,num+1):
        if(health != 0 and injury != 1000000):
            health = health - input_list[x]
            injury = injury*input_list[x]
            print()
            m=m+1
            if(m>maximum):
                maximum=m   # maximum monkeys defeated
                max_pos=pos # position from which maximum monkeys defeated
            
 
        else:
            pos=pos+1
            
            break
 
 
        if(x==num):
            
            break


print("We need to start after ",max_pos," monkey and opt out after defeating ",maximum)
