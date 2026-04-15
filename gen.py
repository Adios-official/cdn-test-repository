import os

# Define the structure
folders = [
    "assets/js",
    "assets/css",
    "assets/img",
    "assets/docs",
    "assets/video"
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Helper to write files
def create_file(path, content):
    with open(path, "w") as f:
        f.write(content)
    print(f"✅ Created {path}")

# 1. Create JS files
create_file("assets/js/test.js", "console.log('CDN Test JS Loaded');")
create_file("assets/js/analytics.js", "console.log('Analytics Mock Loaded');")

# 2. Create CSS files
create_file("assets/css/test.css", "body { background-color: #f0f0f0; }")
create_file("assets/css/main.css", ".header { color: blue; font-weight: bold; }")

# 3. Create Text/Doc files
create_file("assets/docs/test.txt", "This is a plain text file for CDN testing.")
create_file("assets/docs/info.md", "# Documentation\nTesting Markdown files via CDN.")

# 4. Create a dummy "large" file for throughput testing (1MB)
with open("assets/docs/large-test.dat", "wb") as f:
    f.write(os.urandom(1024 * 1024))
print("✅ Created assets/docs/large-test.dat (1MB)")

# 5. Create a valid tiny 1x1 PNG image (Base64 trick)
import base64
pixel = base64.b64decode("iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==")
with open("assets/img/pixel.png", "wb") as f:
    f.close() # Touch file
with open("assets/img/test.png", "wb") as f:
    f.write(pixel)
print("✅ Created assets/img/test.png")

print("\n🚀 All files generated! Ready for 'git push'.")