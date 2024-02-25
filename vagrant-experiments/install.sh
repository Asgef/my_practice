#!/usr/bin/env bash

# Включение режима отладки
set -x


# Обновление системы
sudo apt-get update
# sudo apt-get upgrade
sudo apt dist-upgrade -y


# Установка GIT
#sudo apt install git

# Обновление GIT
sudo add-apt-repository ppa:git-core/ppa
sudo apt-get update
sudo apt-get install git -y


# Установка пользовательского приглашения в Bash для пользователя vagrant
echo "PS1='💻 \[\e[1;34m\]\W\[\e[m\]\[\033[32m\]\$(__git_ps1)\[\033[00m\] \$ '" >> /home/vagrant/.bashrc

# Установка алиаса для питона
echo "alias py='python3'" >> /home/vagrant/.bashrc


# Установка PIP
#sudo apt install pip -y


# Установка netstat
sudo apt install net-tools -y



# Установка супурвизора
# pip install supervisor
# sudo apt install supervisor -y


# Установка ASDF
git clone https://github.com/asdf-vm/asdf.git ~/.asdf --branch v0.14.0 # Требуется обновление команды
. /home/vagrant/.asdf/asdf.sh
. /home/vagrant/.asdf/completions/asdf.bash

echo '. $HOME/.asdf/asdf.sh' >> /home/vagrant/.bashrc
echo 'export PATH="$HOME/.asdf/bin:$HOME/.asdf/shims:$PATH"' >> /home/vagrant/.bashrc

# Установка зависимостей для Python
sudo apt-get update
# sudo apt-get install -y libbz2-dev libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev # liblzma-dev libgdbm-dev libnss3-dev libssl-dev

# Установка Python через ASDF
# asdf plugin add python
# asdf install python 3.12.1
# asdf global python 3.12.1

# Установка Node.js через ASDF
asdf plugin add nodejs https://github.com/asdf-vm/asdf-nodejs.git
asdf install nodejs latest


# Установка Caddy
# sudo apt install -y debian-keyring debian-archive-keyring apt-transport-https
# curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | sudo gpg --dearmor -o /usr/share/# keyrings/caddy-stable-archive-keyring.gpg
# curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | sudo tee /etc/apt/# sources.list.d/caddy-stable.list
# sudo apt update && sudo apt install caddy


# Установка PHP

# apt install php-common libapache2-mod-php php-cli -y


# Установка PostgreSQL и настройка пользователя и базы данных
# sudo apt install -y postgresql
# sudo systemctl start postgresql
# sudo systemctl enable postgresql

# Создание пользователя и базы данных, если они еще не существуют
# sudo -u postgres psql -c "SELECT 1 FROM pg_roles WHERE rolname='vagrant'" | grep -q 1 || sudo -u postgres createuser --createdb vagrant
# sudo -u postgres psql -lqt | cut -d \| -f 1 | grep -qw hexlet || sudo -u postgres createdb --owner=vagrant hexlet

# Версии ПО

git --version
# python3 --version
node -v
