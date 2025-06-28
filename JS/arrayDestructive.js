let numbers = [1, 2, 3, 4];

console.log(numbers);
let [a, b, , d] = numbers;
console.log(d);

let words = "My name is Vijay".split(" ");
let [e, f, ...g] = words;
console.log(words);
console.log(g);
