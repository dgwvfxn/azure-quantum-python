# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, TYPE_CHECKING

from azure.core import PipelineClient
from azure.core.pipeline import policies
from azure.core.rest import HttpRequest, HttpResponse

from ._configuration import QuantumClientConfiguration
from ._serialization import Deserializer, Serializer
from .operations import (
    JobsOperations,
    ProvidersOperations,
    QuotasOperations,
    SessionsOperations,
    StorageOperations,
    TopLevelItemsOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential


class QuantumClient:  # pylint: disable=client-accepts-api-version-keyword
    """Azure Quantum REST API client.

    :ivar jobs: JobsOperations operations
    :vartype jobs: azure.quantum._client.operations.JobsOperations
    :ivar providers: ProvidersOperations operations
    :vartype providers: azure.quantum._client.operations.ProvidersOperations
    :ivar storage: StorageOperations operations
    :vartype storage: azure.quantum._client.operations.StorageOperations
    :ivar quotas: QuotasOperations operations
    :vartype quotas: azure.quantum._client.operations.QuotasOperations
    :ivar sessions: SessionsOperations operations
    :vartype sessions: azure.quantum._client.operations.SessionsOperations
    :ivar top_level_items: TopLevelItemsOperations operations
    :vartype top_level_items: azure.quantum._client.operations.TopLevelItemsOperations
    :param azure_region: Supported Azure regions for Azure Quantum Services. For example, "eastus".
     Required.
    :type azure_region: str
    :param subscription_id: The Azure subscription ID. This is a GUID-formatted string (e.g.
     00000000-0000-0000-0000-000000000000). Required.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group. Required.
    :type resource_group_name: str
    :param workspace_name: Name of the workspace. Required.
    :type workspace_name: str
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.TokenCredential
    :keyword api_version: Api Version. Default value is "2023-11-13-preview". Note that overriding
     this default value may result in unsupported behavior.
    :paramtype api_version: str
    """

    def __init__(
        self,
        azure_region: str,
        subscription_id: str,
        resource_group_name: str,
        workspace_name: str,
        credential: "TokenCredential",
        **kwargs: Any
    ) -> None:
        _endpoint = "https://{azureRegion}.quantum.azure.com"
        self._config = QuantumClientConfiguration(
            azure_region=azure_region,
            subscription_id=subscription_id,
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            credential=credential,
            **kwargs
        )
        _policies = kwargs.pop("policies", None)
        if _policies is None:
            _policies = [
                policies.RequestIdPolicy(**kwargs),
                self._config.headers_policy,
                self._config.user_agent_policy,
                self._config.proxy_policy,
                policies.ContentDecodePolicy(**kwargs),
                self._config.redirect_policy,
                self._config.retry_policy,
                self._config.authentication_policy,
                self._config.custom_hook_policy,
                self._config.logging_policy,
                policies.DistributedTracingPolicy(**kwargs),
                policies.SensitiveHeaderCleanupPolicy(**kwargs) if self._config.redirect_policy else None,
                self._config.http_logging_policy,
            ]
        self._client: PipelineClient = PipelineClient(base_url=_endpoint, policies=_policies, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False
        self.jobs = JobsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.providers = ProvidersOperations(self._client, self._config, self._serialize, self._deserialize)
        self.storage = StorageOperations(self._client, self._config, self._serialize, self._deserialize)
        self.quotas = QuotasOperations(self._client, self._config, self._serialize, self._deserialize)
        self.sessions = SessionsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.top_level_items = TopLevelItemsOperations(self._client, self._config, self._serialize, self._deserialize)

    def send_request(self, request: HttpRequest, *, stream: bool = False, **kwargs: Any) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client.send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        path_format_arguments = {
            "azureRegion": self._serialize.url(
                "self._config.azure_region", self._config.azure_region, "str", skip_quote=True
            ),
        }

        request_copy.url = self._client.format_url(request_copy.url, **path_format_arguments)
        return self._client.send_request(request_copy, stream=stream, **kwargs)  # type: ignore

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "QuantumClient":
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details: Any) -> None:
        self._client.__exit__(*exc_details)
