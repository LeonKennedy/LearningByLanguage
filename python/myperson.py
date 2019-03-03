import math

def myPerson(v1, v2):
    avg1 = sum(v1)/len(v1)
    avg2 = sum(v2)/len(v2)
    psum = 0
    for i in range(len(v1)):
  	    psum += (v1[i] - avg1) * (v2[i] - avg2)
    den1 = math.sqrt(sum([ pow((v-avg1),2) for v in v1]))
    den2 = math.sqrt(sum([ pow((v-avg2),2) for v in v2]))
    return psum/(den1 * den2)

    

if __name__ == "__main__":
    v1 = [1.0, 1.0, 2.0, 2.0, 3.0]
    v2 = [2.0, 2.0, 3.0, 3.0, 5.0]
    a = myPerson(v1,v2)
    print(a) 
