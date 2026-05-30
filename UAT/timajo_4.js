const average = (nums) => {
    let sum = 0;
    for (let num of nums) {
        sum += num;
    }
    
    return sum / nums.length
}

console.log(average([12, 8, 20, 16]))