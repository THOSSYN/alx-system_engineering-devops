exec { 'Fix_nginx_soft_limit':
    command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
    path    => '/bin:/usr/bin:/usr/sbin',
    notify  => Service['nginx'],
}

service { 'nginx':
    ensure     => 'running',
    enable     => true,
    hasrestart => true,
    hasstatus  => true,
}
