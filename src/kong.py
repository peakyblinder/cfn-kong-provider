import os
import logging
import cfn_kong_api_provider
import cfn_kong_plugin_provider
import cfn_kong_consumer_provider
import cfn_kong_acl_provider
import cfn_kong_credential_provider

logging.basicConfig(level=os.getenv('LOG_LEVEL', 'INFO'))


def handler(request, context):
    if request['ResourceType'] == 'Custom::KongAPI':
        return cfn_kong_api_provider.handler(request, context)
    elif request['ResourceType'] == 'Custom::KongPlugin':
        return cfn_kong_plugin_provider.handler(request, context)
    elif request['ResourceType'] == 'Custom::KongACL':
        return cfn_kong_acl_provider.handler(request, context)
    elif request['ResourceType'] == 'Custom::KongCredential':
        return cfn_kong_credential_provider.handler(request, context)
    else:
        return cfn_kong_consumer_provider.handler(request, context)
