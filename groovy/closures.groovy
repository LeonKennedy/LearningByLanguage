// 闭包学习

doubleNum = { num -> num * 2 }
println doubleNum(3) // => 6
processThenPrint = { num, closure ->
num = closure(num); println "num is $num"
}
processThenPrint(3, doubleNum) // => num is 6
processThenPrint(10) { it / 2 } // => num is 5

import Math.*
piA = { 22 / 7 }
piB = { 333/106 }
piC = { 355/113 }
piD = { 0.6 * (3 + Math.sqrt(5)) }
piE = { 22/17 + 37/47 + 88/83 }
piF = { Math.sqrt(Math.sqrt(2143/22)) }
howCloseToPI = { Math.abs(it.value() - Math.PI) }
algorithms = [piA:piA, piB:piB, piC:piC, piD:piD, piE:piE, piF:piF]
findBestPI(algorithms)
def findBestPI(map) {
map.entrySet().sort(howCloseToPI).each { entry ->
def diff = howCloseToPI(entry)
println "Algorithm $entry.key differs by $diff"
}
}

def houston(Closure doit){
    (10..1).each{ count -> doit(count)}
}
houston { print it+' '}
print '\n'



assert [1, 2, 3].grep{ it < 3 } == [1, 2]
assert [1, 2, 3].any{ it % 2 == 0 }
assert [1, 2, 3].every{ it < 4 }
assert (1..9).collect{it}.join() == '123456789'
assert (1..4).collect{it * 2}.join() == '2468'
def add = { x, y -> x + y }
def mult = { x, y -> x * (y+1) }
assert add(1, 3) == 4
assert mult(1, 3) == 4
def min = { x, y -> [x, y].min() }
def max = { x, y -> [x, y].max() }
def triple = mult.curry(4); assert triple(2) == 12
def atLeastTen = max.curry(10)
assert atLeastTen(5) == 10
assert atLeastTen(15) == 15

def pairWise(list, Closure invoke) {
if (list.size() < 2) return []
def next = invoke(list[0], list[1])
return [next] + pairWise(list[1..-1], invoke)
}
// using min, max, etc. From previous slide
assert pairWise(1..5, add) == [3, 5, 7, 9]
assert pairWise(1..5, mult) == [3, 8, 15, 24]
assert pairWise(1..5, min) == [1, 2, 3, 4]
assert pairWise(1..5, max) == [2, 3, 4, 5]
assert 'cbaxabc' == ['a', 'b', 'c'].inject('x') {
    result, item -> item + result + item
}



