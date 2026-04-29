#!/bin/bash

set -e

# Get current branch
branch_name=$(git rev-parse --abbrev-ref HEAD)

echo "Current branch: $branch_name"

# -----------------------------
# Difficulty (1–10)
# -----------------------------
while true; do
  read -p "Difficulty (1-10): " difficulty
  if [[ "$difficulty" =~ ^([1-9]|10)$ ]]; then
    break
  else
    echo "Enter a number 1-10."
  fi
done

# -----------------------------
# Reflection choice
# -----------------------------
echo "Reflection:"
echo "1) am confident in this algorithm"
echo "2) read over the explanation for a refresher"
echo "3) do this problem again"

while true; do
  read -p "Choice (1-3): " choice
  case $choice in
    1) reflection="am confident in this algorithm"; break ;;
    2) reflection="read over the explanation for a refresher"; break ;;
    3) reflection="do this problem again"; break ;;
    *) echo "Invalid choice" ;;
  esac
done

# -----------------------------
# Git add (A: git add .)
# -----------------------------
git add .

# -----------------------------
# Commit message (simple + | separators)
# -----------------------------
git commit -m "solved the $branch_name problem | $difficulty/10 | $reflection"

# -----------------------------
# Push branch
# -----------------------------
git push --set-upstream origin "$branch_name"

# -----------------------------
# Confirm merge
# -----------------------------
read -p "Merge into main? (y/n): " merge_confirm
if [[ "$merge_confirm" != "y" ]]; then
  echo "Stopping before merge."
  exit 0
fi

git checkout main
git merge "$branch_name"
git push

# -----------------------------
# Confirm deletion
# -----------------------------
read -p "Delete branch locally and remotely? (y/n): " delete_confirm

if [[ "$delete_confirm" == "y" ]]; then
  git push --delete origin "$branch_name"
  git branch -d "$branch_name"
  echo "Branch deleted."
else
  echo "Branch kept."
fi

echo "Done."