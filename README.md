# Basher
A tool set for any OS that supports bash, to simplify everyday work.

## Install

1. Install perl and required modules
   ```
   $ sudo apt-get install perl
   ```
   in debian-based system or
   ```
   $ sudo yum install perl
   ```
   in centos-based system. Then
   ```
   $ cpan JSON::Parse
   ```
2. Download the code either by cloning the repository
   ```
   $ git clone https://github.com/yczhangsjtu/Basher.git
   ```
   or downloading and decompressing the package.
3. Go to the repository and run `./install.sh`. If you are installing for the first time, it will remind you to append `. ~/.basher/basher.bashrc` into your `~/.bashrc` file. Just do it.

## Utilities provided by Basher

After installing basher, the following commands are available.

### retab

Easily change the indentation of your file: from tab to space and vice versa, or change the tab width.

### template

Provide template programs for different programming languages and different frameworks.

### autoclean

Move all the stuff in the current directory to where they belong (usually the `Downloads` directory).

### pdftitle

Change the pdf filename to the title written in the pdf.
