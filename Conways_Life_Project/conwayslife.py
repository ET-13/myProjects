import sys, argparse
import numpy as np
import matplotlib.pyplot as mplt
import matplotlib.animation as animation
counter = 1
if counter == 1:
#imshow from matplotlib represents a matrix of numbers as an image
    #a cell being alive and dead will be between 255(Alive) & 0(Dead)
    ON = 255
    OFF = 0
    vals = [ON, OFF]

    def randomizedGrid(N):
        #makes a n*n grid of random values
        return np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N)

    #x = np.array([[0,0,255], [255,255,0], [0,255,0]]) #2D numpy array of shape(3,3)
    #mplt.imshow(x, interpolation='nearest') #display matrix values as image, interpolation for sharp images
    #np.random.choice([0,255], 4*4, p=[0.1,0.9]).reshape(4,4) #random choice method, then voncert from 1D array to 2D array

    def addGlider(i,j,grid):
        glider = np.array([[0, 0,  255], [255,  0,  255], [0,  255,  255]])
        
        grid[i:i+3, j:j+3] = glider

    def update(frameNum, img, grid, N):
        #copy grid, 8 neighbors for calculation, traverse line by line
        newGrid = grid.copy()
        for i in range(N):
            for j in range(N):
                #pacman-like boundary conditions, have to consider what the edge cells respond to
                total = int((grid[i,(j-1)%N] + grid[i, (j+1)%N] + grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                            grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] + grid[(i+1)%N, (j-1)%N] + 
                            grid[(i+1)%N, (j+1)%N])/255)
                if grid[i,j] == ON: #apply rules
                    if (total < 2) or (total > 3):
                        newGrid[i, j] = OFF
                     
                    else: 
                        if total == 3:
                            newGrid[i, j] = ON

        #update data     
        img.set_data(newGrid)
        grid[:] = newGrid[:]
        return img


    def main():
        #command line args
        parseargs = argparse.ArgumentParser(description="Run Conway's Life Simulation")
        
        parseargs.add_argument('--grid.size', dest='N', required=False)
        parseargs.add_argument('--mov-file', dest='movfile', required=False)
        parseargs.add_argument('--interval', dest='interval', required=False)
        parseargs.add_argument('--glider', action='store_true', required=False)
        parseargs.add_argument('--gosper', action='store_true', required=False)
        args = parseargs.parse_args()

        #set grid size
        N=100
        if args.N and int(args.N) > 8:
            N = int(args.N)

        #set animation update interval

        updateInterval = 1000
        if args.interval:
            updateInterval=int(args.interval)

        #declare a grid

        grid = np.array([])
        #check glider

        if args.glider:
            grid = np.zeros(N*N).reshape(N, N)
            addGlider(1, 1, grid)
        else:
            #populate grid with random off/on
            grid = randomizedGrid(N)
        
        #animate
        fig, ax = mplt.subplots()
        img = ax.imshow(grid, interpolation='nearest')
        ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, ), frames=10, interval=updateInterval, save_count=50)

        if args.movfile:
            ani.save(args.movfile, fps=100, extra_args=['-vodec', 'libx264'])

        mplt.show()


    if __name__ == '__main__':
        main()













                        

                
            


    #mplt.show()