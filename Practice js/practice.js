// Importing random-js library
const Random = require('random-js');

// Creating a new Random engine
const random = new Random();

// Generate a random integer between 1 and 100 using random-js
let randomNumber = random.integer(1, 100);
console.log(randomNumber);
