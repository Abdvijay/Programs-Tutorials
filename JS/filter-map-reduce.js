let numbers = [1, 2, 3, 4, 5, 6];

// numbers.forEach((n) => {
//   if (n % 2 === 0) console.log(n);
// });

//Filter method
console.log(numbers.filter((n) => n % 2 === 0)); //[ 2, 4, 6 ]

numbers
  .filter((n) => n % 2 === 0)
  .forEach((n) => {
    console.log(n);
  });

// 2
// 4
// 6

//map methods
numbers
  .filter((n) => n % 2 === 0)
  .map((n) => n * 2)
  .forEach((n) => {
    console.log(n);
  });

//reduce method
let result = numbers
  .filter((n) => n % 2 === 0)
  .map((n) => n * 2)
  .reduce((a, b) => a + b);
console.log(result);
