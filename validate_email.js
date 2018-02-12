function validateEmail(email) {
  try {
    var local_part = email.split("@");
    var domain = local_part[1].split(".");
    var domain_suffix = domain[1];
      }
  catch(err) { 
    return false;
      }
  if 
  if (local_part.indexOf("") != -1){
    return false;
      }
  if (domain.indexOf("") != -1 || domain.length < 2){
    return false;
      }
  if (['co', 'com'].indexOf(domain_suffix) == -1){
    return false;
      }
  return true;
}

const emails = [    // Expected results:
  'test@test.co.im',  // true
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