# Install Nginx web server (w/ Puppet) and add Custom HTTP Header
exec { 'apt-update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure => installed,
}

file_line { 'redirect_me':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://youtu.be/dQw4w9WgXcQ?si=c5SSrhdJz17xP0kV permanent;',
}

file_line { 'add_custom_header':
  ensure => 'present',
  path   => '/etc/nginx/nginx.conf',
  after  => 'listen 80 default_server;',
  line   => 'add_header X-Served-By $hostname;',
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}

