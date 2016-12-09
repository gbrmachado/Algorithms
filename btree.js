var BST = function() {

    var Node = function(pLeft, key, pRight, node_parent) {
        return {
            key: (typeof(key) === 'undefined') ? null : key,
            pLeft: (typeof(pLeft) === 'undefined') ? null : pLeft,
            pRight: (typeof(pRight) === 'undefined') ? null : pRight,
            node_parent: (typeof(node_parent) === 'undefined') ? null : node_parent,
        }
    }

    var root = new Node();

    var insertNode = function(node, key, node_parent) {
        if(node.key === null) {
            node.pLeft = new Node();
            node.pRight = new Node();
            node.key = key;
            node.node_parent = node_parent;
            return true;
        }

        if (key < parseInt(node.key)) {
            insertNode(node.pLeft, key, node);
        }
        else {
            insertNode(node.pRight, key, node);
        }
    }

    var search = function(node, key) {
        if (node.key === null) {
            return null;
        }

        if (node.key === key) {
            return node;
        }

        if (key < parseInt(node.key)) {
            search(node.pLeft, key);

        }
        if (key > parseInt(node.key)) {
            search(node.pRight, key);
        }
    }

    var traverse = function(node, callback) {
        if (node.key) {
            callback(node);
            traverse(node.pLeft, callback);
            traverse(node.pRight, callback);
        }
    }

    var depth = function(node) {
        if (node.key === null) return 0;

        if (!node.pLeft.key && !node.pRight) return 1;

        if (node.pLeft.key) return 1 + depth(node.pLeft);

        if (node.pRight.key) return 1 + depth(node.pRight);

        return Math.min(depth(node.pLeft), depth(node.pRight))+1;
    }

    var minimum = function(node) {
        if (node.pLeft.key === null) return node;
        else return minimum(node.pLeft);
    }

    var maximum = function(node) {
        if (node.pRight.key === null) return node;
        else return maximum(node.pRight);
    }

    var numberSons = function(node) {
        var finalResult = {
            sum : 0,
            left:false,
            right:false
        }
        if (node.pLeft.key) {
            finalResult.sum++;
            finalResult.left = true;
        };

        if (node.pRight.key) {
            finalResult.sum++;
            finalResult.right = true;
        }
        return finalResult;
    }

    var deleteNode = function(node, key) {
        if (node.key === null) {
            return;
        }

        if (key < parseInt(node.key)) {
            deleteNode(node.pLeft, key);
        }

        else if (key > parseInt(node.key)) {
            deleteNode(node.pRight, key);
        }

        else {
            var sons = numberSons(node);

            // If node has no childs
            if (sons.sum === 0) {
                delete node.pLeft;
                delete node.pRight;
                delete node.key;
                delete node;
            }

            // If node has only one child
            else if (sons.sum === 1 ) {
                var positionParent;
                if (node.node_parent.pRight === node) {
                    positionParent = 1;
                }
                else {
                    positionParent = 0;
                }


                if (sons.left) {
                    if (positionParent === 1) {
                        node.node_parent.pRight = node.pLeft;
                    } else {
                        node.node_parent.pLeft = node.pLeft;
                    }
                }  
                if (sons.right) {
                    if (positionParent === 1) {
                        console.log("value");
                        node.pRight.node_parent = node.node_parent;
                        node.node_parent.pRight = node.pRight;
                    } else {
                        node.pLeft.node_parent = node.node_parent;
                        node.node_parent.pLeft = node.pRight;
                    }
                }
            }
            // If node has two children
            else {
                //get the lefmost item on the right pointer
                var leftmost = minimum(node.pRight);
                //Prepare the leftmost to be changed with node
                leftmost.node_parent.pLeft = new Node();
                leftmost.node_parent = node.node_parent;
                leftmost.pRight = node.pRight;
                leftmost.pLeft = node.pLeft;


                if (node.node_parent.pLeft === node) node.node_parent.pLeft = leftmost;
                if (node.node_parent.pRight === node) node.node_parent.pRight = leftmost;

                node.pRight.node_parent = leftmost;
                node.pLeft.node_parent = leftmost;
                node = leftmost;
            }
        }
    }

    return {
        insert: function(key) {
            var keyInt = parseInt(key, 10);
            if (isNaN(keyInt)) {
                return undefined;
            } else {
                return insertNode(root, keyInt)
            }
        },

        print: function() {
            traverse(root, console.log);
        },

        search: function(key) {
            var keyInt = parseInt(key, 10);
            if (isNaN(keyInt)) {
                return undefined
            } else {
                return search(root, keyInt);
            }
        },
        deleteNode: function(key) {
            var keyInt = parseInt(key,10);
            if (isNaN(keyInt)) {
                return undefined;
            } else {
                return deleteNode(root, keyInt);
            }
        },
        minimumDepth: function() {

            return depth(root);
        }


    }
}

var node = new BST();
node.insert(8);
node.insert(4);
node.insert(15);
node.insert(10);
node.insert(17);
node.insert(16);
var minDepth = node.minimumDepth();
console.log(minDepth);
