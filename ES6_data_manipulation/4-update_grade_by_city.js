export default function updateStudentGradeByCity(listOfStudents, city, newGrades) {
  return listOfStudents.filter((student) => student.location === city).map((student) => newGrades.find((grade) => grade.studentId === student.id));
}
 