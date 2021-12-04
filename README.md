Reproduction for https://github.com/linuxmint/cinnamon/issues/8546

Reproduction steps:

1. Run main.py.
2. Close the window (either from the titlebar or via the Show/Hide toggle in the tray).
3. Note the saved position as 0, 0.
4. Reopen the window (either click the tray icon or select the Show/Hide toggle).
5. Note that the correct position is reported as being provided to window.move.
6. Note that the window is positioned below and to the right of the reported position.
7. Close the window
8. Note that the reported position does not correspond to the previously saved position.
9. Repeat as necessary.


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
