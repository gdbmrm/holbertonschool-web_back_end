export default function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
    const success = true;

    if (success) {
      resolve('Stuff worked!');
    } else {
      reject(Error('It broke'));
    }
  });
}
