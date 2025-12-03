from aws_cdk import (aws_apigateway as apigateway, aws_apigatewayv2 as apigatewayv2)

class ExampleStack():
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        
        apigateway.DomainName(self, "example", domain_name="example.com", certificate=certificate, security_policy=apigateway.SecurityPolicy.TLS_1_2)

        
        tls10 = apigateway.SecurityPolicy.TLS_1_0
        tls12 = apigateway.SecurityPolicy.TLS_1_2
        tls10v2 = apigatewayv2.SecurityPolicy.TLS_1_0
        tls12v2 = apigatewayv2.SecurityPolicy.TLS_1_2

        
        apigateway.DomainName(security_policy=apigateway.SecurityPolicy.TLS_1_0) 
        apigateway.DomainName(security_policy=tls10) 
        apigatewayv2.DomainName(security_policy=apigatewayv2.SecurityPolicy.TLS_1_0) 
        apigatewayv2.DomainName(security_policy=tls10v2) 

        
        apigateway.DomainName()
        apigateway.DomainName(security_policy=apigateway.SecurityPolicy.TLS_1_2)
        apigateway.DomainName(security_policy=tls12)
        apigatewayv2.DomainName()
        apigatewayv2.DomainName(security_policy=apigatewayv2.SecurityPolicy.TLS_1_2)
        apigatewayv2.DomainName(security_policy=tls12v2)

class ExampleStack(Stack):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        
        apigateway.CfnDomainName(self, "compliant", domain_name="compliant.example.com", security_policy="TLS_1_2")

        
        tls10 = "TLS_1_0"
        tls12 = "TLS_1_2"

        
        apigateway.CfnDomainName(security_policy="TLS_1_0") 
        apigateway.CfnDomainName(security_policy=tls10) 

        
        apigateway.CfnDomainName()
        apigateway.CfnDomainName(security_policy="TLS_1_2")
        apigateway.CfnDomainName(security_policy=tls12)
        apigateway.CfnDomainName(security_policy="TLS_1_1") 

