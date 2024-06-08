# a manifest that fixes server error on a Wordpress Apache server

exec {'fix_apache':
  command => "sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php && apache2ctl restart",
  path    => ['/bin/', '/usr/sbin/', '/usr/bin'],
}
