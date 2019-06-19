#!/bin/bash

yum update -y
yum install -y zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel git openssl-devel xz xz-devel libffi-devel findutils

curl https://pyenv.run | bash

echo 'export PATH="/root/.pyenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
source ~/.bashrc

pyenv install 2.7.3
pyenv install 3.7.3

pyenv virtualenv 2.7.3 1st
pyenv virtualenv 3.7.3 2st


