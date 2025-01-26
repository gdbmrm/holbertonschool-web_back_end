function countStudents(path) {
  try {
    const data = fs.readFileSync(path);
    const content = data.toString('utf-8').split('\n');
    const lines = content.slice(1);
    const studentsData = content.split(',')

    if (lines.length < 2) {
      throw new Error('Cannot load the database');
    }

    const students = {};
    const totalStudents = lines.length;
    console.log(`Number of students: ${totalStudents}`)

    studentsData.forEach((line) => {

      
    });

    console.log(`Number of students in FIELD: ${totalStudents}. List: ${students}`)

  } catch (error) {
    throw new error ('Cannot load the database');
  }
}
