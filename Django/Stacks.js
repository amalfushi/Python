function Stacks(type){
    this.contents = []
    this.type = type
}
Stacks.prototype.remove = function(){
    return this.contents.pop()
}
Stacks.prototype.add = function(x){
    if (typeof(x) != this.type){
        console.log('Nope')
    } else {
        this.contents.push(x)
    }
    return this
}

stack = new Stacks('number')

stack.add(1).add(2).add(3).add(true).add(false).add('taco').add('cat')
console.log(stack)

stack.remove()
console.log(stack)