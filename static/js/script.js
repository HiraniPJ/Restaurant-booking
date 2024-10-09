// Form Validation

(function() {
    'use strict';
    window.addEventListener('load', function() {
        var forms = document.getElementsByClassName('needs-validation');
        Array.prototype.filter.call(forms, function(form) {
            form.addEventListener('submit', function(event) {
                if (form.checkValidity() === false) {
                    event.preventDefault();
                    event.stopPropagation();
                }
                form.classList.add('was-validated');
            }, false);
        });
    }, false);
})();

// Disable form submission button until all fields are filled

document.addEventListener('DOMContentLoaded', function() {
    var submitButton = document.querySelector('button[type="submit"]');
    var form = document.querySelector('.needs-validation');

    if (form) {
        form.addEventListener('input', function() {
            if (form.checkValidity()) {
                submitButton.disabled = false;
            } else {
                submitButton.disabled = true;
            }
        });
    }
});