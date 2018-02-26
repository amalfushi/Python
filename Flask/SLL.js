function SLL(){
    this.head = null
    this.add = function(val){

        if (val instanceof Node){
            var newNode = val;
        } else {
            var newNode = new Node(val);
        }
        
        if (this.head === null){
            this.head = newNode;
        } else {
            var curNode = this.head;
            while (curNode.next !== null){
                curNode = curNode.next;
            }
            curNode.next = newNode;
        }

    }
}

function Node(val){
    this.val = val;
    this.next = null;
}

// Singularly Linked Lists: are collections of object linked together in one direction

var mySLL = new SLL();
var node1 = new Node(1);
// mySLL.head = node1;
mySLL.add(node1)

console.log(mySLL)
// Classes is a set of blueprints or instructions to define objects

// Objects are instances constructed from the blueprints (Classes)