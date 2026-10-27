English | [简体中文](SECURITY.zh_CN.md)

# Security Policy

Do not disclose unpatched vulnerabilities, credentials or personal data in public issues.

## Reporting

Use GitHub's private vulnerability reporting:
<https://github.com/Juicebro-star/guozhige-koubo/security/advisories/new>

If unavailable, open a public issue that only requests a private channel. Do not include reproduction details.

## Scope

This repository ships scripts and a Remotion project. Relevant risks: path traversal in `config.json` fields, unsafe shell interpolation in `2_make.sh`, dependency compromise in the render toolchain.

## Notes

Never commit API keys. Generation credentials belong to the user's own MiniMax / Metaso account and must stay out of the repo.
