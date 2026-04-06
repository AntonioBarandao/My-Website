const mongoose = require('mongoose');

const studentSchema = new mongoose.Schema({
  name: { type: String, required: true },
  matricNo: { type: String, unique: true, required: true },
  department: String,
  level: Number,
  dateAdded: { type: Date, default: Date.now }
});

module.exports = mongoose.model('Student', studentSchema);
