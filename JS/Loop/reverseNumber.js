let number = 12345;
let rev = 0;
while (number > 0) {
  let temp = number % 10;
  rev = (temp + (rev * 10));
  number = parseInt(number / 10);
}
console.log(`The reverse number is ${rev}`);
