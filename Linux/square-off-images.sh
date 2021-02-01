#!/bin/bash
# Author:        Andrew St Clair
# Usage:         ./square-off-images.sh
# Example:       ./square-off-images.sh
# Description:   Gets width and height of image and sets the smallest to the largest
# Requires:      ImageMagick

# Replace spaces in file and folder names with hyphens
find -name "* *" -type f | rename 's/ /-/g'
find -name "* *" -type d | rename 's/ /-/g'

# Find all files in current folder and subfolders with the extension .png or .jpg
for file in $(find -name "*.png" -or -name "*.jpg" -type f)
do
    # Identify image dimentions
    x=$(identify "${file}" | cut -d " " -f 3 | cut -d "x" -f 1)
    y=$(identify "${file}" | cut -d " " -f 3 | cut -d "x" -f 2)
    # Format data for printing later
    pfile=$(printf "%-70s\n" "${file}")
    px=$(printf "%10s\n" "${x}")
    py=$(printf "%-10s\n" "${y}")
    ix=$(printf "%-10s\n" "${x}")
    iy=$(printf "%10s\n" "${y}")
    if (( x > y )); then
        # X is bigger so use it to set image size
        echo -e "${pfile}\t${px} x ${py}\tSetting to ${px} x ${ix}"
        convert "${file}" -gravity center -background transparent -extent ${x}x${x} "${file}"
    elif (( y > x )); then
        # Y is bigger so use it to set image size
        echo -e "${pfile}\t${px} x ${py}\tSetting to ${iy} x ${py}"
        convert "${file}" -gravity center -background transparent -extent ${y}x${y} "${file}"
    else
        # Dimentions are the same, ignore file but print its name and dimentions
        echo -e "${pfile}\t${px} x ${py}"
    fi
done
