function greet(name) {
  return `Hello, ${name}! Welcome to ClassLab.`;
}

function add(a, b) {
  return a + b;
}

console.log(greet("Student"));
console.log("2 + 3 =", add(2, 3));

// Exposed so the test runner can reach them
globalThis.greet = greet;
globalThis.add = add;
