export default function updateUniqueItem(myMap) {
  if (!(myMap instanceof Map)) {
    throw new Error ('Cannot process')
  }
  for (let [key, value] of myMap) {
    if (value === 1) {
      myMap.set(key, 100)
    }
  }
  return myMap;
}
