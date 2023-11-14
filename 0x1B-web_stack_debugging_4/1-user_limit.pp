# Increases soft and hard limit

exec { 'hard_limit_increment':
    command => '/bin/sed -i "/^holberton hard/s/5/5000/" /etc/security/limits.conf',
    path    => '/bin:/usr/bin:/usr/local/bin',
}

exec { 'Soft_limit_increment':
    command => '/bin/sed -i "/^holberton soft/s/4/5000/" /etc/security/limits.conf',
    path    => '/bin:/usr/bin:/usr/local/bin',
}
