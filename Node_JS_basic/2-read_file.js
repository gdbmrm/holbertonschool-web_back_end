function countStudents(path) {
  try {
    const data = fs.readFileSync(path, "utf-8");
    console.log(`Number of students: ${nb_of_students}`)

  } catch (error) {
    throw new error ('Cannot load the database');
  }
  

}