function add(a, b) {
    this(a, b);
    console.log(a+b);
}

function sub(a, b) {
    console.log(a - b);
}

add.call(sub, 3, 1);


function Animal() {
    this.name = "animal";
    this.showName = function () {
        console.log(this.name);
    };
}

function Book() {
    this.name = 'book';
    this.showName = () => console.log(this.name);
}

function Cat() {
    this.name = "cat";
}
var ani = new Animal();
var cat = new Cat();
ani.showName.call(cat, ['a', 'b']);

function BlackCat(name) {
    Animal.call(this, name);
}

var cat = new BlackCat("black cat");
cat.showName();

var animals = [
  {species: 'Lion', name: 'King'},
  {species: 'Whale', name: 'Fail'}
];

for (var i = 0; i < animals.length; i++) {
  (function (i) { 
    this.print = function () { 
      console.log('#' + i  + ' ' + this.species + ': ' + this.name); 
    } 
    this.print();
  }).call(animals[i], i);
}