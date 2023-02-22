ip_list = [('a','aa',1),('b','bb',2),('c','cc',3)]
op_list=[]
li2=[]
for i in range(len(ip_list)):
    li=[]
    for x in range(len(ip_list[i])):
        if type(ip_list[i][x])!=int and len(ip_list[i][x])>1:
            if ip_list[i][x][0]!=ip_list[i][x][1]:
                li=li+[ip_list[i][x]]
        if type(ip_list[i][x])!=int and len(ip_list[i][x])==1:
            li=li+[ip_list[i][x]]
        if type(ip_list[i][x])==int:
            li=li+[(ip_list[i][x])**2]        
    xy=tuple(li)
    op_list.append(xy)
print(op_list)
                
                

