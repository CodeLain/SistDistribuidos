from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa

public_key = b'''-----BEGIN RSA PRIVATE KEY-----
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
-----END RSA PRIVATE KEY-----'''


private_key = b'''-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEA6vl8RsKRFfe2uSc5i/U3
G+pzIzMpgHY07e55K6jplOWMVBMa1pvyErwR+Qo4hYx1dZhgTk+Rh/89YyYdbviH
JDTMNllGkEQFgyzgqxfHRVpPrI0DzUvLRKtfdPG4REku2PB7WlXqcAdYpj8vloKE
qs3sYzwsaIZKn9P/CfiSVlyf72g9VnDsDOd6rEY3m/LdGzAuT8gPtXX+LqeP2i1b
hqXyLAppMeSIY4K1NGAbxtPQUs31oNi0njhVZeuHWpu+OsWJHYXF3UXZrKZNMKcb
H/K8OWqbBZRLsnvXHa9ih2KEKI9ifC92gBz0fbST4/ETBB+cp0H28KUx4SPRPY5g
htyoiL0aJqlfszfWUPS/DrzQn1yCTIGTHkBaisGo8VkJ1lkWLDg1aSvAAmyEe7jo
1JaMvlCCHop2YL6bMvJqAikse1IUotpPK5n09/ZH+KkkYZgMbi1EYBcEpJ4itQa/
uawJ+zqJWnv0EPJpfvhoAvBnYB88Qq+g6DPL2u7oKu9kLDfNM3gl2HmQC3CEKfhv
IEgDTCXF9vxL6mvJzBga3mISb6zwvY6WbtAigKHMcPL/rDJjry3CtuEUdOBx/aOh
arjfxEPHcQ2VqUkdmu0nXPc4eF/n5bS8qVo7yUxkEgXfp1V6aSATqsTf2xKmhnHa
rtfULcl+1fa6/SZdIbOOtPECAwEAAQ==
-----END PUBLIC KEY-----'''