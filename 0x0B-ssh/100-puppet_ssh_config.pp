# A client configuration file

file { '/etc/ssh/ssh_config':
   mode    => '0600',
   owner   => 'root',
   ensure  => present,
   content => 'PasswordAuthentication no
 IdentityFile ~/.ssh/school',
}
