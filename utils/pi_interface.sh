#!/usr/bin/env bash


if [ "$1" == "Deploy" ]; then
ssh_output=$(
ssh -t -q luke-robotics <<ENDSSH
    cd ~/Documents/project-bowling/
    echo "Pulling from Repository..." >&2
    hg pull
    hg update
    echo "Current repo state deployed on PI" >&2
ENDSSH
)
fi
#echo $home_dir
#echo $name_dir
