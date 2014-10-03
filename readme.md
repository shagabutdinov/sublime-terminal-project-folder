# Sublime TerminalProjectFolder plugin

Provides workaround to open terminal in project folder if no view opened in
sublime. Always open terminal for first folder of project.


### Reason

I was not sure that how default "open_terminal_in_project_folder" is intended to
work so I did this microplugin.


### Installation

This plugin is part of [sublime-enhanced](http://github.com/shagabutdinov/sublime-enhanced)
plugin set. You can install sublime-enhanced and this plugin will be installed
automatically.

If you would like to install this package separately check "Installing packages
separately" section of [sublime-enhanced](http://github.com/shagabutdinov/sublime-enhanced)
package.


### Features

Opens terminal for first project folder.


### Commands

| Description                     | Keyboard shortcut | Command palette                                        |
|---------------------------------|-------------------|--------------------------------------------------------|
| Open terminal                   | ctrl+f12          | TerminalProjectFolder: open terminal                   |
| Open terminal in project folder | f12               | TerminalProjectFolder: open terminal in project folder |


### Dependencies

- https://github.com/wbond/sublime_terminal