# Configures Nginx so that its HTTP response contains a custom header

exec {'update_apt':
     command => "/usr/bin/apt update"
}

package {'nginx':
	ensure   => latest,
	provider => apt,
}


file {'nginx_content':
     ensure  => present,
     path    => "/var/www/html/index.html",
     content => "Hello World!",
}


file_line {'nginx_default':
	ensure  => present,
	path    => "/etc/nginx/sites-available/default",
	line    => "\t*add_header X-Served-By ${hostname};",
	after   => '\t*try_files \$uri \$uri/ =404;',
	require => Package['nginx'],
}


service {'nginx.service':
	ensure  => running,
	enable  => true,
	require => Package['nginx'],
}
