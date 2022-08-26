import numpy as np

#puzzle
grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,0,0]]



#prints the grid 
#print(np.matrix(grid))

#possible solutions function
def possible(row, col, num):
  global grid
  
  #is the number appearing in the given row?
  for i in range (0,9):
    if grid[row][i] == num:
      return False
  
  #is the number appearing in the given column?
  for i in range (0,9):
    if grid[i][col] == num:
      return False
    
  
  #is the number appearing in the given square?
  
  #(col)starting point of square -> 0, 3 or 6
  x0 = (col //3 ) * 3
  #(row)starting point of square -> 0, 3 or 6
  y0 = (row //3 ) * 3
  
  for i in range(0,3):
    for j in range (0,3):
      if grid[y0+i][x0 + j] == num:
        return False
      
  #return True if the number is a possible solution
  return True


#backtracking function
def solvePuzzle():
  global grid
  for row in range(0,9):
    for col in range(0,9):
      #check if the box is empty
      if grid[row][col] == 0:
        #if the box is empty, then we need to check for possible solutions
        for num in range(1,10):
          if possible(row, col, num):
            #assign the num value to the box if it is a possible solution.
            grid[row][col] = num
            #continue solving. 
            solvePuzzle()
            #if we cannot keep solving(stuck) then we need to set it back to 0 
            grid[row][col] = 0
        return
      
  print("\n")
      
  print(np.matrix(grid))
  
  
  #maybe we have more than one solution, thus by pressing enter, we can see if we have more solutions. 
  input("More Possible Solutions(PRESS ENTER)")
solvePuzzle()
  
  
           
          
      
    

      
      
    
  
  
  
  
  
  
