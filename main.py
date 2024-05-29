""""Demonstrates the use of the Smiley class and its subclasses.
If you have access to a SenseHAT (either via a Raspberry Pi or a SenseHAT emulator), you can use the real SenseHAT class instead of the mock SenseHAT class.
That is, delete the sense_hat.py file that is included in this bundle."""

from angry import Angry

if __name__ == '__main__':

    smiley = Angry()


    smiley.show()

    time.sleep(1)


    smiley.blink()
