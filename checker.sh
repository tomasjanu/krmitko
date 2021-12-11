#!/bin/bash
DIR="/var/www/html/media"
inotifywait -m -r -e create "$DIR" | while read f

do
    # you may want to release the monkey after the test :)
    echo $f
    python slack.py $f
    # <whatever_command_or_script_you_liketorun>
done
