from OpenSSL import SSL
import ssl
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager

SSL.Context(SSL.SSLv2_METHOD)  
SSL.Context(method=SSL.SSLv2_METHOD)  
SSL.Context(SSL.TLSv1_2_METHOD)  
SSL.Context(method=SSL.TLSv1_2_METHOD)  

ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv2) 
ctx = ssl.SSLContext(protocol=ssl.PROTOCOL_SSLv2) 
ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1) 
ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1_1) 
ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2) 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_SSLv2) 

ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2) 
ctx = ssl.SSLContext(protocol=ssl.PROTOCOL_TLSv1_2) 


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1_2) 

def default_protocol_attributes():
    
    ssl.SSLContext() 
    ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT) 
    ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER) 
    ssl.SSLContext(ssl.PROTOCOL_TLS) 

    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT) 
    ctx.minimum_version = ssl.TLSv1_2  

    secure_ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    secure_ctx.minimum_version = ssl.TLSv1_3  

    unsafe_ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT) 
    unsafe_ctx.minimum_version = ssl.TLSv1_1  

    
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ctx.minimum_version = ssl.TLSv1_1

    
    invalid_ctx[42] = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT) 
    invalid_ctx.minimum_version = ssl.TLSv1_3


def setting_unsafe_maximum_version():
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER) 
    ctx.maximum_version = ssl.TLSVersion.TLSv1_1


def disabling_unsafe_protocols_through_options():
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    
    ctx.options |= ssl.OP_NO_SSLv2
    ctx.options |= ssl.OP_NO_SSLv3
    ctx.options |= ssl.OP_NO_TLSv1
    ctx.options |= ssl.OP_NO_TLSv1_1
    
    ctx2 = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)  
    ctx2.options |= (ssl.OP_NO_SSLv2 | ssl.OP_NO_SSLv3 | ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1)

def incomplete_disabling_unsafe_protocols_through_options():
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)  

    ctx.options |= ssl.OP_NO_SSLv2
    ctx.options |= ssl.OP_NO_TLSv1
    ctx.options |= ssl.OP_NO_TLSv1_1

    ctx2 = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)  
    ctx2.options |= (ssl.OP_NO_SSLv2 | ssl.OP_NO_SSLv3 | ssl.OP_NO_TLSv1)

def invalid_options_context():
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)  
    foo(ctx.options)
    ctx.options = ssl.OP_NO_SSLv2
    ctx.options |= get_options() 

class Ssl3Adapter(HTTPAdapter):
    """"Transport adapter that forces SSLv3"""

    def init_poolmanager(self, *pool_args, **pool_kwargs):

        self.poolmanager = PoolManager(
            *pool_args,
            ssl_version=ssl.PROTOCOL_SSLv3, 
            **pool_kwargs)

class Tls12Adapter(HTTPAdapter):
    """"Transport adapter that forces TLSv1.2"""

    def init_poolmanager(self, *pool_args, **pool_kwargs):
        self.poolmanager = PoolManager(
            *pool_args,
            ssl_version=ssl.PROTOCOL_TLSv1_2,
            **pool_kwargs)


class unrelated():
    someClass.S = toto
    PROTOCOL_SSLv2 = "someconstant"
    def met():
        foo(PROTOCOL_SSLv2) 


def using_create_default_context():
    ctx = ssl.create_default_context()  
    client_ctx = ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH)  
    server_ctx = ssl.create_default_context(purpose=ssl.Purpose.CLIENT_AUTH)  
    ctx_with_ca = ssl.create_default_context(cafile="ca.pem")  
    
    ctx_secure = ssl.create_default_context()  
    ctx_secure.minimum_version = ssl.TLSv1_3
    
    ctx_unsafe = ssl.create_default_context()  
    ctx_unsafe.minimum_version = ssl.TLSv1_1

    ctx_max_unsafe = ssl.create_default_context()  
    ctx_max_unsafe.maximum_version = ssl.TLSv1_1

    
    ctx_options_secure = ssl.create_default_context()  
    ctx_options_secure.options |= ssl.OP_NO_SSLv2
    ctx_options_secure.options |= ssl.OP_NO_SSLv3
    ctx_options_secure.options |= ssl.OP_NO_TLSv1
    ctx_options_secure.options |= ssl.OP_NO_TLSv1_1

    client_ctx = ssl.create_default_context(purpose=unknown())

def test_openssl_default_tls_methods():
    from OpenSSL import SSL
    
    
    ctx1 = SSL.Context(SSL.TLS_METHOD)  
    ctx2 = SSL.Context(SSL.TLS_SERVER_METHOD)  
    ctx3 = SSL.Context(method=SSL.TLS_CLIENT_METHOD)  
    
    
    ctx4 = SSL.Context(SSL.TLS_METHOD)  
    ctx4.set_min_proto_version(SSL.TLS1_2_VERSION)
    
    ctx5 = SSL.Context(SSL.TLS_SERVER_METHOD)  
    ctx5.set_min_proto_version(SSL.TLS1_3_VERSION)
    
    
    ctx6 = SSL.Context(SSL.TLS_CLIENT_METHOD)  
    ctx6.set_min_proto_version(SSL.TLS1_1_VERSION)
    
    
    ctx7 = SSL.Context(SSL.TLS_METHOD)  
    ctx7.set_options(SSL.OP_NO_SSLv2 | SSL.OP_NO_SSLv3 | SSL.OP_NO_TLSv1 | SSL.OP_NO_TLSv1_1)
    
    ctx8 = SSL.Context(SSL.TLS_SERVER_METHOD)  
    ctx8.set_options(SSL.OP_NO_SSLv2)
    ctx8.set_options(SSL.OP_NO_SSLv3)
    ctx8.set_options(SSL.OP_NO_TLSv1)
    ctx8.set_options(SSL.OP_NO_TLSv1_1)
    
    
    ctx9 = SSL.Context(SSL.TLS_CLIENT_METHOD)  
    ctx9.set_options(SSL.OP_NO_SSLv2 | SSL.OP_NO_SSLv3 | SSL.OP_NO_TLSv1)
    
    
    ctx10 = SSL.Context(SSL.TLS_METHOD)  
    ctx10.set_min_proto_version(SSL.TLS1_2_VERSION)
    ctx10.set_options(SSL.OP_NO_SSLv2 | SSL.OP_NO_SSLv3)
    
    
    ctx11 = SSL.Context(SSL.TLS_SERVER_METHOD)  
    foo(ctx11.set_options)
    
    
    ctx12 = SSL.Context(SSL.TLS_CLIENT_METHOD)
    ctx12.set_min_proto_version(SSL.TLS1_2_VERSION)
    ctx12 = SSL.Context(SSL.TLS_CLIENT_METHOD)  

    ctx13 = SSL.Context(SSL.TLS_SERVER_METHOD) 
    ctx13.set_options()

    
    foo(SSL.Context(SSL.TLS_SERVER_METHOD)) 

    ctx14 = SSL.Context(SSL.TLS_SERVER_METHOD) 
    
    bar(ctx14)
