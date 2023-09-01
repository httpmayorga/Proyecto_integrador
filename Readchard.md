Documentation
There are just two methods:

readchar.readchar() -> str
Reads one character from stdin, returning it as a string with length 1. Waits until a character is available.

As only ASCII characters are actually a single character, you usually want to use the next function, that also handles longer keys.

readchar.readkey() -> str
Reads the next keystroke from stdin, returning it as a string. Waits until a keystroke is available.

A keystroke can be:

single characters as returned by readchar(). These include:
character for normal keys: a, Z, 9,...
special characters like ENTER, BACKSPACE, TAB,...
combinations with CTRL: CTRL+A,...
keys that are made up of multiple characters:
characters for cursors/arrows: 🡩, 🡪, 🡫, 🡨
navigation keys: INSERT, HOME,...
function keys: F1 to F12
combinations with ALT: ALT+A,...
combinations with CTRL and ALT: CTRL+ALT+SUPR,...
Note CTRL+C will not be returned by readkey(), but instead raise a KeyboardInterupt. If you what to handle it yourself, use readchar().

readchar.key module
This submodule contains a list of available keys to compare against. The constants are defined depending on your operating system, so it should be fully portable. If a key is listed here for your platform, readkey() can read it, and you can compare against it.

readchar.config class
This static class contains configurations for readchar. It holds constants that are used in other parts of the code as class attributes. You can override/change these to modify its behaviour. Here is a description of the existing attributes:

INTERRUPT_KEYS
List of keys that will result in readkey() raising a KeyboardInterrupt.
Default: [key.CTRL_C]
