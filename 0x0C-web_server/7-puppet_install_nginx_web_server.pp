$config = @("END"/$)
    server {
        listen 80 default_server;
	listen [::]:80 default_server;

	root /var/www/html;
       	index index.html;
       	server_name _;

       	location /redirect_me {
            return 301 https://google.com;
       	}

        location / {
           try_files \$uri \$uri/ =404;
        }

       error_page 404 /not_found.html;
       location = /not_found.html {
           internal;
       }
}
| END

package {'nginx':
  ensure   => installed,
  name     => nginx,
  provider => apt,
}


file {'config_file':
  ensure  => present,
  path    => '/etc/nginx/sites-available/default',
  content => $config,
  mode    => '0644',
}

file {'index':
  ensure  => present,
  path    => '/var/www/html/index.html',
  content => 'Hello World!',
}

file {'not_found':
  ensure  => present,
  path    => '/var/www/html/not_found.html',
  content => "Ceci n\'est pas une page\n",
}

exec {'reload_nginx':
  command => '/etc/init.d/nginx reload',
  user    => root,
}

exec {'start_nginx':
  command => '/etc/init.d/nginx start',
  user    => root,
}