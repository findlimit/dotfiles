git clone https://github.com/findlimit/dotfiles.git ~/.dotfiles
cd ~/.dotfiles

# To Enable TMUX auto re-attach
#touch ~/.tmux-auto

# Create an empty file for Asana token
touch ~/.asana_token

git remote set-url --push origin git@github.com:findlimit/dotfiles.git
./install
