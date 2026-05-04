#!/bin/bash

set -e

# -----------------------------
# Raw input (NEVER modify this)
# -----------------------------
read -p "Enter problem name (e.g. #48 Rotate Image): " raw_name

if [[ -z "$raw_name" ]]; then
  echo "Name cannot be empty."
  exit 1
fi

# -----------------------------
# Difficulty input
# -----------------------------
while true; do
  read -p "Enter difficulty (EASY/MEDIUM/HARD): " difficulty
  difficulty=$(echo "$difficulty" | tr '[:lower:]' '[:upper:]')

  if [[ "$difficulty" == "EASY" || "$difficulty" == "MEDIUM" || "$difficulty" == "HARD" ]]; then
    break
  else
    echo "Invalid input. Please enter EASY, MEDIUM, or HARD."
  fi
done

# -----------------------------
# Branch name (cleaned version)
# -----------------------------
branch_name=$(echo "$raw_name" \
  | sed 's/#//g' \
  | tr '[:upper:]' '[:lower:]' \
  | tr ' ' '-' \
  | sed 's/[^a-z0-9-]//g')

# -----------------------------
# Folder name (UNCHANGED)
# -----------------------------
folder_name="$raw_name"

echo "Branch: $branch_name"
echo "Folder: $folder_name"
echo "Difficulty: $difficulty"

# -----------------------------
# Create branch
# -----------------------------
git checkout -b "$branch_name"

# -----------------------------
# Create folder (must quote because of spaces/#)
# -----------------------------
mkdir -p "$folder_name"

# -----------------------------
# explanation.md
# -----------------------------
cat <<EOF > "$folder_name/explanation.md"
# $raw_name - Explanation

Write your explanation here.
EOF

# -----------------------------
# instructions.txt
# -----------------------------
cat <<EOF > "$folder_name/instructions.txt"
DIFFICULTY: $difficulty

Problem instructions go here.
EOF

# -----------------------------
# solution.py
# -----------------------------
cat <<EOF > "$folder_name/solution.py"
def solution():
    # write code here
    pass


print(solution())
EOF

echo "Setup complete."
echo "Branch: $branch_name"
echo "Folder: $folder_name"
echo "Difficulty: $difficulty"