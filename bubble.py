# Bubble algorithms 
#الترتيب سيكون تصاعديا
def bubble (b_list):
    sort = False
    while sort == False :
        sort = True
        for i in range (0,len(b_list)-1):
            if b_list[i] > b_list[i+1]:
                b_list[i], b_list[i+1] = b_list[i+1], b_list[i]
                sort = False
    return b_list

print (bubble([4,7,9,1,0,4,7,6,2]))






