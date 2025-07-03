# CLI AI Helper Scripts

This repository contains a collection of command-line interface (CLI) scripts designed to enhance your productivity on Linux by leveraging the Gemini AI model.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/anas1412/scripts.git
    cd your-repo-name
    ```
    (Replace `https://github.com/your-username/your-repo-name.git` with the actual URL if this is a public repository, or instruct the user to copy the files if it's not.)

2.  **Install dependencies:**
    These scripts require the `google-generativeai` Python library.
    ```bash
    pip install google-generativeai
    ```

3.  **Set up API Key:**
    You need a Google Gemini API key. Obtain one from [Google AI Studio](https://aistudio.google.com/app/apikey).
    Set it as an environment variable:
    ```bash
    export GOOGLE_API_KEY="YOUR_API_KEY"
    ```
    For persistence, add this line to your `~/.bashrc` or `~/.zshrc` file.

4.  **Make scripts executable:**
    ```bash
    chmod +x gemini_ai_helper.py gemini_helper.py blocker
    ```

5.  **Add to PATH (Optional but Recommended):**
    To run the scripts from any directory, add the scripts directory to your system's PATH.
    ```bash
    echo 'export PATH="$PATH:/home/nas/scripts"' >> ~/.bashrc
    source ~/.bashrc
    ```
    (Replace `/home/nas/scripts` with the actual path where you cloned the repository.)

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

*   **Purpose:** This script is a silent command-line fixer. If a command fails, you can pipe its output to this script, and it will provide a raw, corrected shell command based on the error. It provides no explanation, only the fix.
*   **Usage:**
    ```bash
    # Example of a failed command
    ls --nonexistent-option 2>&1 | gemini_helper.py "ls --nonexistent-option" "$(cat -)"
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
