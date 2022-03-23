#!/bin/bash
shopt -s extglob
BLOG_ROOT=$(pwd)
ABSPATH=$(realpath "$1")
cd "$ABSPATH"

for file in !([[:digit:]][[:digit:]][[:digit:]][[:digit:]]-*); do
    cd "$ABSPATH"
    OLD=$1/$file
    NEW=$1/$(sed -n "s/.*:date: \([0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\}\).*/\1/p" $file)-$file
    echo "OLD: $OLD"
    echo "NEW $NEW"
    cd $BLOG_ROOT
    poetry run invoke movefile --old "$OLD" --new "$NEW"
done

