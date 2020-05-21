# Add a new sensor to your Node

It is easy to add any kind of sensor. Follow these steps to get you started.

If you want to share your new sensor's code with the community, please get in touch or submit a pull request :-)

## Create the class
- In the `nodes/sensors` folder, create a file with the same name as your sensor (it cannot start with a number)
- As an example, you can copy the content of the `sense_hat.py` file in your new file
- Write the documentation and code you'd like
- Change the `name` property to your liking
- Most importantly, implement the method `_read_data(self)` to return the data from your sensor
- Implement the method `get_protocol(self)` to return the protocol used by your sensor
- In `nodes/sensors/__init.py__`, add your class in the `SENSOR_CLASSES` List.
It should be in the form `(<classname>, <path to your file>)`

# Configure your node for this new class
This part will come later ;-)