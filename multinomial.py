import random

def multinomial_sample(n,p,k=1):  
    '''                                                                 
    Return samples from a multinomial distribution.                     
                                                                        
    n:= number of trials                                                
    p:= list of probabilities                                           
    k:= number of desired samples                                       
    '''
    assert type(n)==int
    assert type(p)==list
    assert sum(p)==1
    total_output = []
    for i in range(k):
        trial_output = [0]*len(p)
        for m in range(n):
            num = random.random()
            j = 0
            while (num>0):
                num -= p[j]
                j += 1
            trial_output[j-1] += 1
        total_output.append(trial_output)


    return total_output
    

# def main():
#     print(multinomial_sample(10,[1/3,1/3,1/3],k=10))
#     return 0

# main()