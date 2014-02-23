# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.box = "ubuntu"

  config.vm.synced_folder "./", "/src"

  Vagrant.configure("2") do |config|
    config.vm.provision "shell", path: "build/provision-vagrant.sh"
  end

end
