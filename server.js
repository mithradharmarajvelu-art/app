
const express = require("express");
const mongoose = require("mongoose");
const path = require("path");

const app = express();
const PORT = 3000;

// MongoDB connection string
const MONGO_URI = "mongodb://127.0.0.1:27017/studentDB";

// Middleware
app.use(express.json());
app.use(express.static(__dirname));

// Student schema
const studentSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true,
        trim: true
    },
    department: {
        type: String,
        required: true,
        trim: true
    }
});

const Student = mongoose.model("Student", studentSchema);

// Home page
app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, "index.html"));
});

// READ: Get all students
app.get("/students", async (req, res) => {
    try {
        const students = await Student.find();
        res.json(students);
    } catch (err) {
        console.error("Read error:", err.message);
        res.status(500).json({
            error: "Could not load students"
        });
    }
});

// CREATE: Register a student
app.post("/students", async (req, res) => {
    try {
        const name = req.body.name?.trim();
        const department = req.body.department?.trim();

        if (!name || !department) {
            return res.status(400).json({
                error: "Name and department are required"
            });
        }

        const student = await Student.create({
            name,
            department
        });

        console.log("Student created:", student.name);
        res.status(201).json(student);

    } catch (err) {
        console.error("Create error:", err.message);
        res.status(500).json({
            error: "Could not register student"
        });
    }
});

// UPDATE: Edit a student
app.put("/students/:id", async (req, res) => {
    try {
        const name = req.body.name?.trim();
        const department = req.body.department?.trim();

        if (!name || !department) {
            return res.status(400).json({
                error: "Name and department are required"
            });
        }

        const student = await Student.findByIdAndUpdate(
            req.params.id,
            { name, department },
            { new: true, runValidators: true }
        );

        if (!student) {
            return res.status(404).json({
                error: "Student not found"
            });
        }

        console.log("Student updated:", student.name);
        res.json(student);

    } catch (err) {
        console.error("Update error:", err.message);
        res.status(400).json({
            error: "Could not update student"
        });
    }
});

// DELETE: Remove a student
app.delete("/students/:id", async (req, res) => {
    try {
        const student = await Student.findByIdAndDelete(
            req.params.id
        );

        if (!student) {
            return res.status(404).json({
                error: "Student not found"
            });
        }

        console.log("Student deleted:", student.name);
        res.json({
            message: "Student deleted successfully"
        });

    } catch (err) {
        console.error("Delete error:", err.message);
        res.status(400).json({
            error: "Could not delete student"
        });
    }
});

// Connect to MongoDB and start the server
async function startServer() {
    try {
        await mongoose.connect(MONGO_URI);

        console.log("------------------------------------");
        console.log("STUDENT REGISTRATION BACKEND");
        console.log("------------------------------------");
        console.log("MongoDB Connection: " + MONGO_URI);
        console.log("Database Name: studentDB");
        console.log("MongoDB Status: Connected");

        app.listen(PORT, () => {
            console.log("Server running at http://localhost:" + PORT);
            console.log("------------------------------------");
        });

    } catch (err) {
        console.error("MongoDB connection failed:", err.message);
        process.exit(1);
    }
}

startServer();
