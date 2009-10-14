#!/bin/sh
GAE_PATH=~/devel/google_appengine/
APP_PATH=$(pwd)
ADDRESS=127.0.0.1
DB=./datastore
DB_HISTORY=./datastore.history
 
$GAE_PATH/dev_appserver.py -a $ADDRESS --datastore_path=$DB --history_path=$DB_HISTORY $APP_PATH

# with default datastore in /tmp
#$GAE_PATH/dev_appserver.py -a $ADDRESS $APP_PATH
