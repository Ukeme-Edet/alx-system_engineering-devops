# A puppet script to configure the Local SSH client so that we can connect to the remote SSH server without password.

file_line { 'Identity file':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/school',
}
file_line { 'disable password login':
  path => '/etc/ssh/ssh_config',
  line => '    PasswordAuthentication no',
}
