#!/bin/bash

if [ -n "$BASHER" ] && [ "$1" != "reinstall" ] ; then
	echo "Already installed"
	exit 1
fi

target_dir=$HOME/.basher
if ! [ -d $target_dir ]; then
	mkdir -p $target_dir
else
	rm -r $target_dir/*
fi

cp -r ./scripts $target_dir
cp basher.bashrc $target_dir

if ! [ -n "$BASHER" ]; then
	echo "Please append the following into your .bashrc file:"
	echo "  . ~/.basher/basher.bashrc"
fi
