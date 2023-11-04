const userRoutes = require('express').Router()
const nodemailer = require('nodemailer');
const bcrypt = require('bcrypt');
const User = require('../model/user.model');

const transporter = nodemailer.createTransport({
  service: 'Gmail',
  auth: {
    user: process.env.mail,
    pass: process.env.pass,
  },
});


userRoutes.post('/signup', async (req, res) => {
    const { email, password } = req.body;
  console.log(email, password)
    // Add validation for email and password
    if (!email || !password) {
      return res.status(400).json({ message: 'Email and password are required.' });
    }
  
    try {
        // Check if the user with the same email already exists
        const existingUser = await User.findOne({ email });

        if (existingUser) {
        return res.status(409).json({ message: 'User with this email already exists.' });
        }
      const hashedPassword = await bcrypt.hash(password, 10);
      const user = new User({ email, password: hashedPassword });
      await user.save();
      // Send a welcome email here
      const mailOptions = {
        from: process.env.mail,
        to: email,
        subject: 'Welcome to Your App',
        text: 'Welcome to our app! We are excited to have you on board.',
      };
  
      transporter.sendMail(mailOptions, (error, info) => {
        if (error) {
          console.log('Email sending failed:', error);
        } else {
          console.log('Email sent:', info.response);
        }
      });

      res.status(201).json({ message: 'User registered successfully.' });
    } catch (error) {
      res.status(500).json({ message: 'Error registering the user.' });
    }
  });
  
  module.exports  = userRoutes