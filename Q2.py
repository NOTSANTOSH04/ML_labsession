list=[]

n = int(input("Enter the number of elements in the list: "))

def list_input(list,n):
    for i in range(0,n):
        ele = int(input(f"Enter the {i+1} element: "))
        list.append(ele)
    return list
def range_list(list,n):
    if(n<=3):
        return "Range determination is not possible"
    else:
        list_input(list,n)
        Min = min(list)
        Max = max(list)
        return Max-Min
print(f"the range between largest and smallest number is : {range_list(list,n)}")


