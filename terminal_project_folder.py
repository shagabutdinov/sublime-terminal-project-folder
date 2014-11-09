import sublime
import sublime_plugin

try:
  from Terminal.Terminal import OpenTerminalCommand
except ImportError:
  sublime.error_message("Dependency import failed; please read readme for " +
    "TerminalProjectFolder plugin for installation instructions; to disable " +
    "this message remove this plugin")


class OpenTerminalInProjectFolderEnhanced(sublime_plugin.WindowCommand):
  def run(self, parameters = None):
    folders = self.window.folders()
    if len(folders) == 0:
      return

    command = OpenTerminalCommand(self.window)
    command.run(folders, parameters=parameters)