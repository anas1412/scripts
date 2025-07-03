# Scripts

This repository contains a collection of command-line interface (CLI) scripts designed to enhance your productivity on Linux by leveraging the Gemini AI model.

## Installation (For Bash and Zsh Users)

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/anas1412/scripts.git
    cd scripts
    ```

2.  **Run the install script:**
    ```bash
    ./install
    ```
    This script will guide you through setting up your Gemini API key, installing dependencies, making scripts executable, and adding necessary aliases and paths to your `~/.bashrc` and `~/.zshrc` files.


## Scripts Overview

### `gemini_ai_helper.py`

*   **Purpose:** This script acts as a helpful, slightly tsundere Linux assistant. You provide a natural language query or goal, and it responds with a brief explanation and the most relevant raw shell command to achieve your objective.
*   **Usage:**
    ```bash
    gemini_ai_helper.py "How do I list all files in the current directory including hidden ones?"
    ```
*   **Example Output:**
    ```
    To list all files including hidden ones, use the 'ls' command with the '-a' option.
    ls -a
    ```

### `gemini_helper.py`

*   **Purpose:** This script is a silent command-line fixer. If a command fails, you can pipe its output to this script, and it will provide a raw, corrected shell command based on the error.
*   **Usage:**
    ```bash
    # Example of a failed command
    ls --nonexistent-option 2>&1 | try "ls --nonexistent-option" "$(cat -)"
    ```
    (Note: The `2>&1 | gemini_helper.py "..." "$(cat -)"` part is a common pattern to pass the failed command and its error output to the helper.)

### `blocker`

*   **Purpose:** This script manages domain blocking by modifying your `/etc/hosts` file. It redirects specified domains (and their `www.` counterparts) to `127.0.0.1`, effectively blocking access to them. It uses a special marker (`# --blocker-managed--`) to manage its own entries.
*   **Usage:**
    ```bash
    # Add one or more domains to block
    sudo blocker add example.com another.org

    # Remove one or more domains from blocking
    sudo blocker remove example.com

    # Edit an existing blocked domain (replaces old_domain with new_domain)
    sudo blocker edit old-domain.com new-domain.net

    # List all currently blocked domains managed by this script
    blocker list
    ```
    **Note:** This script requires `sudo` privileges for `add`, `remove`, and `edit` operations as it modifies `/etc/hosts`.

## Contributing

(Add information on how others can contribute to your scripts, e.g., bug reports, feature requests, pull requests.)

## License

(Specify the license under which these scripts are released, e.g., MIT, GPL.)