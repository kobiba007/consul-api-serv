#!/usr/bin/env bash

CONSUL_VERSION=1.9.1

set -e

# Update
#apt-get update -y
apt-get install curl unzip -y


echo "Installing Consul $CONSUL_VERSION..."
CONSUL_ARCHIVE_HOME=/tmp
CONSUL_ARCHIVE=$CONSUL_ARCHIVE_HOME/consul.zip
curl -sSL https://releases.hashicorp.com/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_linux_amd64.zip > $CONSUL_ARCHIVE

if [[ ! -f /usr/bin/consul ]]
then
  pushd $CONSUL_ARCHIVE_HOME
  unzip $CONSUL_ARCHIVE
  install consul /usr/bin/consul
  popd
fi

groupadd --system consul
useradd -s /sbin/nologin --system -g consul consul

mkdir -p /var/lib/consul
chown -R consul:consul /var/lib/consul
chmod -R 775 /var/lib/consul

mkdir -p /etc/consul.d
cp /vagrant/0_server-base.hcl /etc/consul.d/
chown -R consul:consul /etc/consul.d

cp /vagrant/consul.service /etc/systemd/system

systemctl enable consul
systemctl start consul
