# Installation of Sense HAT

## Pros and Cons
This very cool HAT add-on board for the Pi is a really well built toy. You can do a lot of experiments, and run a lot of funny Python code to learn with it.

But I should mention that, as it sits above the processor, it will run quite hot and your temperature mesures might not represent the actual room temperature.

## Installation
The [Sense HAT](https://pythonhosted.org/sense-hat/) _should_ be supported out of the box, by simply executing the following commands:
```shell
$ sudo apt-get update
$ sudo apt-get install sense-hat
$ sudo reboot
```

If you get console errors when using it, please read on.

## Execution errors on newest releases of Raspbian
I say _it should work_, because sadly since the newest Raspbian releases have a Python version bigger than 3.5.5, we need to do some manual work in order to get the temperature, humidity and pressure sensors to work: we need to download, compile and then install the RTIMU library. Big thanks to **Emeric Planet** for his answer on [this thread](https://github.com/astro-pi/python-sense-hat/issues/58#issuecomment-374414765).

Warning: you need to be on your Pi environment to do the following steps, as it will compile it for the system where this step is run.

First, activate PiNode's virtual environment:

```shell
$ source pinode-env/bin/activate
```

Then navigate to your home directory to clone the library, compile it and then install it:

```shell
$ git clone https://github.com/RPi-Distro/RTIMULib/ RTIMU
$ cd RTIMU/Linux/python
$ python setup.py install
$ python setup.py build
```