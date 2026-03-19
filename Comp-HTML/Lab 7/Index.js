


console.log("Project setup successful!");

//Grading System Function
function calculateGrade(score) {
    // Check for invalid inputs
    if (typeof score !== "number" || score < 0 || score > 100) {
        return "Invalid Score!";
    }

    if (score >= 90 && score <= 100) {
        return "A (Distinction)";
    } else if (score >= 80 && score <= 89) {
        return "B (Merit)";
    } else if (score >= 70 && score <= 79) {
        return "C (Pass)";
    } else if (score >= 50 && score <= 69) {
        return "D (GA - Good Attempt)";
    } else {
        return "F (Fail)";
    }
}

const testScores = [-95, 85, 75, 65, 45, -5, 110];

// Print results
console.log("\nGrading System Test Results:");
for (let i = 0; i < testScores.length; i++) {
    let score = testScores[i];
    console.log("Score: " + score + " -> " + calculateGrade(score));
}