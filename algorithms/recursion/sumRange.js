function sumRange(num) {
    if (num === 1) return 1;   //base case
    return num + sumRange(num - 1);   //recursive call with smaller input   
}
sumRange(3)


//3 + sumRange(2) --> 3 + 2 + sumRange(1) --> 3 + 2 + 1 = 6
