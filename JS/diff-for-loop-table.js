//1.for Loop (Classic Counter):
for (let i = 0; i < 5; i++) {
  console.log(i);
}

//2.for...in Loop (Keys/Indexes):
let obj = { name: "Vijay", age: 25 };

for (let key in obj) {
  console.log(key, obj[key]);
}

// Also works for arrays (gives indexes):

let arr = ["a", "b", "c"];

for (let index in arr) {
  console.log(index, arr[index]);
}

//3.for...of Loop (Values):
let arr1 = ["x", "y", "z"];

for (let value of arr1) {
  console.log(value);
}

// Works for strings too:

for (let char of "JS") {
  console.log(char); // J, S
}

//4.forEach() Method:
let arr2 = [10, 20, 30];

arr2.forEach(function (index, value) {
  console.log(index, value);
});
