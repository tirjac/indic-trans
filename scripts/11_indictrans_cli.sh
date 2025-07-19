#!/bin/bash
export SRCDIR=$(dirname $(cd ${0%/*} 2>>/dev/null ; echo `pwd`/${0##*/}))
. ${SRCDIR}/00_script_config.sh

# main
if [ $# -ne 3 ] ; then echo "Usage: $0 <source> <target> <query>" ; exit 1 ; fi
python src/indictrans/apps/indictrans_cli.py -s $1 -t $2 -q "$3"
python src/indictrans/apps/indictrans_cli.py -r -s $1 -t $2 -q "$3"
