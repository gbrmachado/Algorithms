var heap = function() {
    var Heap = function() {
        return {
            n : 0,
            q : [],
        }
    }

    // Return the parent position of pos
    var parent = function(h, pos) {
        if (pos === 0) return -1;
        else {
            return Math.ceil(pos/2) - 1;
        }
    }

    var youngChild = function(h, pos) {
        return 2 * pos + 1;
    }

    var bubbleUp = function(h, pos) {
        var c = parent(h, pos);
        if (c === -1) return;

        if (h.q[pos] < h.q[c]) {
            var aux = h.q[pos];
            h.q[pos] = h.q[c];
            h.q[c] = aux;
            bubbleUp(h, c);
        }
    }

    var bubbleDown = function(h, pos) {
        var child = youngChild(h, pos);
        var minIndex = pos;

        //Get the Min between the two childs of pos
        for( var i = 0; i<=1; i++ ) {
            if (child + i <= h.n && h.q[minIndex] > h.q[child + i])
                minIndex = child + i;
        }

        if (minIndex !== pos) { //
            var aux = h.q[pos];
            h.q[pos] = h.q[minIndex];
            h.q[minIndex] = aux;
            bubbleDown(h, minIndex);
        }
    }

    var extract_minimum = function(h) {
        if (h.n <= 0) return -1;
        else {
            var min = h.q[0];
            h.q[0] = h.q.pop();
            h.n--;
            
            bubbleDown(h, 0);
            return min;
        }
    }
    var insert = function(h, x) {
        h.q.push(x);
        h.n++;
        bubbleUp(h, h.n - 1);
    }


    var h = new Heap();
    
    return {
        insert: function(x) {
            insert(h, x);
        },
        extractMinimum: function() {
            extract_minimum(h);
        },
        print: function() {
            console.log(h.q);
        }
    }
};

var h = new heap();
h.insert(5);
h.insert(2);
h.insert(3);
h.print();
h.extractMinimum();
h.print();
