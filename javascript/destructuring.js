let [a, b, c] = [1,2,3]
let [foo, [[bar], baz]] = [1, [[2], 3]];
let [ , , thirdz] = ["foo", "bar", "baz"];
let [head, ...tail] = [1, 2, 3, 4];
// ∏—Ã€§£¶®•\°AâZ∂q™∫≠»¥Nµ•§_undefined
let [barz, foot] = [1];


// §£¨O•iπM?™∫?Ã€ âN©Í?

// ¶˝•u≠n¨O•i•HπM? êm•i•H?≠»
function* fibs() {
    let a = 0;
    let b = 1;
    while (true) {
      yield a;
      [a, b] = [b, a + b];
    }
  }
  let [first, second, third, fourth, fifth, sixth] = fibs();

  // ∏—Ã€•i•H®œ•Œ¿q?≠»
  let [foos = true] = [];  // true
let [x, y = 'b'] = ['a']; // x='a', y='b'
let [x2, y2 = 'b'] = ['a', undefined]; // x='a', y='b'


// ∏—Ã€?∂H?≠»
let { fooa, bara } = { foo: 'aaa', bar: 'bbb' };
let {foob} = {bar: 'baz'}; // ¶p™G∏—Ã€•¢? ≠»? undefined

// ¶p™GâZ∂q¶W…OòÌ© ¶W§£¶P
let obj = { left: 'hello', last: 'world' };
let { left: f, last: l } = obj;   // first ¨O§«∞tº“¶° f¨OâZ∂q

let {0 : uno, [arr.length - 1] : last} = arr;
const [a, b, c, d, e] = 'hello';
