// for墇竚碻?塟秖ê场だ琌熌ノ办τ碻?蔨?场琌熌??ノ办
for (let i = 0; i < 4; i++) {
    let i = 'abc';
    console.log(i);
}
// ?? TDZ
function func() {
    let a = 10;
    // var a = 1;
}

// ?? TDZ
function func() {
    let a = 10;
    // let a = 1;
}

// 材销?猭?? ゲ?璶璶Τ毬ノ办
// if (true) let x = 1;
// 材销?猭ぃ??
if (true) {
  let x = 1;
}


// -----   const   -------- 
const PI = 3.1415;
PI // 3.1415
// PI = 3;  ╆? ぃ?

const foo = {};

// ? foo 睰熌橅┦Θ
foo.prop = 123;
foo.prop // 123

// ? foo 熌?禜碞塏??
// foo = {}; // TypeError: "foo" is read-only

// ?禜??
const foo2 = Object.freeze({});