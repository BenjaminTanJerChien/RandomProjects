@echo off 
title Push to git shortcut
set /P commit_message="Commit Message: "
git add .
git commit -m "%commit_message%"
git push origin master
pause 