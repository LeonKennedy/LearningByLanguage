// 遍历的使用

// each
def log = 0
(1..10).each{log+=it }
assert log == 55
log = ""
(1..10).each{log+=it }
assert log == "12345678910"

// findAll
assert [1,2,3,4,5].findAll{ it > 2 } == [3,4,5] 

// collect
assert [1,2,3,4,5].collect{ it * it } == [1,4,9,16,25] 

// any
assert [1,3,5,7,9].any{ it * it == it + 6}

// every
assert [1,3,5,7,9].every{ it * it < 1000 }
