# Fix the user limit

file { '/etc/security/limits.conf':
  content => "holberton hard nofile 4096\n",
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}

file { '/etc/pam.d/common-session':
  content => "session required pam_limits.so\n",
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}

file { '/etc/pam.d/common-session-noninteractive':
  content => "session required pam_limits.so\n",
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}
