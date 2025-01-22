process.stdin.setEncoding('utf8');

console.log("Welcome to Holberton School, what is your name?")


let studentName;

process.stdin.on('readable', function() {
  var chunk = process.stdin.read();
  if (chunk !== null) {
    studentName = chunk
  } else {
    studentName = "Bob"
  }
});

process.stdin.on('end', function() {
  process.stdout.write('end');
});

console.log(`Your name is: ${studentName}`)
console.log("This important software is now closing")
