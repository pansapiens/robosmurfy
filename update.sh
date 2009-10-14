#!/bin/sh
GAE_PATH=$HOME/devel/google_appengine/
APP_PATH=$(pwd)
#EMAIL=

#$GAE_PATH/appcfg.py --email=$EMAIL update $APP_PATH
$GAE_PATH/appcfg.py update $APP_PATH

