const express = require("express");
const mongoose = require("mongoose");
const bodyParser = require("body-parser"); 
require("dotenv/config");
const app = express();
const postsRoute = require("./routes/posts");
const cors = require("cors");


app.use(cors());
app.use(bodyParser.json());
app.use("/posts", postsRoute);

app.get("/", (req, res) => {
  res.send("We are on home");
});

mongoose.connect(process.env.DB_CONNECTION, 
{ useNewUrlParser: true }
);

app.listen(3000);