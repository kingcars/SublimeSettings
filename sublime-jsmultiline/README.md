sublime-jsmultiline
===================

Sublime plugin for creating multiline text arrays from selected text.

This plugin will take selected text and convert it to a javascript array of lines with a join() statement at the end.
For example, the following text
```
this is some text
 that spans multiple lines.
It even works with "double quotes", 'single quotes', and \backslashes\.
```
is converted to
```javascript
['this is some text',
' that spans multiple lines.',
'It even works with \"double quotes\", \'single quotes\', and \\backslashes\\.'].join('\n');
```
The new text remains selected and is suitable for cutting and pasting into a variable assignment such as,
```javascript
var mystring = ['this is some text',
' that spans multiple lines.',
'It even works with \"double quotes\", \'single quotes\', and \\backslashes\\.'].join('\n');
```
If multiple regions are selected, each region will be converted.

The default keybinding is ctrl-alt-j/super-alt-j

Enjoy!

License
-------
This package is licensed under the Apache License, version 2.  See LICENSE file for details.
