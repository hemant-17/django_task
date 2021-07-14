import math
import cmath

def find_roots(a,b,c):
    
    #calculating discriminant (b^2 -4ac)
    disc=(b*b)-(4*a*c)
    
    #If discriminant==0 then roots are same and equal
    if disc==0:
        root = ( -b + (math.sqrt(disc)))/(2*a)
        root=round(root,3)
        return (root,root)
    
    #If discriminant>0 then roots are real and unequal
    elif disc>0:
        #Calculating roots and rounding off upto 3 decimal places
        root1 = ( -b + (math.sqrt(disc)))/(2*a)
        root1=round(root1,3)
        
        root2 = ( -b - (math.sqrt(disc)))/(2*a)
        root2=round(root2,3)
        return (root1,root2)
        
    #If discriminant <0 then roots are complex
    else:
        root1 = (-b + cmath.sqrt(disc))/ (2*a)
        
        root2 = (-b - cmath.sqrt(disc))/ (2*a)
        return (root1,root2)

#For Real and Equal roots        
print(find_roots(9,-12,4))

#For real and unequal roots
print(find_roots(2,-9,4))

#For complex roots
print(find_roots(2,5,4))