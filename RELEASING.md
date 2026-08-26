# Releasing

The published artifact is built from a git tag, and the tag is checked against the version
recorded in the package. A release therefore cannot be cut from an unpushed working tree, and the
version on PyPI always matches a commit anyone can check out.

## One-time setup: Trusted Publishing

PyPI can verify a GitHub Actions workflow by its OIDC identity, so no API token has to be stored
in the repository's secrets. Nothing to rotate, nothing to leak.

1. Sign in at <https://pypi.org>, open **Your projects → Publishing → Add a pending publisher**.
2. Fill in exactly:
   - PyPI project name: `iranian-marketplaces-sdk`
   - Owner: `stupidprogrammer4`
   - Repository: `iranian-marketplaces-sdk`
   - Workflow name: `release.yml`
   - Environment name: `pypi`
3. In the GitHub repository, **Settings → Environments → New environment** named `pypi`. Adding a
   required reviewer here makes every publish a manual approval.

A *pending* publisher is what you register before the project exists on PyPI; the first successful
run creates the project and converts it to a normal publisher.

## Cutting a release

```bash
# 1. Bump the version — it lives in exactly one place.
#    pyproject.toml reads it from here via [tool.hatch.version].
$EDITOR iranian_marketplaces_sdk/__init__.py   # __version__ = "0.3.0"

# 2. Make sure the tree is green.
ruff check . && ruff format --check . && mypy && pytest -q

# 3. Commit, tag, push.
git commit -am "release: 0.3.0"
git tag v0.3.0
git push && git push --tags
```

Pushing the tag runs `.github/workflows/release.yml`, which builds the sdist and wheel, refuses to
continue if the tag and the packaged version disagree, and publishes.

## Publishing by hand

Only needed if Actions is unavailable. Requires an API token from
<https://pypi.org/manage/account/token/>, entered as the password with `__token__` as the
username.

```bash
python -m pip install --upgrade build twine
rm -rf dist
python -m build
python -m twine check dist/*

# Rehearse against TestPyPI first — a version number on real PyPI can never be reused,
# even after deleting the release.
python -m twine upload --repository testpypi dist/*
python -m twine upload dist/*
```

## Verifying a release

```bash
python -m venv /tmp/verify && /tmp/verify/bin/pip install iranian-marketplaces-sdk
/tmp/verify/bin/python -c "import iranian_marketplaces_sdk as m; print(m.__version__, m.available())"
```
