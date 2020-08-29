function insertion_sort(arr) {
    //Iterate over every item starting at 1st index instead of 0
    for (var i = 1; i < arr.length; i++) {
        //Variable to keep track of value we're looking at
        var currentVal = arr[i]
        //Loop to work backwards - starting at 1 less than i. If i is 4, we want to compare to index i -1
        for (var j = i - 1; j >= 0 && arr[j] > currentVal; j--) {
            //Move value forward
            arr[j + 1] = arr[j]
            console.log(arr)
        }
        //Insert current val to j+1, ex insert 1 at beginning
        arr[j + 1] = currentVal
        console.log(arr)
    }
    return arr
}

insertion_sort([2, 1, 9, 76, 4])

//If our array was sorted [1, 2, 9, 76, 4]
// Take 4 and compare it to 76 - if it's smaller, move 76 up to where 4 is
// Look next - 9 is larger so move 9
// Check 2 - 4 is larger so put 4 right here[1, 2, 4. 9, 76]

//Start with 1 and look back at 2, 1 needs to go here so move 2 forward, never added in 1
//After loop finishes, that means we found correct spot for where we need to insert current val
// (5)[2, 2, 9, 76, 4]
//     (5)[2, 2, 9, 76, 76]
//     (5)[2, 2, 9, 9, 76]
//     (5)[2, 2, 9, 9, 76]



//If our array was sorted [1, 2, 9, 76, 0]
// If I is for, we  have loop j that goes from 3, 2, 1, 0



//Insertion console.log
insertion_sort([2, 1, 9, 76, 4])

// VM7341: 10(5)[2, 2, 9, 76, 4]
// VM7341: 14(5)[1, 2, 9, 76, 4]
// VM7341: 14(5)[1, 2, 9, 76, 4]
// VM7341: 14(5)[1, 2, 9, 76, 4]
// VM7341: 10(5)[1, 2, 9, 76, 76]
// VM7341: 10(5)[1, 2, 9, 9, 76]
// VM7341: 14(5)[1, 2, 4, 9, 76]
//     (5)[1, 2, 4, 9, 76]