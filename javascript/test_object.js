var Book = {
    name: 'book',
    show() {
        console.log(this.name);
    },
    ashow: function () {
        console.log(this.name);
    },
    showName: () => console.log(this.name),
}
var ani = new Animal();
ani.showName();
let book = Book;
book.showName();
book.show()
book.ashow()
