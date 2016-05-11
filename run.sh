#!/bin/bash

MYDIR="$(dirname "$(realpath "$0")")"
cd $MYDIR

$MYDIR/hb.py >> $MYDIR/log
