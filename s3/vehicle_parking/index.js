const express = require('express');
const bodyParser = require('body-parser');
const app = express();
require('dotenv').config();
const port = process.env.PORT || 3000;
const connection = require('./db')
const carRouter = require('./routes/car.routes')
app.use(bodyParser.json());

// Define routes here
app.use('/api', carRouter)

app.listen(port, async () => {
    try {
        await connection
        console.log("Database connection established")
    } catch (error) {
        console.log("Error in db connection")
    }
  console.log(`Server is running on port ${port}`);
});
