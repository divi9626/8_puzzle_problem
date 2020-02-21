import numpy as np
import queue 

       
print("Enter the entries in a single line (separated by space): ") 
  
    
entries = list(map(int, input().split())) 

    
# For printing the matrix 
initial_matrix = np.array(entries).reshape(3, 3) 
print(initial_matrix)


#goal matrix
def check_solvable(m):
    arr = np.reshape(m, 9)
    counter_state = 0
    for i in range(9):
        if not arr[i] == 0:
            check_element = arr[i]
            for x in range(i+1, 9):
                if check_element < arr[x] or arr[x] == 0:
                    continue
                else:
                    counter_state += 1
    if counter_state % 2 == 0:
        print("the puzzle is solvable, generating path")
    else:
        print("the puzzle is insolvable")
        
check_solvable(initial_matrix)

# function to find blank cell
def blanktile(mat):
    i,j = np.where(mat == 0)
    i = int(i)
    j = int(j)
    return (i,j)

def moveleft(mat):
    i, j = blanktile(mat)
    if j == 0:
        return None
    else:
        temp_mat = np.copy(mat)
        temp = temp_mat[i,j-1]
        temp_mat[i,j] = temp
        temp_mat[i,j-1] = 0
        
        return temp_mat
    
            
def moveright(mat):
    i, j = blanktile(mat)
    if j == 2:
        return None
    else:
        temp_mat = np.copy(mat)
        temp = temp_mat[i,j+1]
        temp_mat[i,j] = temp
        temp_mat[i,j+1] = 0
        
        return temp_mat
    
def moveup(mat):
    i, j = blanktile(mat)
    if i == 0:        
        return None
    else:
        temp_mat = np.copy(mat)
        temp = temp_mat[i-1,j]
        temp_mat[i,j] = temp
        temp_mat[i-1,j] = 0
        
        return temp_mat
    
def movedown(mat):
    i, j = blanktile(mat)
    if i == 2:
        return None
    else:
        temp_mat = np.copy(mat)
        temp = temp_mat[i+1,j]
        temp_mat[i,j] = temp
        temp_mat[i+1,j] = 0
        
        return temp_mat
        

    
def check_equal(A,B):
    for i in range(3):
        for j in range(3):
            if A[i][j] != B[i][j]:
                return False
    return True


    
def get_child_list(node):
    
    child_list = []
    
    action_up = moveup(node)
    if action_up is not None:
        child_list.append(action_up)        
    action_down = movedown(node)
    if action_down is not None:
        child_list.append(action_down)
    action_left = moveleft(node)
    if action_left is not None:
        child_list.append(action_left)        
    action_right = moveright(node)
    if action_right is not None:
        child_list.append(action_right)
        
    
        
    return child_list
    

q = queue.Queue()
index_q = queue.Queue()
visited = []
parent = []
q.put(initial_matrix)
index_q.put(1)
    
# main loop

child_parent_map = {1:0} 
state_map ={1:initial_matrix}
counter = 0
breakwhile = False
while (q.qsize() != 0) and not breakwhile:
    counter = counter + 1
    
    node = q.get()
    print(node)
    
    node_index = index_q.get()
    visited.append(node)
    child_list = get_child_list(node)
    
    latest_child_ind = np.max(list(child_parent_map.keys()))
    
    for i, state in enumerate(child_list):
        new_latest = latest_child_ind + i + 1
        child_parent_map[new_latest] = node_index
        
        state_map[new_latest] = state

        
    
    child_counter = 0
    for child in child_list:
        
        child_counter += 1
    
        
        if check_equal(child,matrix_goal) is True:
            breakwhile = True
            print('solved')
            solution_index = latest_child_ind + child_counter
            break
        else:
            child_not_found = True
            for visited_mat in visited:
                if check_equal(visited_mat,child):
                    child_not_found = False
                   
        if child_not_found:
            
            index_q.put(latest_child_ind + child_counter)
            q.put(child)
               
       
with open("Nodes.txt","w") as f1:
    for i in range(len(visited)):
        f1.write(str(visited))
        
    
print(counter)


# backtracking index
child_path = []
parent_path = []
parent = child_parent_map[solution_index]
child_index = solution_index
while parent != 0:
    
    child_path.append(child_index)
    parent_path.append(parent)
    child_index = parent
    parent = child_parent_map[child_index]
    
#child_path.reverse()
#parent_path.reverse()
print(child_path)
print(parent_path)

with open("NodesInfo.txt","w") as f1:
    for i in range(len(child_path)):
        f1.write(str(child_path))



state_list =[]
for index in child_path:
    state_variable = np.transpose(state_map[index])
    state_list.append(state_variable)
print(initial_matrix)
print(state_list)

            
def Convert(string): 
    li = list(string.split(" ")) 
    return li

for state_out in state_list:
    p = np.array2string(state_out)
    print(p)
    b = Convert(p)
    print(b)
    #p_prime = get_one_list(p)
    #print(p_prime)
    

with open("nodePath.txt", "w") as f:
    for i in range(len(state_list)):
        f.write(str(b))
    
    
    
       
          

 
















