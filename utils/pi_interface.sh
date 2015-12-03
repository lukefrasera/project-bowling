#!/usr/bin/env bash

SCRIPT=`basename ${BASH_SOURCE[0]}`

OPT_D=false
OPT_R=false

NORM=`tput sgr0`
BOLD=`tput bold`
REV=`tput smso`

function HELP {
  echo -e \\n"Usage of: ${BOLD}${SCRIPT}.${NORM}"\\n
  echo "Commands:"
  echo "-d	- Deploy current Bitbucket Repo state to RaspberryPi"
  echo "-r	- Run current RaspberryPi Repo state"
  echo "EXAMPLE:"
  echo "./${BOLD}${SCRIPT} -r${NORM}"
  echo "./${BOLD}${SCRIPT} -d${NORM}"
}

NUMARGS=$#
if [ ${NUMARGS} -eq 0 ]; then
  HELP
  exit
fi

while getopts "rd" FLAG; do
  case $FLAG in
    r)
      OPT_R=true
      ;;
    d)
      OPT_D=true
      ;;
    \?)
      echo "Unrecognized Option"
      HELP
      exit
      ;;
  esac
done

shift $((OPTIND-1))

HOST="raspberrypi.local"
COUNT=$(ping -c 1 ${HOST} | grep 'received' | awk -F',' '{ print $2 }' | awk '{ print $1 }')

if [ "$COUNT" = "" ]; then
  echo "Raspberry Pi not found!"
  exit 
fi
if [ $COUNT = 0 ]; then
  echo "Can't find Raspberry pi. check connection"
  exit
fi

if [ $OPT_D = true ]; then
ssh_output=$(
ssh -t -q turkey@raspberrypi.local <<ENDSSH
    cd ~/Documents/project-bowling/
    echo "Pulling from Repository..." >&2
    hg pull
    hg update
    echo "Current repo state deployed on PI" >&2
ENDSSH
)
fi

if [ $OPT_R = true ]; then
ssh_run=$(
ssh -t -q turkey@raspberypi.local <<ENDSSH2
  sh /Documents/project-bowling/utils/run.sh >&2
ENDSSH2
)
fi
