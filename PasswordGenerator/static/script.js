function copyPassword() {
        const passwordInput = document.getElementById('password');
        if (!passwordInput.value) return;

        navigator.clipboard.writeText(passwordInput.value).then(() => {
        const btn = document.getElementById('copyBtn');
        btn.textContent = 'Copied!';
        btn.disabled = true;
        setTimeout(() => {
            btn.textContent = 'Copy';
            btn.disabled = false;
        }, 1500);
        }).catch(() => { alert('Failed to copy password. Please copy manually.'); });
    }

    function generatePassword() {
        fetch('/generate-password')
            .then(response => response.json())
            .then(data => {
            const passwordInput = document.getElementById('password');
            const copyBtn = document.getElementById('copyBtn');

            passwordInput.value = data.password;
            copyBtn.disabled = false;
            copyBtn.textContent = 'Copy';
        });
    }

    function toggleDarkMode() {
      document.body.classList.toggle('light');
    }