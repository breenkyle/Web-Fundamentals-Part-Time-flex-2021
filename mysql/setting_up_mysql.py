
# Create mysql alias for terminal connection:
# **Note** These instructions are for if you are using zsh as you bash window.  If you are using bash, replace .zshrc with .bash_profile

# Run the below command in the terminal window.

echo 'export PATH=${PATH}:/usr/local/mysql/bin' >> ~/.zshrc && source ~/.zshrc


# Let's take a look at what line is doing.

# echo will write to a file.
# export PATH=${PATH}:/usr/local/mysql/bin
# export at the beginning makes the value available to programs that you run from the terminal
# PATH= sets the value of the PATH variable
# ${PATH} expands to the current value
# /usr/local/mysql/bin is the location of the mysql executable we just installed.
# >> will append to a file.
# ~/.zshrc is a file that the terminal window will look at for any commands to run.
# && will run another command.
# source ~/.zshrc will execute the changes made and make them available in the terminal window.
