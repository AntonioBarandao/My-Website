document.querySelector("form").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent page reload

    console.log("JS Loaded")

    // Get form values
    const name = document.querySelector('input[name="FullName"]').value;
    const email = document.querySelector('input[name="email"]').value;
    const gender = document.querySelector('input[name="gender"]:checked')?.value;
    const dob = document.querySelector('input[name="DateOfBirth"]').value;

    // Create new table row
    const newRow = document.createElement("tr");

    newRow.innerHTML = `
        <td>${name}</td>
        <td>${email}</td>
        <td>${gender}</td>
        <td>${dob}</td>
    `;

    // Append to table
    document.querySelector("tbody").appendChild(newRow);

    // Reset form after submission
    document.querySelector("form").reset();

    console.log("JS Finished")
});
