const express = require('express');
const app = express();
const port = 3000;

// Set EJS as the templating engine
app.set('view engine', 'ejs');


const students = [
    { name: "John", major: "Computer Science" },
    { name: "Maria", major: "Information Technology" },
    { name: "David", major: "Cybersecurity" },
    { name: "Lisa", major: "Software Engineering" }
];

// Define a route for the homepage
app.get('/', (req, res) => {
    res.render('index', { title: 'Welcome to EJS Lab', message: 'Hello, Students!' });
});

app.get('/students/:name', (req, res) => {
    res.render('student', { studentName: req.params.name });
});

app.get('/students', (req, res) => {
    res.render('students', { students: students });
});

// Start the server
app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});


