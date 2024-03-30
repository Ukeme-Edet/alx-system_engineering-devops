# A puppet script to configure the Local SSH client so that we can connect to the remote SSH server without password.

exec { 'ssh-keygen':
  command => 'ssh-keygen -b 4096 -N "" -f ~/.ssh/id_rsa',
  creates => '/root/.ssh/id_rsa',
}

exec { 'copy_pub_to_auth':
  command => 'cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys',
  require => Exec['ssh-keygen'],
}

exec { 'add_lines'
  commands => [
    'echo "Host *" >> ~/.ssh/config',
    'echo "StrictHostKeyChecking no" >> ~/.ssh/config',
    'echo "UserKnownHostsFile=/dev/null" >> ~/.ssh/config',
  ],
  require => Exec['copy_pub_to_auth'],
}
