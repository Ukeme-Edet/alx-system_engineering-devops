# Using Puppet, install `flask` from `pip3`

# Requirements:
#   Install `flask`
#   Version must be 2.1.0
exec { 'install_flask_2.1.0':
  command => 'pip3 install flask==2.1.0',
  path    => '/usr/local/bin',
  unless  => 'pip3 show flask | grep Version | grep 2.1.0'
}
