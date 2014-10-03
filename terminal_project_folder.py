import sublime
import sublime_plugin
from Terminal.Terminal import OpenTerminalCommand

class OpenTerminalInProjectFolderEnhanced(sublime_plugin.WindowCommand):
  def run(self, parameters = None):
    folders = self.window.folders()
    if len(folders) == 0:
      return

    command = OpenTerminalCommand(self.window)
    command.run(folders, parameters=parameters)