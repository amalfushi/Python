function Human(name, age){
    this.name = name;
    this.age = age;
}

Human.prototype.speak = function(){
    console.log('My name is ${this.name}');
}

var frank = new Human('Frank', 49);
var speros = new Human('Speros', 35);

frank.speak()
speros.speak()