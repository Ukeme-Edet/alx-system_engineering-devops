# A script to find out why Apache is returning a 500 error using strace
# Usage: ./0-strace_is_your_friend.pp
# Example: curl -sI
#
# This script will use strace to find out why Apache is returning a 500 error
# when you try to access the root of the server. It will then fix the issue
# and make sure Apache is running.
exec { 'apt-get-update':
  command => '/usr/bin/apt-get update',
}

package { 'apache2':
  ensure  => installed,
  require => Exec['apt-get-update'],
}

file_line { 'a':
  ensure  => 'present',
  path    => '/etc/apache2/sites-available/000-default.conf',
  after   => '<VirtualHost *:80>',
  line    => 'ServerName localhost',
  require => Package['apache2'],
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
  require => Package['apache2'],
}

service { 'apache2':
  ensure  => running,
  require => Package['apache2'],
}
