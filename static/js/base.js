
function toggleForm(buttonId, formId) {
    var button = document.getElementById(buttonId);
    var form = document.getElementById(formId);

    console.log("function working");

    if (form.style.display === 'none') {
        form.style.display = 'block';
        button.textContent = "Close";
    } else {
        form.style.display = 'none';
        button.textContent = "Create new post";
    }
}
