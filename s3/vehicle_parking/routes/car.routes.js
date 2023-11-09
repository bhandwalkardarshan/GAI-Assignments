const carRoutes = require('express').Router()
const ParkingSlot = require('../model/car.model'); // Import the model

// Route to create a parking slot
carRoutes.post('/create-slot', async (req, res) => {
  try {
    // Retrieve the slot number from the request body
    const { slotNumber } = req.body;

    // Check if the slot number is within the allowed range (1 to 5)
    if (slotNumber < 1 || slotNumber > 5) {
      return res.status(400).json({ message: 'Invalid slot number. Slot number must be between 1 and 5.' });
    }

    // Check if the slot with the specified number already exists
    const existingSlot = await ParkingSlot.findOne({ slotNumber });

    if (existingSlot) {
      return res.status(400).json({ message: 'Slot already exists.' });
    }

    // Create a new parking slot
    const newSlot = new ParkingSlot({ slotNumber });

    // Save the slot to the database
    await newSlot.save();

    return res.status(201).json({ message: 'Parking slot created successfully.' });
  } catch (error) {
    console.error('Error creating parking slot:', error);
    return res.status(500).json({ message: 'Error creating parking slot.' });
  }
});

// Route to park a car
carRoutes.patch('/park', async (req, res) => {
  // Retrieve the car number from the request
  const { carNumber } = req.body;

  try {
    // Find an available parking slot
    const availableSlot = await ParkingSlot.findOne({ isOccupied: false });

    if (!availableSlot) {
      return res.status(400).json({ message: 'Parking lot is full.' });
    }

    // Update the slot with the car number and mark it as occupied
    availableSlot.carNumber = carNumber;
    availableSlot.isOccupied = true;
    await availableSlot.save();

    return res.status(201).json({ message: 'Car parked successfully.' });
  } catch (error) {
    console.error('Error parking car:', error);
    return res.status(500).json({ message: 'Error parking car.' });
  }
});

// Route to unpark a car
carRoutes.patch('/unpark', async (req, res) => {
  // Retrieve the slot number from the request
  const { slotNumber } = req.body;

  try {
    // Find the parking slot by the specified slot number
    const parkingSlot = await ParkingSlot.findOne({ slotNumber });

    if (!parkingSlot) {
      return res.status(404).json({ message: 'Parking slot not found.' });
    }

    if (!parkingSlot.isOccupied) {
      return res.status(400).json({ message: 'Parking slot is already empty.' });
    }

    // Clear the slot by removing the car number and marking it as unoccupied
    parkingSlot.carNumber = null;
    parkingSlot.isOccupied = false;
    await parkingSlot.save();

    return res.status(200).json({ message: 'Car removed from the parking slot.' });
  } catch (error) {
    console.error('Error unparking car:', error);
    return res.status(500).json({ message: 'Error unparking car.' });
  }
});

// Route to get car/slot information
carRoutes.get('/info', async (req, res) => {
  // Retrieve the input (either slot number or car number)
  const slotNumber = req.query.slot;
  const carNumber = req.query.car_number;
  
  try {
    // Find the parking slot or car based on the input
    let info=undefined
    if(slotNumber){
      info = await ParkingSlot.findOne(
          { slotNumber: slotNumber },
          );
    }
    if(carNumber){
      info = await ParkingSlot.findOne(
          { carNumber: carNumber },
          );
    }
    

    if (!info) {
      return res.status(404).json({ message: 'Car or parking slot not found.' });
    }

    return res.status(200).json({ info });
  } catch (error) {
    console.error('Error getting car/slot information:', error);
    return res.status(500).json({ message: 'Error getting car/slot information.' });
  }
});

  module.exports  = carRoutes