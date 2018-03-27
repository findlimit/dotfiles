git clone https://github.com/findlimit/dotfiles.git ~/.dotfiles
cd ~/.dotfiles

# To Enable TMUX auto re-attach
touch ~/.tmux-auto

git remote set-url --push origin git@github.com:findlimit/dotfiles.git
./install
