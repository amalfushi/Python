function SLL() {
    this.head = null;
}

function Node(val) {
    this.val = val;
    this.next = null;
}

SLL.prototype.newNode = function(newVal) {
    var newNode = new Node(newVal);
    if (this.head == null){
        this.head = newNode;
    } else {
        newNode.next = this.head;
        this.head = newNode;
    }
    return this;
}

SLL.prototype.removeNode = function() {
    if (this.head.next === null){
        this.head = null;
    } else {
        this.head = this.head.next;
    }
    return this;
}

var SLLone = new SLL()
SLLone.newNode('a').newNode('b').newNode('c')
console.log(SLLone)
SLLone.removeNode().removeNode()
console.log(SLLone)