#!/bin/bash
# token.sh - Estimate token count for text input from stdin or file
# Usage: echo "text to count" | ./token.sh
#        or ./token.sh filename.txt

# Function to count tokens using simple whitespace/character estimation
count_tokens() {
  local text="$1"
  local char_count=${#text}
  local word_count=$(echo "$text" | wc -w)

  # Simple estimation: ~0.75 tokens per word + additional tokens for punctuation and special chars
  # Approximate 4 chars per token
  local estimated_tokens=$(((char_count + 1) / 4))

  echo $estimated_tokens
}

# Check if input is from pipe or file
if [ -t 0 ]; then
  # Input from file argument
  if [ $# -eq 0 ]; then
    echo "Error: No file provided" >&2
    echo "Usage: skogcli misc run token filename.txt" >&2
    echo "       echo 'text' | ./token.sh" >&2
    exit 1
  fi

  if [ ! -f "$1" ]; then
    echo "Error: File $1 not found" >&2
    exit 1
  fi

  # Read file content
  content=$(cat "$1")
else
  # Input from pipe
  content=$(cat)
fi

# Count and output tokens
count_tokens "$content"
