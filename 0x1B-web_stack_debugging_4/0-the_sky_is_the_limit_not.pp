# Fix the number of max open files per process
exec { 'limits':
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:\
/sbin:/bin',
  command => "sudo sed -i 's/.*worker_processes.*/worker_processes 10;/' /etc/nginx/nginx.conf;
  sudo sed -i '/worker_processes 10;/a worker_rlimit_nofile 5000;' /etc/nginx/nginx.conf;
  sudo service nginx restart"
}
