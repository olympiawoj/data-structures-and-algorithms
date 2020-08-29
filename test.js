function validAnagram(str1, str2) {
    // add whatever parameters you deem necessary - good luck!
    //if the letters are not the same size, the are not

    if (str1.length !== str2.length) {
        return false
    }

    var letters = []
    for (var el of str1) {

        letters.push(el)
    }
    console.log('letters', letters)

    for (var el of str2) {
        var index = letters.indexOf(el)
        if (index !== -1) {
            letters.splice(index, 1)
            console.log('letters', letters)
        }

    }

    console.log('letters', letters)

    if (letters.length > 0) {
        return false
    } else {
        return true
    }

}






console.log(validAnagram("aaz", 'zza')) //false
// console.log(validAnagram('anagram', 'nagaram')) // true