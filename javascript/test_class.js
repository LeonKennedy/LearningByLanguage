var birth = '2000/01/01'

var Person = {
    name: '张三',
    birth,
    hello() { console.log('my name is: ', this.name); },
    ['say' + 'hi']() { console.log('say hi'); }
}


var p = Person;
p.hello();
p['name'] = 'leon';
p.sayhi();
var gobj = {
    * m() {
        yield 'hello, world';
    }
}

    + 0 === -0 //true
NaN === NaN // false
Object.is(+0, -0) // false
Object.is(NaN, NaN) // true


var target = { a: 1 };
var source1 = { b: 2 };
var source2 = { c: 3, d: 4 };

Object.assign(target, source1, source2);
console.log(target); // {a:1, b:2, c:3}