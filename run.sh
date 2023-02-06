#!/bin/bash

logKill() {
  echo >&2 "[ERROR] $@" && exit 1
}

# param $1: command 동작을 확인하려는 대상
# example $1: "multipass", "kubectl", ...
checkPrerequisite() {
  local _silentRun_=$($@ | grep "command not found: $@" && logKill "$@ unavailable")
  unset _silentRun_
}

if [ -z $1 ]; then
  logKill "give a index for running flask code (Ex. bash run.sh 01, bash run.sh 02, ...)"
else
  __INDEX__=$1
fi

__TARGET__=$(ls tutorials | grep $__INDEX__)
__APP__="--app tutorials/$__TARGET__"
__RUN__="python3 -m flask"
__DEBUG__="--debug"
__BIND__="--host=0.0.0.0"
__PORT__="--port=5000"

checkPrerequisite "$__RUN__ --help $__APP__"

$__RUN__ $__APP__ $__DEBUG__ run $__BIND__ $__PORT__
