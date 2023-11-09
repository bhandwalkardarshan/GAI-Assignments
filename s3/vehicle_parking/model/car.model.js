const mongoose = require('mongoose');

// Define the ParkingSlot schema
const parkingSlotSchema = new mongoose.Schema({
  slotNumber: { type: Number, required: true, unique: true, enum: [1, 2, 3, 4, 5] },
  carNumber: { type: String, default: null },
  isOccupied: { type: Boolean, default: false },
});

// Create the ParkingSlot model
const ParkingSlot = mongoose.model('ParkingSlot', parkingSlotSchema);

module.exports = ParkingSlot;
