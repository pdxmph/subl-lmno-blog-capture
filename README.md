# lmno.lol Blog Capture for Sublime Text

A simple Sublime Text plugin to quickly write Markdown blog posts into a single [lmno.lol][] file.
Posts are prepended so the newest entries appear at the top.

---

## Features

* Prompt for post title and date
* Open a scratch buffer in Markdown mode
* Finalize to save (prepended to your destination file)
* Abort without saving
* User-configurable destination path via settings

---

## Default Key Bindings

<details>
<summary>macOS (Default (OSX).sublime-keymap)</summary>

```json
[
  { "keys": ["super+alt+b"], "command": "lmno_capture_post"      },
  { "keys": ["super+alt+f"], "command": "lmno_finalize_capture" },
  { "keys": ["super+alt+a"], "command": "lmno_abort_capture"    }
]
```

</details>

<details>
<summary>Windows (Default (Windows).sublime-keymap)</summary>

```json
[
  { "keys": ["ctrl+alt+b"], "command": "lmno_capture_post"      },
  { "keys": ["ctrl+alt+f"], "command": "lmno_finalize_capture" },
  { "keys": ["ctrl+alt+a"], "command": "lmno_abort_capture"    }
]
```

</details>

<details>
<summary>Linux (Default (Linux).sublime-keymap)</summary>

```json
[
  { "keys": ["ctrl+alt+b"], "command": "lmno_capture_post"      },
  { "keys": ["ctrl+alt+f"], "command": "lmno_finalize_capture" },
  { "keys": ["ctrl+alt+a"], "command": "lmno_abort_capture"    }
]
```

</details>

---

## Installation

1. **Manual**

   * Copy `lmno_blog_capture.sublime-package` into your `Installed Packages/` folder.
   * Restart Sublime Text.

2. **Package Control**
   *(coming soon)*

---

## Configuration

Override the default destination in your user settings:

1. Open **Preferences → Package Settings → LMNO Blog Capture → Settings – User**
2. Add or modify:

```json
{
  "destination_path": "~/path/to/your/posts.md"
}
```

---

## Usage

1. Press **Start Capture** (e.g. ⌘ ⌥ B or Ctrl Alt B).
2. Enter your post title.
3. Write your content in the new scratch buffer.
4. Press **Finalize** (e.g. ⌘ ⌥ F or Ctrl Alt F) to prepend and save.
5. Or press **Abort** (e.g. ⌘ ⌥ A or Ctrl Alt A) to cancel.

---

## License

MIT © Mike Hall
Feel free to fork and improve!

[lmno.lol]: https://lmno.lol