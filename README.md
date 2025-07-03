# Mari's CLI Toolkit: Smart Helpers for Your Linux Workflow

![GitHub last commit](https://img.shields.io/github/last-commit/anas1412/scripts?style=flat-square)
![GitHub top language](https://img.shields.io/github/languages/top/anas1412/scripts?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)

A collection of opinionated command-line utilities, enhanced with AI, to streamline your daily Linux tasks. It's not like I **want** to make your life easier, but someone has to do it, right?

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [`ai` command](#ai-command)
  - [`fix` command](#fix-command)
  - [`blocker` script](#blocker-script)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Notes](#notes)
- [Contributing](#contributing)
- [License](#license)
- [About the Maintainer](#about-the-maintainer)

## Features

*   **`ai` Command:** Get concise explanations and immediate raw commands directly from a helpful (but don't expect compliments) AI assistant. Perfect for when you need a quick answer without digging through man pages.
*   **`fix` Command:** Did your last command fail? Just type `fix`. This intelligent command will analyze the error and suggest a corrected command using AI, with an option to execute it immediately. It's less embarrassing than asking me every time.
*   **`blocker` Script:** Easily manage your `/etc/hosts` file to block unwanted websites. Great for staying focused or just, you know, not getting distracted by nonsense.
*   **Streamlined Installation:** A robust `install` script handles setting up dependencies, copying files, and configuring your shell environment, ensuring everything just... works. Don't worry, I made it robust enough even for you.

## Prerequisites

Before you start, make sure you have these essentials:

*   A Linux or macOS environment.
*   `git` installed (for cloning the repository).
*   `python3` and `pip3` installed.
*   A Google Gemini API key. You'll be prompted to enter this during the installation process.

## Installation

Getting these tools set up is straightforward. Just follow these steps:

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/anas1412/scripts.git
    cd scripts
    ```

2.  **Run the Installer:**
    ```bash
    chmod +x install
    ./install
    ```

    *   The script will prompt you to enter your Google Gemini API key.
    *   It will install the necessary Python dependency (`google-genai`) for your user.
    *   It will copy the scripts into `~/scripts/`.
    *   It will create and populate `~/scripts/shell_config.sh` with the `ai` alias and `fix` function.
    *   It will update your `~/.bashrc` and `~/.zshrc` files to:
        *   Export your `GEMINI_API_KEY`.
        *   Add `~/scripts/` to your system's `PATH`.
        *   Source the `~/scripts/shell_config.sh` file, making `ai` and `fix` available.

3.  **Activate Changes:**
    After the installation completes, you'll need to refresh your shell.
    ```bash
    source ~/.zshrc # If you use Zsh
    # OR
    source ~/.bashrc # If you use Bash
    # OR simply close and reopen your terminal window.
    ```

## Usage

Now that it's set up (you're welcome), here's how to use the commands.

### `ai` command

Ask the AI for quick Linux command help or general information. It'll give you a concise explanation and the command.

```bash
ai "how do I list all hidden files in my home directory"
```
```
# Expected output:
# To list all files including hidden ones in your home directory, use 'ls -a'.
# ls -a $HOME
```

### `fix` command


fix command
If your last command failed, just type fix. The AI will analyze the error and suggest a correction.
```bash
# Example of a failed command:
ls -lz # This command will likely fail if '-z' is not a valid option or context
```
```bash
# Output:
# ls: invalid option -- 'z'
# Try 'ls --help' for more information.
```
Now, run 'fix':
```bash
fix
```
```bash
# Expected output:
# Attempting to re-run: ls -lz
# The previous command failed (exit code 1).
# Sending details to AI for a suggested fix...
#
# AI suggests:
# ls -l
# Execute suggested command? (y/N): y
# # The suggested command 'ls -l' will then be executed.
```
### `blocker` script

blocker script
Manage entries in your /etc/hosts file. This script requires sudo internally, but you don't need to type sudo before blocker.

Add domains:
```bash
blocker add facebook.com twitter.com example.org
# Adds '127.0.0.1 facebook.com www.facebook.com # --blocker-managed--' (etc.) to /etc/hosts
```

List blocked domains:
```Bash
blocker list
# Expected output:
# facebook.com
# twitter.com
# example.org
```
Remove domains:
```bash
blocker remove facebook.com
```

Edit a domain:
```bash
blocker edit oldsite.com newsite.com
# Replaces 'oldsite.com' and 'www.oldsite.com' with 'newsite.com' and 'www.newsite.com'
```

Get help:
```bash
blocker help
# Expected output:
# Usage: blocker [add|remove|edit|list] <domain(s)> [new_domain]
```

Upon installation, the scripts are copied to ~/scripts/.

## Configuration
Your GEMINI_API_KEY is stored as an environment variable in your ~/.bashrc and ~/.zshrc. 

The install script handles this, so you shouldn't need to manually modify it unless your key changes.


The scripts are designed to live in ~/scripts/. If you move them manually, you'll need to update your PATH and the source command in your shell configuration files.


## Notes
The fix command relies on your shell's history, so ensure your shell's history configuration is functional.

The blocker script directly modifies /etc/hosts, which requires sudo permissions. The script incorporates sudo calls where necessary, so you're not prompted for a password for every individual change.

If you encounter issues with Python packages after pip3 install --user, ensure that ~/.local/bin is included in your PATH environment variable.

## Contributing
Feel free to open issues or submit pull requests. Just... try not to break things. And if you submit code, make sure it's clean and doesn't introduce more problems.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
