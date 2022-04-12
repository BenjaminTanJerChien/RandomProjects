@echo off 
title Push to git shortcut

git add .
git commit -m "Added shortcut"
git push origin master
pause 
cls
pause