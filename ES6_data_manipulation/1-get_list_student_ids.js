export default function getListStudents(myArray) {
  if (!Array.isArray(myArray)) {
    return [];
  }
  return myArray.map(({ id }) => id);
}
