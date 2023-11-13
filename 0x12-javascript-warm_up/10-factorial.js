#!/usr/bin/node
// #!/usr/local/bin/node
function factorial (n) {
  if (isNaN(n) || n === 0 || n === 1) {
    return 1;
  }

  return n * factorial(n - 1);
}

const result = factorial(parseInt(process.argv[2]));
console.log(result);
