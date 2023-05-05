import random

random_list=[]

for i in range(0,21):
    random_list.append(random.randint(1,100))
    
print("\n--------------------Random List------------------\n")
print(random_list)

order=input("Define the sorting type (ascending or descending): ")

for i in range(0,len(random_list)):
    for j in range(0,i):
        if order=="ascending":
            condition=(random_list[i]<=random_list[j])
        elif order=="descending":
            condition=(random_list[i]>=random_list[j])
            
        if condition:
            var=random_list[j]
            random_list[j]=random_list[i]
            random_list[i]=var
            
        
    

    
for k in range(0,len(random_list)):
    print(random_list[k])
