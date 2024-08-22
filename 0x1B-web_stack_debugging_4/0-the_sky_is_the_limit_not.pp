# a puppet manifest to raise max open files limit on nginx

exec { 'raise nginx file limits':
  command => "/bin/sed -Ei 's/15/4096/g' /etc/default/nginx",
}

-> exec { 'restart nginx':
  command => '/usr/sbin/service nginx restart',
  #require => Exec['raise nginx file limits'], -> alt
}

