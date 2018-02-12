//Validating an email address using regular exprestions 

function validateEmail(email) {
  return new RegExp(/[^@]+@([^@\.]+\.)+[[c][o]|[c][o][m]]/).test(email);
}

const emails = [    // Expected results:
  'test@test.com',  // true
  'test@@test.com', // false
  'test@test..com', // false
  'test@test',      // false
  '@test.com',      // false
  'a@b.c',          // false
  'a@b.co',         // true
  '@.',             // false
  'foo@bar123.com'  // true
];

(function() {
  for (let i = 0; i < emails.length; i++) {
    console.log(validateEmail(emails[i]));
  }
}());