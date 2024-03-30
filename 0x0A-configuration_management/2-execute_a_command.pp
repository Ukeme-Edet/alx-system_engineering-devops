# Using Puppet, create a manifest that kills a process named `killmenow`

# Requirements:
#   Must use the `exec` Puppet resource
#   Must use the `pkill`
exec { 'killmenow':
  path    => '/usr/bin:/bin',
  command => 'pkill killmenow',
  onlyif  => 'pgrep killmenow',
}
