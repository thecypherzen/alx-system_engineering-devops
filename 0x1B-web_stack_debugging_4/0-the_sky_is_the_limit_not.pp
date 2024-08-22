# a puppet manifest to raise max open files limit on nginx

exec { 'raise nginx file limits':
  command => "sed -Ei 's/#ULIMIT=.*/ULIMIT=\"-n 65500\"/g' /etc/default/nginx",
  path    => ['/bin/', '/usr/bin', '/usr/sbin'],
}

exec { 'restart nginx':
  command => 'service nginx restart',
  path    => ['/bin/', '/usr/bin', '/usr/sbin/'],
}

