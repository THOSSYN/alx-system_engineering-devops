# Kills a process using pkill

exec { 'pkillyou':
  command => 'pkill -f killmenow',
  path    => '/usr/bin:/usr/sbin:/bin',
  returns => 0,
}
