
row = [-1, 0, 0, 1]
col = [0, -1, 1, 0]
def isValid(mat,x,y,target):
    return (0<=x<M and 0<=y<N) and mat[x][y]==target
def dfs(mat,x,y,replace):
    target=mat[x][y]
    mat[x][y]=replace
    
    for k in range(4):
        if isValid(mat,x+row[k],y+col[k],target):
            dfs(mat,x+row[k],y+col[k],replace)
        
def replace(mat):
    (M,N)=(len(mat),len(mat[0]))
    
    for i in range(N):
        if mat[0][i]==0:
            dfs(mat,0,i,-1)
        if mat[M-1][i]==0:
            dfs(mat,M-1,i,-1)
            
    for i in range(N):
        if mat[i][0]==0:
            dfs(mat,i,0,-1)
        if mat[i][N-1]==0:
            dfs(mat,i,N-1,-1)
            
    for i in range(M):
        for j in range(N):
            if mat[i][j]==0:
                mat[i][j]=1
                
            if mat[i][j]==-1:
                mat[i][j]=0
            

if __name__ == '__main__':
     
    mat = [
        [1, 1, 1, 1, 0, 0, 1, 1, 0, 1],
        [1, 0, 0, 1, 1, 0, 1, 1, 1, 1],
        [1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 1, 1, 0, 1],
        [0, 0, 1, 1, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 1, 1, 0, 1, 1, 0, 0],
        [1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 0, 0, 1, 0, 1],
        [1, 1, 1, 0, 1, 0, 1, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1]
    ]
 
    # size of a given matrix is `M × N`
    M = N = 10
 
    replace(mat)
 
    # print matrix
    for r in mat:
        print(r)
 