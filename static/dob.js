const today = new Date();

const maxDate = new Date(today.getFullYear() - 18, today.getMonth(),
today.getDate());

document.getElementById("dob").max = maxDate.toISOString().split("T")[0]
