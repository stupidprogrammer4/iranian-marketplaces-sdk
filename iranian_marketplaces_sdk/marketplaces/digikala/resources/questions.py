"""Digikala questions: sync and async resource clients."""

from __future__ import annotations

from iranian_marketplaces_sdk.marketplaces.digikala.data.api import questions as models
from iranian_marketplaces_sdk.marketplaces.digikala.resources.base import (
    AsyncResource,
    SyncResource,
    parse_response,
    path_value,
)

LIST_PATH = "/questions"
GET_PATH = "/questions/{question_id}"
ANSWER_PATH = "/questions/answer"


class QuestionsSync(SyncResource):
    def list(self, *, query: models.ListQuery | None = None) -> models.ListResponse:
        """GET /questions. Scopes => question."""
        response = self._request(
            "GET", LIST_PATH, query=query, separators={"search[answer-status]": ","}
        )
        return parse_response(models.ListResponse, response)

    def get(self, question_id: int) -> models.GetResponse:
        """GET /questions/{question_id}. Scopes => question."""
        response = self._request("GET", GET_PATH.format(question_id=path_value(question_id)))
        return parse_response(models.GetResponse, response)

    def answer(self, *, body: models.AnswerRequest) -> models.AnswerResponse:
        """POST /questions/answer. Scopes => question."""
        response = self._request("POST", ANSWER_PATH, body=body)
        return parse_response(models.AnswerResponse, response)


class QuestionsAsync(AsyncResource):
    async def list(self, *, query: models.ListQuery | None = None) -> models.ListResponse:
        """GET /questions. Scopes => question."""
        response = await self._request(
            "GET", LIST_PATH, query=query, separators={"search[answer-status]": ","}
        )
        return parse_response(models.ListResponse, response)

    async def get(self, question_id: int) -> models.GetResponse:
        """GET /questions/{question_id}. Scopes => question."""
        response = await self._request("GET", GET_PATH.format(question_id=path_value(question_id)))
        return parse_response(models.GetResponse, response)

    async def answer(self, *, body: models.AnswerRequest) -> models.AnswerResponse:
        """POST /questions/answer. Scopes => question."""
        response = await self._request("POST", ANSWER_PATH, body=body)
        return parse_response(models.AnswerResponse, response)
