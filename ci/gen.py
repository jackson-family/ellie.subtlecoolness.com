import json
import pathlib


THIS_FILE = pathlib.PurePosixPath(
    pathlib.Path(__file__).relative_to(pathlib.Path().resolve())
)


def gen(content: dict, target: str):
    pathlib.Path(target).parent.mkdir(parents=True, exist_ok=True)
    pathlib.Path(target).write_text(
        json.dumps(content, indent=2, sort_keys=True), newline="\n"
    )


def gen_dependabot(target: str):
    def update(ecosystem: str) -> dict:
        return {
            "package-ecosystem": ecosystem,
            "allow": [{"dependency-type": "all"}],
            "directory": "/",
            "schedule": {"interval": "daily"},
        }

    ecosystems = ["github-actions", "npm", "uv"]
    content = {
        "version": 2,
        "updates": [update(e) for e in ecosystems],
    }

    gen(content, target)


def gen_github_workflows(target: str):
    content = {
        "env": {
            "description": f"This workflow ({target}) was generated from {THIS_FILE}",
        },
        "name": "Deploy site",
        "on": {"push": {"branches": ["main"]}, "workflow_dispatch": {}},
        "concurrency": {"cancel-in-progress": True, "group": "github-pages"},
        "jobs": {
            "deploy": {
                "name": "Deploy site",
                "runs-on": "ubuntu-latest",
                "environment": {
                    "name": "github-pages",
                    "url": "${{ steps.deployment.outputs.page_url }}",
                },
                "permissions": {
                    "contents": "read",
                    "pages": "write",
                    "id-token": "write",
                },
                "steps": [
                    {"name": "Check out repository", "uses": "actions/checkout@v4"},
                    {
                        "name": "Configure GitHub Pages",
                        "uses": "actions/configure-pages@v5",
                    },
                    {"name": "Build site", "run": "sh ci/build.sh"},
                    {
                        "name": "Upload artifact",
                        "uses": "actions/upload-pages-artifact@v3",
                        "with": {"path": "output"},
                    },
                    {
                        "name": "Deploy to GitHub Pages",
                        "id": "deployment",
                        "uses": "actions/deploy-pages@v4",
                    },
                ],
            },
        },
    }

    gen(content, target)


def gen_package_json(target: str):
    content = {
        "dependencies": {"bootstrap": "5.3.7"},
        "description": f"This file ({target}) was generated from {THIS_FILE}",
        "license": "UNLICENSED",
        "name": "ellie.subtlecoolness.com",
        "private": True,
        "version": "1.0.0",
    }

    gen(content, target)


def main():
    gen_dependabot(".github/dependabot.yaml")
    gen_github_workflows(".github/workflows/github-pages.yaml")
    gen_package_json("package.json")


if __name__ == "__main__":
    main()
