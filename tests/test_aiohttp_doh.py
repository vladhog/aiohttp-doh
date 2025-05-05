import pytest
from aiohttp import ClientSession, TCPConnector

import aiohttp_doh
from aiohttp_doh import DNSOverHTTPSClientSession

pytest_plugins = ('pytest_asyncio',)


@pytest.mark.asyncio
async def test_DNSOverHTTPSResolver():
    endpoints = [
        'https://dns.google.com/resolve',
        'https://cloudflare-dns.com/dns-query',
    ]
    resolver = aiohttp_doh.DNSOverHTTPSResolver(endpoints=endpoints)
    connector = TCPConnector(resolver=resolver)
    async with ClientSession(connector=connector) as session:
        async with session.head("https://example.com") as response:
            assert response.status == 200


@pytest.mark.asyncio
async def test_DNSOverHTTPSClientSession():
    async with DNSOverHTTPSClientSession() as session:
        async with session.head("https://example.com") as response:
            assert response.status == 200
