// for�z�m�`?�Z�q���������O�@�Ĥ��@�ΰ�A�Ӵ`?�^?���O�@��??���l�@�ΰ�C
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

// �Ĥ@��?�k�A?? ��?�n�n���§@�ΰ�
// if (true) let x = 1;
// �ĤG��?�k�A��??
if (true) {
  let x = 1;
}


// -----   const   -------- 
const PI = 3.1415;
PI // 3.1415
// PI = 3;  ��? ���i�H?��

const foo = {};

// ? foo �K�[�@�Ę�ʡA�i�H���\
foo.prop = 123;
foo.prop // 123

// ? foo ���V�t�@��?�H�A�N�N??
// foo = {}; // TypeError: "foo" is read-only

// ?�H??
const foo2 = Object.freeze({});