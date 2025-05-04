import os
import sublime
import sublime_plugin
from datetime import datetime

SETTINGS_FILE = "lmno_blog_capture.sublime-settings"

class LmnoCapturePostCommand(sublime_plugin.WindowCommand):
    """Start a new blog post capture by prompting for a title and opening a scratch buffer."""
    def run(self):
        self.window.show_input_panel("Post title:", "", self.on_done, None, None)

    def on_done(self, title):
        date = datetime.now().strftime("%Y-%m-%d")
        heading = "# [{}] {}\n\n".format(date, title)
        view = self.window.new_file()
        view.set_name("LMNO Blog Capture")
        view.set_scratch(True)
        view.settings().set("lmno_capture", True)
        view.run_command("lmno_insert_heading", {"heading": heading})
        view.set_syntax_file("Packages/Markdown/Markdown.sublime-syntax")
        sublime.status_message("Writing post… press finalize or abort shortcuts.")

class LmnoInsertHeadingCommand(sublime_plugin.TextCommand):
    """Insert the generated heading into the capture buffer."""
    def run(self, edit, heading):
        self.view.insert(edit, 0, heading)

class LmnoFinalizeCaptureCommand(sublime_plugin.TextCommand):
    """Prepend the capture buffer contents to the destination file and close the buffer."""
    def run(self, edit):
        if not self.view.settings().get("lmno_capture"):
            return

        content = self.view.substr(sublime.Region(0, self.view.size()))

        settings = sublime.load_settings(SETTINGS_FILE)
        dest = os.path.expanduser(settings.get("destination_path"))

        # Read existing contents with UTF-8 encoding
        try:
            with open(dest, "r", encoding="utf-8") as f:
                existing = f.read()
        except FileNotFoundError:
            existing = ""
        except UnicodeDecodeError:
            sublime.error_message("Error decoding {}: non-UTF8 bytes detected".format(dest))
            return
        except Exception as e:
            sublime.error_message("Error reading {}:\n{}".format(dest, e))
            return

        # Write new top-prepended file with UTF-8 encoding
        try:
            with open(dest, "w", encoding="utf-8") as f:
                f.write(content + "\n\n" + existing)
        except Exception as e:
            sublime.error_message("Error writing {}:\n{}".format(dest, e))
            return

        self.view.close()
        sublime.status_message("Blog post saved to {}".format(dest))

class LmnoAbortCaptureCommand(sublime_plugin.TextCommand):
    """Cancel the capture and close the buffer without saving."""
    def run(self, edit):
        if not self.view.settings().get("lmno_capture"):
            return
        self.view.close()
        sublime.status_message("Blog capture aborted.")

# Plugin load hook

def plugin_loaded():
    print("✅ lmno_blog_capture loaded")
