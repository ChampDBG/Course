# import package
import random, math

def GenDataPair():
    '''
    To generate the data pair (x,y) with the value between 0 and 1.
     Output
      -dta: The data pair (x, y)
    '''
    dta = [random.uniform(0,1), random.uniform(0,1)]
    return dta

def SimProc(times):
    '''
    This function use to simulate whether data pair (x, y) is inside the circle with radius is 1.
     Input
      -times: Executing times in one simulation.
     Output
      -count: Counting how many data pair (x, y) is inside the circle.
    '''
    count = 0
    now = 0
    while now<times:
        x, y = GenDataPair()
        if (pow(x,2)+pow(y,2)) < 1:
            count = count+1
        now = now+1
    return count

def SimPI(scale, order):
    '''
    This function is used to estimate the value of pi
     Input
      -scale & order: The parameter of executing times
     Output
      -est_pi: The estimated value of pi
    '''
    times = scale*pow(10, order)+1
    count = SimProc(times)
    est_pi = (count/times)*4
    return est_pi

## main
# parameter
times = int(input('Simulating points: '))
order = int(math.log10(times))
scale = pow(10, (math.log10(times)-order))
num_proc = int(input('Simulating times: '))

rst = []
for i in range(num_proc):
    print('No.' + str(i+1) + ' simulation')
    rst.append(SimPI(scale, order))

mean = sum(rst)/len(rst)
error = abs(mean - math.pi)
print('Averaging %d simulations with %d points, result is %.10f, error is %.10f.' % (num_proc, times, mean, error))