A simple calculator as a floating window that always remains on top of other windows.

It was created for the purpose of quickly recalculating degrees according to the formula:
- If the original rotation value was positive, subtract it from 180 degrees.
- If the original rotation value was negative, add it to 180 degrees.

Features include:
- Automatically recalculates manually entered values
- The "paste" button feature detects whether the content in the clipboard is a number
- The result is automatically copied to the clipboard
- To use it, you just need to copy the degree value in another program, press the "paste" button, return to the other program and paste the new value

Initially it was written for GUI dearpygui, but was rewritten in tkinter because I couldn't implement keeping the window always on top in dearpygui.
