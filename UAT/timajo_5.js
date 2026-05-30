const is_palindrome = (text) => {
    const str = text.toLowerCase().replaceAll(" ", "");
    let reversed = "";
    for (let i = str.length - 1; i >= 0; i--) {
        reversed += str[i];
    }
    
    return str === reversed;
} 

console.log(is_palindrome("racecar")) // true
console.log(is_palindrome("Hello"))   // false
console.log(is_palindrome("Was it a car or a cat I saw")) // true