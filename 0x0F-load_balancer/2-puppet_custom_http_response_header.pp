# A manifest that automates the task of creating a HTTP Header

package { 'nginx':
  ensure   => 'latest',
  provider => 'apt',
}

file { '/etc/nginx/sites-available/set_header':
  ensure  => present,
  content => "
server {
  listen 80;
  server_name 54.237.100.5;
  
  root /var/www/html;
  index index.html;

  location / {
     add_header X-Served-By "351953-web-01";
  }
}",
}

file { '/etc/nginx/sites-enabled/set_header':
  ensure => 'link',
  target => '/etc/nginx/sites-available/set_header',
}

file { '/etc/nginx/sites-enabled/default':
  ensure => absent,
}

service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => [File['/etc/nginx/sites-enabled/set_header'], Package['nginx']],
}
