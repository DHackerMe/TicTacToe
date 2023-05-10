#!/bin/bash
# Update Script for TicTacToe by DHackerMe

command -v git > /dev/null 2>&1 || { echo >&2 "Package GIT is not installed, install it to continue"; exit 1; }

clear
printf "\n \e[1;92mUpdating \e[1;94mTicTacToe\e[1;92m directory...\n\n"
sleep 1.5
cd ..
rm -rf TicTacToe
git clone https://github.com/DHackerMe/TicTacToe
printf "\n\e[1;92m Update Complete\n\e[0m"