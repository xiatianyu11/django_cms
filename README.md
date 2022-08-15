<VirtualHost *:80>
    <Proxy balancer://cluster>
        BalancerMember http://127.0.0.1:8092/api
    </Proxy>
    ProxyPreserveHost On
    ProxyPass /api balancer://cluster/
    ProxyPassReverse /api balancer://cluster/
</VirtualHost># django_cms


