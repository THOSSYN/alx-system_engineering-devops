# A puppet manifest to install nginx

# site.pp

# Set DEBIAN_FRONTEND to non-interactive mode to avoid prompts during installation
exec { 'set DEBIAN_FRONTEND':
  command => 'export DEBIAN_FRONTEND=noninteractive',
  path    => ['/bin', '/usr/bin'],
  creates => '/etc/environment',
}

# Install Nginx package
package { 'nginx':
  ensure  => 'installed',
  require => Exec['set DEBIAN_FRONTEND'],
}

# Define Nginx server configuration as a string
$file_content = @(EOT)
server {
    listen 80;
    listen [::] 80; 
    root /var/www/test_website/html;
    index.html index.htm;
    server_name mywebsite.com www.mywebsite.com;

    location / {
      return 301 $scheme://www.mywebsite.com$request_uri;
    }
}
EOT

file { '/etc/nginx/sites-available/test_website':
  ensure  => 'present',
  content => $file_content,
  require => Package['nginx'],
}

# Create index.html file content as a string
$index_html_content = @(EOT)
<!DOCTYPE html>
<html>
<head>
</head>
<body>
<h1>Hello World!</h1>
</body>
</html>
EOT

file { '/var/www/test_website/html/index.html':
  ensure  => 'present',
  content => $index_html_content,
}

# Enable the Nginx site
file { '/etc/nginx/sites-enabled/test_website':
  ensure  => 'link',
  target  => '/etc/nginx/sites-available/test_website',
  require => File['/etc/nginx/sites-available/test_website'],
}

# Define Nginx listen80 configuration as a string
$listen80_content = @(EOT)
server {
    listen 80;
}
EOT

file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => $listen80_content,
  require => Package['nginx'],
}

# Verify that Nginx returns "Hello World!" on GET request to /
exec { 'test_nginx_root':
  command => "curl -s http://localhost/ | grep -q 'Hello World!'",
  path    => '/usr/bin:/usr/sbin:/bin',
  require => Package['nginx'],
}
