git clone https://github.com/findlimit/dotfiles.git ~/.dotfiles
cd ~/.dotfiles

# To Enable YCM vim plugin
mkdir ~/.vim
touch ~/.vim/.ycm_support

git remote set-url --push origin git@github.com:findlimit/dotfiles.git
./install
