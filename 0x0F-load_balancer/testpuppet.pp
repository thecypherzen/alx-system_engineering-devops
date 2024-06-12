$content = @(EOF)
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
| - EOF

file {'nginx_default':
  ensure  => present,
  path    => '/etc/nginx/sites-available/default',
  content => $content,
}
