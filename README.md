# 1NFER crypto inference connection check

An opt-in, dependency-free GitHub Action checking the public 1NFER model catalogue and payment terms. No API key, account creation, paid generation, inference spend, code upload or crypto transfer. Two bounded GETs, no retries or redirects.

```yaml
- uses: hesoyambusiness/1nfer-connection-check@v1.0.0
```

Prefer the verified release commit SHA for a pinned dependency. Python3 must exist on the runner. No GitHub token or write permission needed. Outputs: `model-count` and `funding-enabled`. Neither proves model completion, quality or every invoice currency.

Connect through [1NFER](https://1nfer.net/?utm_source=github_action&utm_medium=readme&utm_campaign=connection_check). Read [integration instructions](https://1nfer.net/guides/crypto-inference-agents.html) and actual account rates before funding. Scoped router/business setup: [HESOYAM](https://hesoyam.business/router). No guaranteed income or customers.

Tests: `python3 -m unittest test_probe.py`.
