function fact(num) {
  if (num === 0) return 1;
  else {
    return num * fact(num - 1);
  }
}
let result = fact(5);
console.log(`factorial of 5 is ${result}`);
