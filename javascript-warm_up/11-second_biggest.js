#!/usr/bin/node
if (process.argv[3] === undefined) {
  console.log(0);
} else {
  const numbers = process.argv.slice(2).map(Number).sort((a, b) => b - a);

  console.log(numbers[1]);
}
