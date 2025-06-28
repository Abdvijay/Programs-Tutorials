//1.Push method
let arr = [1, 4, 3];
arr.push(10);
console.log(arr); //[ 1, 4, 3, 10 ]

//2.Pop method
arr.pop();
console.log(arr); //[ 1, 4, 3 ]

//3.Unshift method
arr.unshift(0);
console.log(arr); //[ 0, 1, 4, 3 ]

//4.Shift method
arr.shift(10);
console.log(arr); //[ 1, 4, 3 ]

//5. Length method
console.log(arr.length); //3

//6. indexOf method
console.log(arr);
console.log(arr.indexOf(3)); //2
console.log(arr.indexOf(5)); //-1
console.log(arr[5]); // undefined

//7. includes method
console.log(arr.includes("Vijay")); //false
console.log(arr.includes(4));

//8. join method
console.log(arr.join(" | ")); //1 | 4 | 3

//9. reverse method
console.log(arr.reverse().join(" ~ ")); //3 ~ 4 ~ 1

//10. sort method
console.log(arr.sort()); //[ 1, 3, 4 ]

//11. slice method
let fruits = ["Apple", "Banana", "Mango", "Lemon"];
console.log(fruits); //[ 'Apple', 'Banana', 'Mango', 'Lemon' ]
console.log(fruits.slice(0, 2)); //[ 'Apple', 'Banana' ]

//12. splice method
console.log(fruits); //[ 'Apple', 'Banana', 'Mango', 'Lemon' ]
fruits.splice(1, 2); // 1 is index, 2 is how many elements from the index
console.log(fruits); //[ 'Apple', 'Lemon' ]

let numbers = [5, 7, 8, 9, 4];
// console.log(numbers.splice(2))
console.log(numbers); //[ 5, 7, 8, 9, 4 ]
console.log(numbers.splice(2, 2, 10, 10)); //[ 8, 9 ]
console.log(numbers); //[ 5, 7, 10, 10, 4 ]

console.log(numbers.splice(2,1,20,30,40));
console.log(numbers)