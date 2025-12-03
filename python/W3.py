from aws_cdk import (aws_opensearchservice as opensearch)
from aws_cdk import (aws_elasticsearch as elasticsearch)

class OpenSearchStack(Stack):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        
        opensearch.Domain(self, "default", version=opensearch.EngineVersion.OPENSEARCH_1_0, tls_security_policy=opensearch.TLSSecurityPolicy.TLS_1_2)

        
        os_tls10 = opensearch.TLSSecurityPolicy.TLS_1_0
        os_tls12 = opensearch.TLSSecurityPolicy.TLS_1_2
        es_tls10 = elasticsearch.TLSSecurityPolicy.TLS_1_0
        es_tls12 = elasticsearch.TLSSecurityPolicy.TLS_1_2

        
        opensearch.Domain() 
        opensearch.Domain(tls_security_policy=opensearch.TLSSecurityPolicy.TLS_1_0) 
        opensearch.Domain(tls_security_policy=os_tls10) 
        elasticsearch.Domain() 
        elasticsearch.Domain(tls_security_policy=elasticsearch.TLSSecurityPolicy.TLS_1_0) 
        elasticsearch.Domain(tls_security_policy=es_tls10) 

        
        elasticsearch.Domain(tls_security_policy=elasticsearch.TLSSecurityPolicy.TLS_1_2) 
        elasticsearch.Domain(tls_security_policy=es_tls12) 


class CfnOpenSearchStack(Stack):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        
        opensearch.CfnDomain(self, "compliant", domain_endpoint_options=opensearch.CfnDomain.DomainEndpointOptionsProperty(tls_security_policy="Policy-Min-TLS-1-2-2019-07"))

        
        str_tls_10 = "Policy-Min-TLS-1-0-2019-07"
        str_tls_12 = "Policy-Min-TLS-1-2-2019-07"
        domain_endpoint_options_tls_10 = opensearch.CfnDomain.DomainEndpointOptionsProperty(tls_security_policy="Policy-Min-TLS-1-0-2019-07")
        domain_endpoint_options_tls_12 = opensearch.CfnDomain.DomainEndpointOptionsProperty(tls_security_policy="Policy-Min-TLS-1-2-2019-07")
        dict_tls_10 = {"tls_security_policy":"Policy-Min-TLS-1-0-2019-07"}
        dict_tls_12 = {"tls_security_policy":"Policy-Min-TLS-1-2-2019-07"}

        
        opensearch.CfnDomain() 
        opensearch.CfnDomain(domain_endpoint_options=opensearch.CfnDomain.DomainEndpointOptionsProperty)
        opensearch.CfnDomain(domain_endpoint_options=opensearch.CfnDomain.DomainEndpointOptionsProperty()) 
        opensearch.CfnDomain(domain_endpoint_options=opensearch.CfnDomain.DomainEndpointOptionsProperty(tls_security_policy="Policy-Min-TLS-1-0-2019-07")) 
        opensearch.CfnDomain(domain_endpoint_options=opensearch.CfnDomain.DomainEndpointOptionsProperty(tls_security_policy=str_tls_10)) 
        opensearch.CfnDomain(domain_endpoint_options={"any_key":"any_value"}) 
        opensearch.CfnDomain(domain_endpoint_options={"tls_security_policy":"Policy-Min-TLS-1-0-2019-07"}) 
        opensearch.CfnDomain(domain_endpoint_options={"tls_security_policy":str_tls_10}) 
        opensearch.CfnDomain(domain_endpoint_options=dict_tls_10) 
        elasticsearch.CfnDomain(domain_endpoint_options=elasticsearch.CfnDomain.DomainEndpointOptionsProperty()) 

        
        opensearch.CfnDomain(domain_endpoint_options=opensearch.CfnDomain.DomainEndpointOptionsProperty(tls_security_policy="Policy-Min-TLS-1-2-2019-07"))
        opensearch.CfnDomain(domain_endpoint_options=opensearch.CfnDomain.DomainEndpointOptionsProperty(tls_security_policy=str_tls_12))
        opensearch.CfnDomain(domain_endpoint_options={"tls_security_policy":"Policy-Min-TLS-1-2-2019-07"})
        opensearch.CfnDomain(domain_endpoint_options={"any_key":"any_value", "tls_security_policy":"Policy-Min-TLS-1-2-2019-07"})
        opensearch.CfnDomain(domain_endpoint_options={"tls_security_policy":str_tls_12})
        opensearch.CfnDomain(domain_endpoint_options=[])
        opensearch.CfnDomain(domain_endpoint_options=dict_tls_12)
        elasticsearch.CfnDomain(domain_endpoint_options=elasticsearch.CfnDomain.DomainEndpointOptionsProperty(tls_security_policy="Policy-Min-TLS-1-2-2019-07"))
