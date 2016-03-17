
def name = 'Olenji'
println "$name, I want get car."

String longer = """${name}, the car is int the next row. """
        
assert 0.5 == 1/2
        
def printSize(obj){
    println obj?.size()
}

printSize(name)

def twister = '''\
She sells, sea shells
By the sea shore'''

def lines = twister.split('/n')
println lines[0]

// Number...
def x = 3
def y = 4
assert x + y == 7
assert x.plus(y) == 7
assert x instanceof Integer
assert 0.5 == 1/2 // uses BigDecimal arithmetic as default
def a = 2 / 3 // 0.6666666666
def b = a.setScale(3, BigDecimal.ROUND_HALF_UP)
assert b.toString() == '0.667'
assert 4 + 3 == 7 // 4.plus(3)
assert 4 - 3 == 1 // 4.minus(3)
assert 4 * 3 == 12 // 4.multiply(12)
assert 4 % 3 == 1 // 4.mod(3)
assert 4 ** 3 == 64 // 4.power(3)
assert 4 / 3 == 1.3333333333 // 4.div(3)
assert 4.intdiv(3) == 1 // normal integer division
assert !(4 == 3) // !(4.equals(3))
assert 4 != 3 // ! 4.equals(3)
assert !(4 < 3) // 4.compareTo(3) < 0
assert !(4 <= 3) // 4.compareTo(3) <= 0
assert 4 > 3 // 4.compareTo(3) > 0
assert 4 >= 3 // 4.compareTo(3) >= 0
assert 4 <=> 3 == 1 // 4.compareTo(3)

// Lists
def list = [ 3, new Date(), 'Jan']
assert list + list == list * 2

assert [1,2,3,4] == (1..4)
assert [1,2,3] + [1] == [1,2,3,1]
assert [1,2,3] << 1 == [1,2,3,1]
assert [1,2,3,1] - [1] == [2,3]
assert [1,2,3] * 2 == [1,2,3,1,2,3]
assert [1,[2,3]].flatten() == [1,2,3]
assert [1,2,3].reverse() == [3,2,1]
assert [1,2,3].disjoint([4,5,6])
assert [1,2,3].intersect([4,3,1]) == [3,1]
assert [1,2,3].collect{ it+3 } == [4,5,6]
assert [1,2,3,1].unique().size() == 3
assert [1,2,3,1].count(1) == 2
assert [1,2,3,4].min() == 1
assert [1,2,3,4].max() == 4
assert [1,2,3,4].sum() == 10
assert [4,2,1,3].sort() == [1,2,3,4]
assert [4,2,1,3].findAll{ it%2 == 0 } == [4,2]

// Maps
def map = [a:1, 'b':2]
assert map['a'] == 1 && map.b == 2
println map.keySet()                       // [a, b]

map = [:]                                  // define 
// extend the map through assignment
map[1] = 'a'; map[2] = 'b'
map[true] = 'p'; map[false] = 'q'
map[null] = 'x'; map['null'] = 'z'
assert map == [ 1:'a', 2:'b', (true):'p',
(false):'q', (null):'x', 'null':'z' ]
def sb = new StringBuffer()
[1:'a', 2:'b', 3:'c'].each{ k, v-> sb << "$k:$v, " }
assert sb.toString() == '1:a, 2:b, 3:c, '

map = [1:'a', 2:'b', 3:'c']
def string = map.collect{ k, v -> "$k:$v" }.join(', ')
assert string == '1:a, 2:b, 3:c'

assert [
[ name: 'Clark', city: 'London' ],
[ name: 'Sharma', city: 'London' ],
[ name: 'Maradona', city: 'LA' ],
[ name: 'Zhang', city: 'HK' ],
[ name: 'Ali', city: 'HK' ],
[ name: 'Liu', city: 'HK' ]
].groupBy { it.city } == [
London: [
[ name: 'Clark', city: 'London' ],
[ name: 'Sharma', city: 'London' ]
], LA: [
[ name: 'Maradona', city: 'LA' ]
], HK: [
[ name: 'Zhang', city: 'HK' ],
[ name: 'Ali', city: 'HK' ],
[ name: 'Liu', city: 'HK' ]
]
]

// Regular Expreesions...
assert "Hello World!" =~ /Hello/        // Find operator
assert "Hello World!" ==~ /Hello\b.*/   // Match operator
def p = ~/Hello\b.*/                    // Pattern operator
assert p.class.name == 'java.util.regex.Pattern'
// replace matches with calculated values
assert "1.23".replaceAll(/./){ ch -> ch.next() } == '2/34'
assert "1.23".replaceAll(/\d/){ num ->
num.toInteger() + 1
} == '2.34'
assert "1.23".replaceAll(/\d+/){ num ->
num.toInteger() + 1
} == '2.24'

// Control Structures
switch (10) {
case 0 : /* F */ 
     break
case 0..9 : // F
case [8,9,11] : // F
case Float : // F
case {it % 3 == 0} : // F
case ~/../ : // T
    println "~/../"
    break
default : // F
    println 'default'
}

// Beans and GPath
class Dir {
String name
List dirs
}
def root = new Dir (name: '/', dirs: [
new Dir (name: 'a'),
new Dir (name: 'b')
])
assert root.dirs[0].name == 'a'
assert root.dirs.name == ['a', 'b']
assert root.dirs.name*.size() == [1, 1]
def expected = ['getName', 'setName', 'getDirs', 'setDirs']
def accessorMethods = Dir.methods.name.grep(~/(g|s)et.*/)
assert accessorMethods.intersect(expected) == expected
println Dir.methods.name

// Ranges
def letters = 'a'..'z'
def numbers = 0..<10

// Static Imports
import static java.awt.Color.LIGHT_GRAY
println LIGHT_GRAY

import static Boolean.FALSE as F
println !F

import static Calendar.getInstance as now
println now().time

import static Math.PI
// assert cos(2 * PI) == 1.0

new File('baby.txt').eachLine{println it}


