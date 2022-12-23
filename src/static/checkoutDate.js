const today = new Date();
const todayString = today.getFullYear() + "-" + (today.getMonth() + 1).toString().padStart(2, '0') + "-" + today.getDate().toString().padStart(2,'0');

const maxDate = new Date(today.getTime() + 14 * 24 * 60 * 60 * 1000);
const maxDateString = maxDate.getFullYear() + "-" + (maxDate.getMonth() + 1).toString().padStart(2, '0') + "-" + maxDate.getDate().toString().padStart(2,'0');

document.getElementById("delivery__date").min = todayString
document.getElementById("delivery__date").max = maxDateString
