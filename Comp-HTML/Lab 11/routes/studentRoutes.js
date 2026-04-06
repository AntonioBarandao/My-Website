const express = require('express');
const router = express.Router();
const Student = require('../models/student');

// CREATE
router.post('/', async (req, res) => {
  try {
    const student = new Student(req.body);
    const saved = await student.save();
    res.status(201).json(saved);
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
});

// READ
router.get('/', async (req, res) => {
  const students = await Student.find();
  res.json(students);
});

// UPDATE
router.put('/:id', async (req, res) => {
  try {
    const updated = await Student.findByIdAndUpdate(req.params.id, req.body, { new: true });
    res.json(updated);
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
});

// DELETE
router.delete('/:id', async (req, res) => {
  try {
    const deleted = await Student.findByIdAndDelete(req.params.id);
    res.json({ message: 'Student deleted', deleted });
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
});

module.exports = router;
