mp3list
=======

Necessary apache config
-----

I use Apache because nginx's x-sendfile support is awful.

    <VirtualHost *:80>
        ServerName example.com
    
        ProxyPass / http://localhost:56344/
        ProxyPassReverse / http://localhost:56344/
        ProxyRequests Off
    
        <Proxy http://localhost:56344/*>
          Require all granted
        </Proxy>
        <Location />
          XSendFile on
          XSendFilePath /music
        </Location>
        Customlog /var/log/apache2/access.log combined
        ErrorLog /var/log/apache2/error.log
        LogLevel debug
    </VirtualHost>

Setup
-----

Install `flask` from pypi using pip or easy\_install or whatever. Edit config.py[.sample] with the path to the files, the same one you put into the apache config above. `./run.py`

Original implementation (PHP): https://gist.github.com/blha303/c769a6d0da207f2d3ac9

[Issues](https://github.com/blha303/mp3list/issues)    
[Questions](https://github.com/blha303/mp3list/issues)    
[Rants/raging](https://github.com/blha303/mp3list/issues)    
[Love letters](https://github.com/blha303/mp3list/issues)
