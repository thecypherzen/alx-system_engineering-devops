# A puppet file that fixes limit on user's file
exec {'increase user hard limit':
  command => "/bin/sed -Ei 's/holberton hard.*[0-9]$/holberton hard nofile 8192/g' /etc/security/limits.conf",
}

exec {'increase user soft limit':
  command => "/bin/sed -Ei 's/holberton soft.*[0-9]$/holberton soft nofile 1024/g' /etc/security/limits.conf",
}
