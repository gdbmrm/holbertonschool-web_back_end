export default function getResponseFromAPI() {
  var promise = new Promise(function(resolve, reject) {
    let success = true;
  
    if (success) {
      resolve("Stuff worked!");
    }
    else {
      reject(Error("It broke"));
    }
  });
  return promise;
}
