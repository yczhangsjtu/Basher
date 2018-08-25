#!/bin/bash

backups="scripts/perl/autoclean.conf"

if [ -n "$BASHER" ] && [ "$1" != "reinstall" ] ; then
	echo "Already installed"
	exit 1
fi

target_dir=$HOME/.basher
if ! [ -d $target_dir ]; then
	mkdir -p $target_dir
else
  for backup in $backups; do
    tmpfile=`echo $backup | md5`
    [ -f $target_dir/$backup ] && cp $target_dir/$backup /tmp/$tmpfile
  done
	rm -r $target_dir/*
fi

cp -R ./scripts ./config basher.bashrc $target_dir

for backup in $backups; do
  tmpfile=`echo $backup | md5`
  [ -f /tmp/$tmpfile ] && mv /tmp/$tmpfile $target_dir/$backup
done

if ! [ -n "$BASHER" ]; then
	echo "Please append the following into your .bashrc file:"
	echo "  . ~/.basher/basher.bashrc"
fi
