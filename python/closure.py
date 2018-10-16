#!/usr/bin/python
__author__ = "olenji"


class A:
    def here(self):
        data = "A.here"
        def inline(param):
            print(data)
            print(param)

        aB = B()
        aB.here(inline)

class B:
    def here(self, callbackfuc):
        data = "B.here"
        callbackfuc(data)


# -------------------

def make_average():
  series = []
  def avg(p):
    series.append(p)
    return sum(series) / len(series)
  return avg
    
    
if __name__ == '__main__':
    aa = A()
    aa.here()
    print('---- other ----')
    avg = make_average()
    avg(10)
    print(avg(11))
    print(avg(12))
    print(avg.__code__.co_varnames)
    print(avg.__code__.co_freevars)
    print("avg.__closure__ \t%s" % avg.__closure__)
    print("avg.__closure__[0].cell_contents: \t%s" % avg.__closure__[0].cell_contents)
