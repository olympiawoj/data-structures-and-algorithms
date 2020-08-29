function bubbleSort(arr) {
    var noSwaps
    for (var i = arr.length; i > 0; i--) {
        //assume no swaps every time through
        //but if we make a swap, set to be false
        noSwaps = true
        //repeat this process for every item
        for (var j = 0; j < i - 1; j++) {
            console.log(arr, arr[j], arr[j + 1])
            //compare w/e item we're looking at with j to the one in front of it, j and j+1
            if (arr[j] > arr[j + 1]) {
                //SWAP
                var temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                noSwaps = false
            }
        }
        console.log("ONE PASS COMPLETE")
        if (noSwaps) break;
    }
    return arr;
}

bubbleSort([8, 1, 2, 3, 4, 5, 6, 7])