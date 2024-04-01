# Install Ngnix web server (w/ Puppet)

package { 'nginx':
  ensure => present,
}

file_line { 'add_redirection':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => 'server_name _;',
  line   => 'rewrite ^/redirect$ https://youtu.be/dQw4w9WgXcQ?si=c5SSrhdJz17xP0kV',
}

file { '/var/www/html/index.html':
  content => 'Hello, World!',
}

service { 'nginx':
  ensure => running,
  require => Package['nginx'],
}
