Write-Host "Building application (docker)"

# Create a directory
Write-Host "+ create output directory 'dist/'"
New-Item -ItemType Directory -Path "dist" -Force

# Adding build dependencies
Write-Host "+ installing build dependencies"
poetry self add poetry-bumpversion

# Linting source for errors
Write-Host "+ linting sourcecode (result in dist\source.lint)"
poetry run flake8 . | Out-File -FilePath "dist\source.lint"

# Checking source for vulnerabilities
Write-Host "+ checking for vulnerabilities (result in dist\source.vuln)"
poetry run bandit -r . -c "pyproject.toml" | Out-File -FilePath "dist\source.vuln"

# Building Docker image
Write-Host "+ building docker image"
docker build --pull --rm -f "Dockerfile" -t prat:v0.1.0 "."