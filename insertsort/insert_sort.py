def insertion_sort(d):
    data = d.copy()
    for i in range(1,len(data)):   
        
        j = i                    
        
        key = data[j]            
        while j > 0 and key < data[j-1]: 
            data[j] = data[j-1] 
            j-=1 
        data[j] = key
    return data