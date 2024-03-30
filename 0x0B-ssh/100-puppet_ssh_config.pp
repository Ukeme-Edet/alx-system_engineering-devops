# A puppet script to configure the Local SSH client so that we can connect to the remote SSH server without password.

file_line { 'IdentityFile':
  ensure => present,
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/id_rsa',
}
file_line { 'disable password authentication':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
}
