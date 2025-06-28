let number = new Set();

number.add(4);
number.add("Vijay");
number.add(5);
number.add(4);
console.log(number); //Set(3) { 4, 'Vijay', 5 }

for (value of number) {
  console.log(value);
}

number.forEach((element) => {
  console.log(element);
});

let name = new Set("Bookkeeper");
console.log(name); //Set(6) { 'B', 'o', 'k', 'e', 'p', 'r' }