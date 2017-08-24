function* gen(x) {
    var y = yield x + 2;
    return y * 2;
}
var g = gen(1);
console.log(g.next());
console.log(g.next(2));