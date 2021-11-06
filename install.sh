#!/usr/bin/env bash

unameOut="$(uname -s)"
echo "running on ${unameOut}"
case "${unameOut}" in 
	Linux*) machine=Linux;;
	Darwin*) machine=Mac;;
	*) machine=
esac

if [ $machine == Mac ];
then
	if [ -f ~/.zshenv ];
	then 	
		configuration=~/.zshenv
	else 
		configuration=~/.zshrc
	fi
else
	configuration=~/.bashrc
fi


if [ ! -f $configuration ]; then
	touch $configuration
fi


pip3 install -r requeriments.txt
pip3 install --user . && echo "alias gilfoyle=${HOME}/.local/bin/gilfoyle" >> $configuration

source $configuration

echo "installed :D"
