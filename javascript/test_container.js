var arr = new Array(3);
arr[0] = "leon";
arr[1] = "coffee";
arr[2] = "olenji";
console.log(arr);

var arr1 = new Array(1, 2, 3);
console.log(arr1);

var arr1 = Array.prototype.slice.call((1, 2, 3));
console.log(arr1);
function list() {
    return Array.prototype.slice.call(arguments);
    // var slice = Function.prototype.call.bind(Array.prototype.slice, 37);
    // return slice(arguments);
}

var leading37List = list.bind(undefined, 37);
var list2 = leading37List();
console.log(list2);
var list3 = leading37List(1, 2, 3);
console.log(list3);