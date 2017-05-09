import sublime
import sublime_plugin

try:
  from Terminal.Terminal import OpenTerminalCommand
except ImportError as error:
  sublime.error_message("Dependency import failed; please read readme for " +
    "TerminalProjectFolder plugin for installation instructions; to disable " +
    "this message remove this plugin; message: " + str(error))
  raise error

class OpenTerminalInProjectFolderEnhanced(sublime_plugin.WindowCommand):
  def run(self, parameters = None):
    folders = self.window.folders()

    view = self.window.active_view()
    if view != None:
      folder = view.settings().get('terminal_project_folder', None)
      if folder != None:
        folders.insert(0, folder)


    if len(folders) == 0:
      return

    command = OpenTerminalCommand(self.window)
    command.run(folders, parameters=parameters)