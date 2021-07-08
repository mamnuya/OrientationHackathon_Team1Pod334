#!/bin/bash
echo "Checking register page: "
curl 'https://rinkisportfolio.duckdns.org/register' && curl 'https://rinkisportfolio.duckdns.org/login' && curl 'https://rinkisportfolio.duckdns.org/health' && curl --request POST 'https://rinkisportfolio.duckdns.org/register' 
if [ $?==0 ]
then
 exit 0
else
 exit 1
fi

