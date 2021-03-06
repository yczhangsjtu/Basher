export BASHER="basher"

script_path="$HOME/.basher/scripts"
bash_script_path=`echo "$script_path/bash"`
alias template="$bash_script_path/template"

perl_script_path=`echo "$script_path/perl"`
alias retab="$perl_script_path/retab"
alias pdftitle="$perl_script_path/pdftitle"

python_script_path=`echo "$script_path/python"`
alias passgen="$python_script_path/passgen"
alias label-with-folder="$python_script_path/label-with-folder"
alias autoclean="$python_script_path/autoclean"
