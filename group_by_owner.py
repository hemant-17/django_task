file_2_owner={
 'Input.txt': 'Randy',
 'Code.py': 'Stan',
 'Output.txt': 'Randy',
 'app.yml': 'Randy',
 }
 
def group_by_owners(dic):
    owner_2_file={}
    for key,value in dic.items():
        if value in owner_2_file:
            owner_2_file[value].append(key)
        else:
            owner_2_file[value]=[key]
            
    print(owner_2_file)
    
     
group_by_owners(file_2_owner)