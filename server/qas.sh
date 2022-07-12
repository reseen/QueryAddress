#!/bin/bash
lock="qas.py"

start(){
    echo "qas service start..."
    python -u ~/qas/qas.py > ~/qas/qas.log &
    echo "qas service started"
}

stop(){
    echo "qas service stop..."
    pkill -f $lock
}

status(){
    if [ -e $lock ];then
        echo "$0 service start"
    else
	echo "$0 service stop"
    fi
}

restart(){
    stop
    start
}

case "$1" in
    "start")
	start
	;;
    "stop")
	stop
	;;
    "status")
	status
	;;
    "restart")
	restart
	;;
    *)
	echo "$0 start | stop | status | restart"
	;;
esac

