//RECURSIVELY
function countDown(num) {
    if (num < 0) {
        console.log("All done!");
        return //must return to stop it
    }
    console.log(num);
    num--
    countDown(num)
}


//ITERIVELY W/O RECURSION
function countDown(num) {
    for (var i = num; i > 0; i--) {
        console.log(i)
    }
    console.log("All done!")
}