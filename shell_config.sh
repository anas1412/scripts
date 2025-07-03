# --- Custom Shell Functions and Aliases managed by install script ---

# AI Helper Alias
alias ai='python3 "$HOME/scripts/gemini_ai_helper.py"'

# Fix Command Function
fix() {
    local last_command
    local command_output
    local exit_status
    local scripts_dir="$HOME/scripts"

    # Get the last command from history
    if [ -n "$ZSH_VERSION" ]; then
        last_command=$(print -r -- "${history[$(($HISTCMD-1))]}")
    elif [ -n "$BASH_VERSION" ]; then
        last_command=$(history -p '!!' 2>/dev/null)
    else
        echo "Error: Unsupported shell. Cannot determine last command for 'fix' function." >&2
        return 1
    fi

    # Basic check to prevent fixing 'fix' itself, or empty commands
    if [[ -z "$last_command" || "$last_command" == "fix" ]]; then
        echo "No meaningful previous command to fix." >&2
        return 1
    fi

    echo "Attempting to re-run: $last_command"
    local tmp_output=$(mktemp)
    if [ $? -ne 0 ]; then
        echo "Error: Failed to create temporary file for command output. Check permissions or disk space." >&2
        return 1
    fi
    if eval "$last_command" >"$tmp_output" 2>&1; then
        exit_status=0
    else
        exit_status=$?
    fi
    command_output=$(cat "$tmp_output")
    rm -f "$tmp_output" # Use -f to suppress errors if file doesn't exist

    if [ $exit_status -eq 0 ]; then
        echo "The previous command completed successfully (exit code 0). No AI fix needed."
    else
        echo "The previous command failed (exit code $exit_status)."
        echo "Sending details to AI for a suggested fix..."
        local suggested_command

        suggested_command=$(python3 "$scripts_dir/gemini_try_helper.py" "$last_command" "$command_output")

        if [ -n "$suggested_command" ]; then
            echo -e "\nAI suggests:\n$suggested_command"
            read -p "Execute suggested command? (y/N): " -n 1 -r
            echo
            if [[ $REPLY =~ ^[Yy]$ ]]; then
                eval "$suggested_command"
            else
                echo "AI suggestion not executed."
            fi
        else
            echo "AI did not provide a suggestion or an error occurred with the AI helper."
        fi
    fi
    return $exit_status
}

# --- End Custom Shell Functions and Aliases ---
