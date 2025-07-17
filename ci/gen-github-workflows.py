import gen
import pathlib

this_file = pathlib.PurePosixPath(
    pathlib.Path(__file__).relative_to(pathlib.Path().resolve())
)

target = ".github/workflows/github-pages.yaml"


content = {
    "env": {
        "description": f"This workflow ({target}) was generated from {this_file}",
    },
    "name": "Build and deploy site",
    "on": {"push": {"branches": ["main"]}, "workflow_dispatch": {}},
    "permissions": {"contents": "read", "pages": "write", "id-token": "write"},
    "concurrency": {"cancel-in-progress": True, "group": "github-pages"},
    "jobs": {
        "build": {
            "name": "Build site",
            "runs-on": "ubuntu-latest",
            "steps": [
                {"name": "Check out repository", "uses": "actions/checkout@v4"},
                {"name": "Configure Pages", "uses": "actions/configure-pages@v5"},
                {"name": "Build site", "run": "sh ci/build.sh"},
                {
                    "name": "Upload artifact",
                    "uses": "actions/upload-pages-artifact@v3",
                    "with": {"path": "output"},
                },
            ],
        },
        "deploy": {
            "name": "Deploy site",
            "runs-on": "ubuntu-latest",
            "environment": {
                "name": "github-pages",
                "url": "${{ steps.deployment.outputs.page_url }}",
            },
            "needs": "build",
            "steps": [
                {
                    "name": "Deploy to GitHub Pages",
                    "id": "deployment",
                    "uses": "actions/deploy-pages@v4",
                }
            ],
        },
    },
}

gen.gen(content, target)
