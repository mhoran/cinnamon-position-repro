Reproduction for https://github.com/linuxmint/cinnamon/issues/8546


## Prerequisite
1. Have python installed
2. Install `gi` package for python [per instructions](https://pygobject.readthedocs.io/en/latest/getting_started.html). For Ubuntu it would look like:

    2.1. Installing the system provided PyGObject:
    - Execute `sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0`

    2.2. Installing from PyPI with pip:
    - Execute `sudo apt install libgirepository1.0-dev gcc libcairo2-dev pkg-config python3-dev gir1.2-gtk-3.0` to install the build dependencies and GTK
    - Execute `pip3 install pycairo` to build and install Pycairo
    - Execute `pip3 install PyGObject` to build and install PyGObject
    
    2.3. In some cases the above solutions will not be enough and the program will still complain `ModuleNotFoundError: No module named 'gi'`. Running the following commands solves the running issue at least for some users:
    - `python3 -m pip install PyGObject`
    - `python3 -m pip install pycairo`


## Reproduction steps
1. Run main.py (run `python3 main.py` command from the terminal).
2. Close the window (either from the titlebar or via the Show/Hide toggle in the tray).
3. Note the saved position as 0, 0.
4. Reopen the window (either click the tray icon or select the Show/Hide toggle).
5. Note that the correct position is reported as being provided to window.move.
6. Note that the window is positioned below and to the right of the reported position.
7. Close the window
8. Note that the reported position does not correspond to the previously saved position.
9. Repeat as necessary.

## Example outputs
### Example 1
```
Saving position 0, 0
Moving to 0, 0
Saving position 1, 41
Moving to 1, 41
Saving position 2, 82
Moving to 2, 82
Saving position 3, 123
Moving to 3, 123
Saving position 4, 164
Moving to 4, 164
```

### Example 2
```
Saving position 0, 0
Moving to 0, 0
Saving position 1, 23
Moving to 1, 23
Saving position 2, 46
Moving to 2, 46
Saving position 3, 69
Moving to 3, 69
Saving position 4, 92
Moving to 4, 92
Saving position 5, 115
Moving to 5, 115
```
