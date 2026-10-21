
const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors");

const app = express();

app.use(cors());
app.use(express.json());

mongoose.connect("mongodb://127.0.0.1:27017/VotingDB")
.then(() => console.log("MongoDB Connected"))
.catch(err => console.log(err));

const Candidate = mongoose.model("Candidate", {
    name: String,
    party: String,
    votes: { type: Number, default: 0 }
});

// CREATE
app.post("/candidates", async (req, res) => {
    const c = await Candidate.create(req.body);
    res.json(c);
});

// READ
app.get("/candidates", async (req, res) => {
    res.json(await Candidate.find());
});

// UPDATE
app.put("/candidates/:id", async (req, res) => {
    const c = await Candidate.findByIdAndUpdate(
        req.params.id, req.body, { new: true }
    );
    res.json(c);
});

// DELETE
app.delete("/candidates/:id", async (req, res) => {
    await Candidate.findByIdAndDelete(req.params.id);
    res.json({ message: "Deleted" });
});

// VOTE
app.post("/candidates/:id/vote", async (req, res) => {
    const c = await Candidate.findByIdAndUpdate(
        req.params.id, { $inc: { votes: 1 } }, { new: true }
    );
    res.json(c);
});

app.listen(5000, () => {
    console.log("Server running on port 5000");
});
