# script for setting up python 3 in termux on android
# taken from discussion here:
# https://www.reddit.com/r/tasker/comments/7bdtzu/running_a_python_script/

apt update
apt install -y git termux-tools
apt install -y coreutils
apt install -y python
apt install -y neovim
apt install -y curl

# neovim setup
apt install -y clang
apt install -y python-dev
mkdir -p ~/.config/nvim
mkdir -p ~/.local/share/nvim/site/autoload
git clone https://github.com/chiplukes/init.vim.git ~/.config/nvim/cfg
bash ~/.config/nvim/cfg/install.sh
python -m pip install neovim

# put python files in this folder
mkdir -p .termux/tasker
# start of python file needs:  #!/data/data/com.termux/files/usr/bin/env python
# also make sure python file is executable: chmod +x ./hello.py

pkg install -y termux-exec

# failed attempt at getting pyenv set up :(
# curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
# export PATH="/data/data/com.termux/files/home/.pyenv/bin:$PATH"
# eval "$(pyenv init -)"
# eval "$(pyenv virtualenv-init -)"

# Other stuff
#termux-setup-storage
