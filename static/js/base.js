
// Toggle form buttons
function toggleForm(buttonId, formId) {
    var button = document.getElementById(buttonId);
    var form = document.getElementById(formId);

    console.log("function working");

    if (!button.dataset.originalHtml) {
        button.dataset.originalHtml = button.innerHTML;
    }

    if (form.style.display === 'none') {
        form.style.display = 'block';
        button.textContent = "Close";
    } else {
        form.style.display = 'none';
        button.innerHTML = button.dataset.originalHtml;

    }
}
