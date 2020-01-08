
#This program runs solves a 8-puzzle (sliding puzzle) using the A* algorithm 

nodesVisited = 0
class Node:
    
    def __init__(self,data,level,fval):
    #initialize node
        self.data = data
        self.level = level
        self.fval = fval
    
    def generate_child(self):
    #generate children nodes by moving the blank space up (denoted by 0) up, down, left, or right
        global nodesVisited
        x,y = self.find(self.data,'0')
        
        val_list = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]] #position value for moving the blank in a given direction
        children = []
        for i in range(4):
            child = self.shuffle(self.data,x,y,val_list[i][0],val_list[i][1])
            if child is not None:
                child_node = Node(child,self.level+1,0)
                children.append((child_node,i))
                nodesVisited+=1
        return children
        
    def shuffle(self,puz,x1,y1,x2,y2):
        """ Move the blank space in the given direction and if the position value are out
            of limits the return None """
        if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data):
            temp_puz = []
            temp_puz = self.copy(puz)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            return temp_puz
        else:
            return None
            

    def copy(self,root):
        """ Copy function to create a similar matrix of the given node"""
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp    
    
    #this function is used to find the position of the blank        
    def find(self,puz,x):
        for i in range(0,len(self.data)):
            for j in range(0,len(self.data)):
                if puz[i][j] == x:
                    return i,j


class Puzzle:
    def __init__(self,filename):
        # Initializing, puzzle size here is set to 3, open and closed lists are set as empty
        self.n = 3
        self.open = []
        self.closed = []
        self.filename = filename

    def accept(self):
        #accepts puzzle from user
        puz = []
        for i in range(0,self.n):
            temp = input().split(" ")
            puz.append(temp)
        return puz

    def f(self,start,goal):
        #Function to calculate hueristic value f(x) = h(x) + g(x) 
        return self.h(start.data,goal)+start.level

    def h(self,start,goal):
        #calulcate difference between puzzles
        temp = 0
        for i in range(0,self.n):
            for j in range(0,self.n):
                if start[i][j] != goal[i][j] and start[i][j] != '0':
                    temp += 1
        return temp
        

    def process(self):
        global nodesVisited
        moveCounter = 1
        moves = {-1:'',0:'left',1:'right',2:'up',3:'down'}
        
        start = read_file(self.filename)
        goal = [['0','1','2'],['3','4','5'],['6','7','8']]

        start = Node(start,0,0)
        start.fval = self.f(start,goal)
        
        """this is where we print the output, showing first the starting position
            and then each position along with moves taken to get to the correct goal positon"""
        print('START')
        self.open.append((start,-1))
        while True:
            cur = self.open[0][0]
            if self.open[0][1]!=-1:
                print('move',moveCounter,'ACTION:',moves[self.open[0][1]])
                moveCounter+=1
            for i in cur.data:
                for j in i:
                    print(j,end=" ")
                print("")
            if(self.h(cur.data,goal) == 0):
                break
                
            for i in cur.generate_child():
                i[0].fval = self.f(i[0],goal)
                self.open.append(i)
            self.closed.append(cur)
            del self.open[0]

            #sort open list based on f value
            self.open.sort(key = lambda x:x[0].fval,reverse=False)
        print ('')
        print('Number of states visited = ',nodesVisited-2) #Subtracting two nodes start and end   

def read_file(filename):
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    board = [];
    for lines in content:
        board.append(lines.split(' '))
    return board    
        
if __name__ == "__main__":    
    filename = 'mp1input2.txt'  #text file to read as given in assignment, change as needed
    puz = Puzzle(filename)
    puz.process()