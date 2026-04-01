// Assignment 1: Palindrome Checker
function checkPalindrome() {
    let input = document.getElementById("palindromeInput").value;

    // Remove spaces, punctuation, and make lowercase
    let cleaned = input.toLowerCase().replace(/[^a-z0-9]/g, "");

    let reversed = cleaned.split("").reverse().join("");

    let result = document.getElementById("palindromeResult");

    if (cleaned === reversed && cleaned !== "") {
        result.textContent = `"${input}" is a palindrome.`;
    } else {
        result.textContent = `"${input}" is not a palindrome.`;
    }
}

// Assignment 2: Prime Number Checker
function checkPrime() {
    let num = parseInt(document.getElementById("primeInput").value);
    let result = document.getElementById("primeResult");

    if (isNaN(num)) {
        result.textContent = "Please enter a valid number.";
        return;
    }

    if (num <= 1) {
        result.textContent = `"${num}" is not a prime number.`;
        return;
    }

    for (let i = 2; i <= Math.sqrt(num); i++) {
        if (num % i === 0) {
            result.textContent = `"${num}" is not a prime number.`;
            return;
        }
    }

    result.textContent = `"${num}" is a prime number.`;
}