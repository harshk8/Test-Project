
function Validate() {
        var password = document.getElementById("id_password").value;
        var confirmPassword = document.getElementById("id_confirm_pass").value;
        if (password != confirmPassword) {
            alert("Passwords do not match.");
            return false;
        }

        return true;
    }

