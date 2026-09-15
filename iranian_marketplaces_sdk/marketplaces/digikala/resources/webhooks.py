"""Digikala webhooks: sync and async resource clients."""

from __future__ import annotations

from iranian_marketplaces_sdk.marketplaces.digikala.data.api import webhooks as models
from iranian_marketplaces_sdk.marketplaces.digikala.resources.base import (
    AsyncResource,
    SyncResource,
    parse_response,
)

EVENT_TYPES_PATH = "/webhook/event-types"
SUBSCRIBE_PATH = "/webhook/subscription"
UNSUBSCRIBE_PATH = "/webhook/unsubscription"
CHANGE_ACTIVATION_PATH = "/webhook/subscription/change-activation"


class WebhooksSync(SyncResource):
    def event_types(self) -> models.EventTypesResponse:
        """GET /webhook/event-types. Scopes => self_settings."""
        response = self._request("GET", EVENT_TYPES_PATH)
        return parse_response(models.EventTypesResponse, response)

    def subscribe(self, *, body: models.SubscribeRequest | None = None) -> models.SubscribeResponse:
        """POST /webhook/subscription. Scopes => self_settings."""
        response = self._request("POST", SUBSCRIBE_PATH, body=body)
        return parse_response(models.SubscribeResponse, response)

    def unsubscribe(
        self, *, body: models.UnsubscribeRequest | None = None
    ) -> models.UnsubscribeResponse:
        """POST /webhook/unsubscription. Scopes => self_settings."""
        response = self._request("POST", UNSUBSCRIBE_PATH, body=body)
        return parse_response(models.UnsubscribeResponse, response)

    def change_activation(
        self, *, body: models.ChangeActivationRequest | None = None
    ) -> models.ChangeActivationResponse:
        """POST /webhook/subscription/change-activation. Scopes => self_settings."""
        response = self._request("POST", CHANGE_ACTIVATION_PATH, body=body)
        return parse_response(models.ChangeActivationResponse, response)


class WebhooksAsync(AsyncResource):
    async def event_types(self) -> models.EventTypesResponse:
        """GET /webhook/event-types. Scopes => self_settings."""
        response = await self._request("GET", EVENT_TYPES_PATH)
        return parse_response(models.EventTypesResponse, response)

    async def subscribe(
        self, *, body: models.SubscribeRequest | None = None
    ) -> models.SubscribeResponse:
        """POST /webhook/subscription. Scopes => self_settings."""
        response = await self._request("POST", SUBSCRIBE_PATH, body=body)
        return parse_response(models.SubscribeResponse, response)

    async def unsubscribe(
        self, *, body: models.UnsubscribeRequest | None = None
    ) -> models.UnsubscribeResponse:
        """POST /webhook/unsubscription. Scopes => self_settings."""
        response = await self._request("POST", UNSUBSCRIBE_PATH, body=body)
        return parse_response(models.UnsubscribeResponse, response)

    async def change_activation(
        self, *, body: models.ChangeActivationRequest | None = None
    ) -> models.ChangeActivationResponse:
        """POST /webhook/subscription/change-activation. Scopes => self_settings."""
        response = await self._request("POST", CHANGE_ACTIVATION_PATH, body=body)
        return parse_response(models.ChangeActivationResponse, response)
