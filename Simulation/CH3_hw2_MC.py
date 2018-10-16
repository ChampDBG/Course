# import package
import random, math
import matplotlib.pyplot as plt

def AimFunc(x):
    '''
    Calculate the result with input is x
     Input
      -x: the input of the function
     Output
      rst: the result with input is x
    '''
    rst = math.exp(x+pow(x,2))
    return rst

def GenData():
    '''
    Generate the data pair (x,y)
     Output
      -dta: the data pair (x,y), where -2 <= x <= 2, 0 <= y <= max(AimFunc(x))
    '''
    dta = [random.uniform(-2,2), random.uniform(0,AimFunc(2))]
    return dta

def SimProc(times):
    '''
    This function use to simulate whether data pair (x, y) is under the AimFunc.
     Input
      -times: executing times in one simulation
     Output
      -count: counting how many data pair (x,y) is under the AimFunc
    '''
    count = 0
    now = 0
    while now < times:
        rand_x, rand_y = GenData()
        y = AimFunc(rand_x)
        if rand_y <= y:
            count = count+1
        now = now+1
    return count

def SimInt(scale, order):
    '''
    Estimate the integral of AimFunc
     Input
      -scale & order: the parameter of executing times
     Output
      -est_int: the estimated integral result
    '''
    times = scale*pow(10, order)+1
    count = SimProc(times)
    est_int = (count/times)*(4*AimFunc(2))
    return est_int

# plot funciton
def PltFunc():
    seq = []
    seq_y = []
    for i in range(1001):
        seq.append(2*(i/500)-2)
        seq_y.append(AimFunc(2*(i/500)-2))
    plt.plot(seq, seq_y)
    plt.show()

## main
# parameter
times = int(input('Simulating points: '))
order = int(math.log10(times))
scale = pow(10, (math.log10(times)-order))
num_proc = int(input('Simulating times: '))
rst = []
for i in range(num_proc):
    print('No.' + str(i+1) + ' simulation')
    rst.append(SimInt(scale, order))

mean = sum(rst)/len(rst)
error = abs(mean - 93.1628)
print('Averaging %d simulations with %d points, result is %.10f, error is %.10f.' % (num_proc, times, mean, error))