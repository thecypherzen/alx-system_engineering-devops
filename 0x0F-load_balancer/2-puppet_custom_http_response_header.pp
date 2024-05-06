# Configures Nginx so that its HTTP response contains a custom header

$default_config = @(EOT)
server {
       listen 80 default_server;
       listen [::]:80 default_server;

       root /var/www/html;
       index index.html index.htm index.nginx-debian.html;

       server_name _;
       location / {
                try_files $uri $uri/ =404;
		add_header X-Served-By $hostname;
       }
}
| - EOT

# update apt
exec {'update_apt':
  command => '/usr/bin/apt update',
}

# ensure nginx is installed
package {'nginx':
  ensure   => latest,
  provider => apt,
}

# start nginx
service {'nginx.service':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

# ensure nginx default index has right content
file {'nginx_content':
  ensure  => present,
  path    => '/var/www/html/index.html',
  content => "Hello World!\n",
}


file {'nginx_default':
  ensure  => present,
  path    => '/etc/nginx/sites-available/default',
  content => $default_config,
}

# restart nginx
exec {'restart_nginx':
  command => 'systemctl restart nginx',
  path    => ['/usr/bin', '/bin'],
}
