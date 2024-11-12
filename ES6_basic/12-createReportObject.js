export default function createReportObject(employeesList) {
  return {
    allEmployees: employeesList,
    getNumberOfDepartments() {
      let sum = 0;
      for (const department in employeesList) {
        sum += 1;
      }
      return sum;
    },
  };
}
